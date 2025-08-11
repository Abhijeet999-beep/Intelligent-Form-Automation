import pandas as pd
import time
import random
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from config import *
import os
from datetime import datetime

class RobustAutomation:
    def __init__(self):
        self.driver = None
        self.data = None
        self.setup_logging()
        
    def setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.StreamHandler(),
                logging.FileHandler("robust_automation_log.txt")
            ]
        )
        
    def setup_driver(self):
        """Setup Chrome driver to connect to existing browser instance"""
        try:
            chrome_options = Options()
            
            # Connect to existing Chrome instance
            chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
            
            # Create service and driver
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            
            logging.info("✅ Connected to existing Chrome browser successfully")
            return True
            
        except Exception as e:
            logging.error(f"❌ Error connecting to existing Chrome browser: {e}")
            logging.error("Make sure Chrome is running with remote debugging enabled")
            return False
    
    def check_browser_active(self):
        """Check if browser window is still active"""
        try:
            # Try to get current URL - this will fail if window is closed
            current_url = self.driver.current_url
            return True
        except Exception as e:
            logging.error(f"❌ Browser window is not active: {e}")
            return False
    
    def load_excel_data(self):
        try:
            self.data = pd.read_excel(EXCEL_FILE_PATH)
            logging.info(f"✅ Loaded {len(self.data)} entries from Excel")
            return True
        except Exception as e:
            logging.error(f"❌ Error loading Excel: {e}")
            return False
    
    def find_all_form_fields(self):
        """Find all form fields with multiple selectors"""
        fields = []
        
        # Check if browser is still active
        if not self.check_browser_active():
            logging.error("❌ Browser window is not active - cannot detect form fields")
            return fields
        
        # Wait for page to fully load (ultra-fast)
        time.sleep(1)
        
        # Debug: Print current URL to verify we're on the right page
        try:
            current_url = self.driver.current_url
            logging.info(f"🔍 Current URL: {current_url}")
        except Exception as e:
            logging.error(f"❌ Cannot get current URL: {e}")
            return fields
        
        # Method 1: Try the standard Google Forms selector
        try:
            found_fields = self.driver.find_elements(By.CSS_SELECTOR, "div[role='listitem']")
            if found_fields:
                fields.extend(found_fields)
                logging.info(f"Found {len(found_fields)} fields with selector: div[role='listitem']")
        except Exception as e:
            logging.info(f"Method 1 failed: {e}")
        
        # Method 2: Look for divs with "Your answer" text
        if not fields:
            try:
                all_divs = self.driver.find_elements(By.CSS_SELECTOR, "div")
                logging.info(f"Scanning {len(all_divs)} div elements for 'Your answer' text")
                
                for div in all_divs:
                    try:
                        div_text = div.text.strip()
                        if div_text and "Your answer" in div_text:
                            # Check if this div contains an input field
                            inputs_in_div = div.find_elements(By.CSS_SELECTOR, "input, textarea, div[contenteditable='true']")
                            if inputs_in_div:
                                fields.append(div)
                                logging.info(f"Found field with 'Your answer': {div_text[:50]}...")
                    except:
                        continue
                logging.info(f"Found {len(fields)} fields with 'Your answer' text")
            except Exception as e:
                logging.info(f"Method 2 failed: {e}")
        
        # Method 3: Direct input field detection
        if not fields:
            try:
                all_inputs = self.driver.find_elements(By.CSS_SELECTOR, "input[type='text'], input[type='email'], input[type='number'], textarea, div[contenteditable='true']")
                logging.info(f"Found {len(all_inputs)} direct input elements")
                
                for input_elem in all_inputs:
                    try:
                        # Find the form field container (parent with label)
                        parent = input_elem.find_element(By.XPATH, "./ancestor::div[position()<=5]")
                        if parent and parent not in fields:
                            # Check if this parent has a label or "Your answer" text
                            parent_text = parent.text.strip()
                            if parent_text and ("Your answer" in parent_text or any(label in parent_text for label in ["Age", "Name", "Email", "Registration", "Mobile", "Weight", "Gender", "Degree", "Institute", "Stream", "Work", "City", "Region", "Blood"])):
                                fields.append(parent)
                    except:
                        continue
            except Exception as e:
                logging.info(f"Method 3 failed: {e}")
        
        # Remove duplicates
        unique_fields = []
        seen_elements = set()
        
        for field in fields:
            try:
                field_id = field.id if field.get_attribute("id") else str(hash(field))
                if field_id not in seen_elements:
                    seen_elements.add(field_id)
                    unique_fields.append(field)
            except:
                continue
        
        logging.info(f"✅ Total unique form fields found: {len(unique_fields)}")
        return unique_fields
    
    def get_field_label(self, field):
        """Get field label with multiple methods"""
        try:
            # Get the full text of the field
            full_text = field.text.strip()
            
            # For Google Forms, the label is usually the first line before "Your answer"
            if "Your answer" in full_text:
                label = full_text.split("Your answer")[0].strip()
                return label
            
            # Try multiple selectors for field labels
            label_selectors = [
                "div[role='heading']",
                "span[dir='auto']",
                "label",
                "div[data-params*='title']",
                "div[class*='title']",
                "div[class*='label']"
            ]
            
            for selector in label_selectors:
                try:
                    label_elements = field.find_elements(By.CSS_SELECTOR, selector)
                    for label_element in label_elements:
                        label_text = label_element.text.strip()
                        if label_text and len(label_text) > 0:
                            return label_text
                except:
                    continue
            
            # Try to get from aria-label or title
            aria_label = field.get_attribute("aria-label")
            if aria_label:
                return aria_label.strip()
            
            title = field.get_attribute("title")
            if title:
                return title.strip()
            
            # Try to find label by looking for text that's not "Your answer"
            if full_text:
                lines = full_text.split('\n')
                for line in lines:
                    line = line.strip()
                    if line and line != "Your answer" and len(line) > 0:
                        return line
            
            return None
        except Exception as e:
            logging.error(f"❌ Error getting field label: {e}")
            return None
    
    def find_field_by_label(self, label_text):
        """Find form field by exact label text"""
        try:
            form_fields = self.find_all_form_fields()
            
            for field in form_fields:
                field_label = self.get_field_label(field)
                if field_label and field_label.strip() == label_text:
                    logging.info(f"✅ Found field: '{label_text}'")
                    return field
            
            # Try partial matching if exact match fails
            for field in form_fields:
                field_label = self.get_field_label(field)
                if field_label and label_text.lower() in field_label.lower():
                    logging.info(f"✅ Found field (partial match): '{field_label}' for '{label_text}'")
                    return field
            
            logging.error(f"❌ Field '{label_text}' not found")
            return None
        except Exception as e:
            logging.error(f"❌ Error finding field '{label_text}': {e}")
            return None
    
    def fill_field(self, label_text, value):
        """Fill a specific field by label"""
        try:
            field = self.find_field_by_label(label_text)
            if not field:
                return False
            
            # Try multiple input selectors
            input_selectors = [
                "input[type='text']",
                "input[type='email']", 
                "input[type='number']",
                "textarea",
                "input",
                "div[contenteditable='true']"
            ]
            
            input_element = None
            for selector in input_selectors:
                try:
                    input_element = field.find_element(By.CSS_SELECTOR, selector)
                    if input_element:
                        break
                except:
                    continue
            
            if not input_element:
                logging.error(f"❌ No input element found for '{label_text}'")
                return False
            
            # Clear and fill
            input_element.clear()
            time.sleep(0.05)
            
            value_str = str(value) if pd.notna(value) else ""
            
            # Type character by character (ultra-fast)
            for char in value_str:
                input_element.send_keys(char)
                time.sleep(random.uniform(0.0005, 0.002))
            
            logging.info(f"✅ Filled '{label_text}' with: {value_str[:30]}{'...' if len(value_str) > 30 else ''}")
            return True
            
        except Exception as e:
            logging.error(f"❌ Error filling '{label_text}': {e}")
            return False
    
    def find_submit_button(self):
        """Find and click the submit button"""
        try:
            # Try finding by text content first
            all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "div[role='button'], button, input[type='submit']")
            for button in all_buttons:
                try:
                    if "submit" in button.text.lower():
                        logging.info("✅ Found submit button by text content")
                        return button
                except:
                    continue
            
            # Try multiple selectors for submit button
            submit_selectors = [
                "div[role='button'][data-value='Submit']",
                "span[data-value='Submit']",
                "div[jsaction*='submit']",
                "div[class*='submit']",
                "div[class*='Submit']"
            ]
            
            for selector in submit_selectors:
                try:
                    submit_button = self.driver.find_element(By.CSS_SELECTOR, selector)
                    if submit_button and submit_button.is_displayed():
                        logging.info(f"✅ Found submit button with selector: {selector}")
                        return submit_button
                except:
                    continue
            
            logging.error("❌ Submit button not found")
            return None
            
        except Exception as e:
            logging.error(f"❌ Error finding submit button: {e}")
            return None
    
    def submit_form(self):
        """Submit the form automatically"""
        try:
            logging.info("📝 Attempting to submit form...")
            
            # Find and click submit button
            submit_button = self.find_submit_button()
            if not submit_button:
                logging.error("❌ Could not find submit button")
                return False
            
            # Click submit
            submit_button.click()
            logging.info("✅ Submit button clicked")
            time.sleep(1)  # Ultra-fast wait for submission
            
            # Check for "Submit another response" button
            time.sleep(1.5)  # Ultra-fast wait for page to load after submission
            
            # Look for "Submit another response" button with improved detection
            another_response_button = None
            
            # Method 1: Try finding by text content with more flexible matching
            all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "div[role='button'], button, a, span[role='button']")
            for button in all_buttons:
                try:
                    button_text = button.text.lower().strip()
                    if any(phrase in button_text for phrase in ["another response", "submit another", "new response", "fill another"]):
                        another_response_button = button
                        logging.info(f"✅ Found 'Submit another response' button: {button.text}")
                        break
                except:
                    continue
            
            # Method 2: Try finding by link text (for hyperlinks)
            if not another_response_button:
                try:
                    links = self.driver.find_elements(By.CSS_SELECTOR, "a")
                    for link in links:
                        try:
                            link_text = link.text.lower().strip()
                            if "another response" in link_text or "submit another" in link_text:
                                another_response_button = link
                                logging.info(f"✅ Found 'Submit another response' link: {link.text}")
                                break
                        except:
                            continue
                except:
                    pass
            
            # Method 3: Try finding by aria-label or title
            if not another_response_button:
                try:
                    all_elements = self.driver.find_elements(By.CSS_SELECTOR, "*")
                    for element in all_elements:
                        try:
                            aria_label = element.get_attribute("aria-label") or ""
                            title = element.get_attribute("title") or ""
                            aria_label = aria_label.lower().strip()
                            title = title.lower().strip()
                            
                            if any(phrase in aria_label or phrase in title for phrase in ["another response", "submit another", "new response"]):
                                if element.is_displayed() and element.is_enabled():
                                    another_response_button = element
                                    logging.info(f"✅ Found 'Submit another response' by aria-label/title: {aria_label or title}")
                                    break
                        except:
                            continue
                except:
                    pass
            
            # Method 4: Try finding by partial text match
            if not another_response_button:
                try:
                    all_clickable = self.driver.find_elements(By.CSS_SELECTOR, "[role='button'], button, a, [onclick], [jsaction]")
                    for element in all_clickable:
                        try:
                            if element.is_displayed() and element.is_enabled():
                                element_text = element.text.lower().strip()
                                if len(element_text) > 0 and ("another" in element_text and "response" in element_text):
                                    another_response_button = element
                                    logging.info(f"✅ Found potential 'another response' button: {element.text}")
                                    break
                        except:
                            continue
                except:
                    pass
            
            if another_response_button:
                logging.info("✅ Found 'Submit another response' button - clicking...")
                try:
                    # Scroll to the button to make sure it's visible
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", another_response_button)
                    time.sleep(0.3)
                    
                    # Click the button
                    another_response_button.click()
                    logging.info("✅ Clicked 'Submit another response' - New form loaded")
                    
                    # Wait for new form to load
                    time.sleep(1.5)
                    
                    # Verify we're back on a form page
                    fields = self.find_all_form_fields()
                    if len(fields) > 0:
                        logging.info(f"✅ Confirmed: New form loaded with {len(fields)} fields")
                        return True
                    else:
                        logging.warning("⚠️ New form doesn't seem to have fields, will load fresh form")
                        return False
                        
                except Exception as e:
                    logging.error(f"❌ Error clicking 'Submit another response': {e}")
                    return False
            else:
                logging.info("⚠️ 'Submit another response' button not found, will load fresh form")
                return False
                
        except Exception as e:
            logging.error(f"❌ Error submitting form: {e}")
            return False
    
    def fill_form(self, row_data, entry_num):
        """Fill form with data from Excel row and submit automatically"""
        try:
            logging.info(f"📊 Filling entry {entry_num + 1}")
            
            # Field mappings
            field_mappings = {
                "Registration Number": " Registration Number",
                "Name": "Name", 
                "Email Address": "Email Address",
                "Middle Initial": "Middle Initial",
                "Blood Group": "Blood Group",
                "Age": "Age ",
                "Mobile Number": "Mobile Number",
                "Weight in Kgs.": "Weight in Kgs.",
                "Gender": "Gender",
                "Degree": "Degree",
                "Institute": "Institute",
                "Stream": "Stream",
                "Register joining code": "Register joining code",
                "Age in Company (Years)": "Age in Company (Years)",
                "Work Experience": "Work Experience",
                "Current City": "Current City",
                "Region": "Region"
            }
            
            # Fill each field
            for field_label, excel_column in field_mappings.items():
                if excel_column in self.data.columns:
                    value = row_data[excel_column]
                    if pd.notna(value):
                        logging.info(f"   {field_label}: {value}")
                        self.fill_field(field_label, value)
                        time.sleep(0.05)  # Ultra-fast delay between fields
            
            logging.info(f"✅ Entry {entry_num + 1} filled - Submitting automatically...")
            
            # Submit form automatically
            if self.submit_form():
                logging.info(f"✅ Entry {entry_num + 1} submitted successfully!")
                return True
            else:
                logging.warning(f"⚠️ Entry {entry_num + 1} submission failed, will try fresh form")
                return False
            
        except Exception as e:
            logging.error(f"❌ Error filling entry {entry_num + 1}: {e}")
            return False
    
    def test_browser(self):
        """Test if browser is working properly"""
        try:
            # Check if we can get the current URL
            current_url = self.driver.current_url
            logging.info(f"✅ Browser test successful! Current URL: {current_url}")
            return True
            
        except Exception as e:
            logging.error(f"❌ Browser test failed: {e}")
            return False
    
    def run_automation(self):
        start_time = datetime.now()
        
        try:
            logging.info("🚀 Starting Robust Automation")
            
            # Setup driver to connect to existing browser
            if not self.setup_driver():
                logging.error("❌ Failed to connect to existing Chrome browser")
                return False
            
            # Test browser immediately
            if not self.test_browser():
                logging.error("❌ Browser test failed - cannot proceed")
                return False
            
            if not self.load_excel_data():
                return False
            
            # Debug: Print page source info
            try:
                page_title = self.driver.title
                logging.info(f"📄 Page title: {page_title}")
                
                # Check if we're on a Google Form
                if page_title and ("form" in page_title.lower() or "docs.google.com/forms" in self.driver.current_url):
                    logging.info("✅ Confirmed: Page appears to be a Google Form")
                else:
                    logging.warning("⚠️ Page doesn't appear to be a Google Form")
            except Exception as e:
                logging.error(f"❌ Error checking page info: {e}")
                print("⚠️ Warning: Could not verify page title. Make sure you're on the correct Google Form page.")
            
            # Check if we're on a submission confirmation page and navigate to fresh form
            current_url = self.driver.current_url
            if "formResponse" in current_url:
                print("🔄 Detected submission confirmation page - navigating to fresh form...")
                self.driver.get(GOOGLE_FORM_URL)
                time.sleep(1.5)
                print("✅ Navigated to fresh form")
            
            # Wait for form fields with multiple attempts
            form_detected = False
            for attempt in range(5):
                try:
                    print(f"🔍 Attempt {attempt + 1}: Looking for form fields...")
                    fields = self.find_all_form_fields()
                    if len(fields) > 0:
                        print(f"✅ Form detected! Found {len(fields)} fields")
                        form_detected = True
                        break
                    else:
                        print(f"⚠️  Attempt {attempt + 1}: No fields found, waiting...")
                        time.sleep(0.5)
                except Exception as e:
                    print(f"⚠️  Attempt {attempt + 1}: Error detecting fields: {e}")
                    time.sleep(0.5)
            
            if not form_detected:
                print("❌ Form not detected after 5 attempts")
                print("Please make sure you're on the correct Google Form page")
                print("Try refreshing the page and signing in again")
                return False
            
            # Process entries in batches from config
            end_index = END_INDEX if END_INDEX is not None else len(self.data)
            start_index = START_INDEX
            batch_size = BATCH_SIZE
            
            # Calculate batch information
            total_entries = min(end_index, len(self.data)) - start_index
            current_batch = (start_index // batch_size) + 1
            total_batches = (total_entries + batch_size - 1) // batch_size
            
            print(f"\n📊 BATCH PROCESSING INFO:")
            print(f"   Total entries to process: {total_entries}")
            print(f"   Batch size: {batch_size}")
            print(f"   Current batch: {current_batch}/{total_batches}")
            print(f"   Processing entries: {start_index + 1} to {min(end_index, len(self.data))}")
            print()
            
            successful_submissions = 0
            failed_submissions = 0
            
            for index in range(start_index, min(end_index, len(self.data))):
                logging.info(f"📝 Processing entry {index + 1}/{len(self.data)} (Batch {current_batch})")
                
                row_data = self.data.iloc[index]
                
                if self.fill_form(row_data, index):
                    successful_submissions += 1
                    print(f"\n🎯 ENTRY {index + 1} COMPLETED! ✅")
                    print(f"📊 Progress: {successful_submissions + failed_submissions}/{min(batch_size, total_entries)} in current batch")
                    
                    # Check if we need to load fresh form (if "Submit another response" failed)
                    if index + 1 < min(end_index, len(self.data)):
                        # Check if we're still on a form page
                        try:
                            fields = self.find_all_form_fields()
                            if len(fields) == 0:
                                print(f"\n🔄 Loading fresh form for entry {index + 2}...")
                                self.driver.get(GOOGLE_FORM_URL)
                                time.sleep(1.5)  # Ultra-fast wait time
                                
                                # Wait for form to load with more attempts
                                form_loaded = False
                                for attempt in range(10):  # Increased attempts
                                    try:
                                        fields = self.find_all_form_fields()
                                        if len(fields) > 0:
                                            form_loaded = True
                                            print(f"✅ Fresh form loaded successfully with {len(fields)} fields")
                                            break
                                        else:
                                            print(f"⚠️  Attempt {attempt + 1}: Form not loaded yet, waiting...")
                                            time.sleep(0.5)
                                    except Exception as e:
                                        print(f"⚠️  Attempt {attempt + 1}: Error checking form: {e}")
                                        time.sleep(0.5)
                                
                                if not form_loaded:
                                    print("⚠️  Form not loading automatically. Please manually navigate.")
                                    input("Press Enter when form is loaded...")
                                    # Check again after manual navigation
                                    try:
                                        fields = self.find_all_form_fields()
                                        if len(fields) > 0:
                                            print(f"✅ Manual navigation successful! Found {len(fields)} fields")
                                        else:
                                            print("⚠️  Still no fields found after manual navigation")
                                    except:
                                        print("⚠️  Error checking fields after manual navigation")
                        except Exception as e:
                            # If error checking fields, load fresh form
                            print(f"\n🔄 Loading fresh form for entry {index + 2} (error occurred: {e})...")
                            self.driver.get(GOOGLE_FORM_URL)
                            time.sleep(3)
                else:
                    failed_submissions += 1
                    logging.error(f"❌ Failed to fill entry {index + 1}")
                
                # Check if batch is complete
                entries_in_current_batch = (index - start_index + 1)
                if entries_in_current_batch >= batch_size:
                    print(f"\n🎉 BATCH {current_batch} COMPLETED!")
                    print(f"✅ Successful: {successful_submissions}")
                    print(f"❌ Failed: {failed_submissions}")
                    print(f"📊 Success Rate: {(successful_submissions/(successful_submissions+failed_submissions)*100):.1f}%")
                    
                    # Ask user if they want to continue with next batch
                    if index + 1 < min(end_index, len(self.data)):
                        print(f"\n🔄 Ready for next batch? (entries {index + 2} to {min(index + 1 + batch_size, min(end_index, len(self.data)))})")
                        response = input("Press Enter to continue, or type 'stop' to end: ").strip().lower()
                        if response == 'stop':
                            print("🛑 Automation stopped by user")
                            break
                        
                        # Reset counters for next batch
                        successful_submissions = 0
                        failed_submissions = 0
                        current_batch += 1
                
                # Progress update every 10 entries
                if (index + 1) % 10 == 0:
                    elapsed = datetime.now() - start_time
                    logging.info(f"📈 Progress: {index + 1}/{len(self.data)} entries")
                    logging.info(f"⏱️  Elapsed: {elapsed}")
                    logging.info(f"📊 Batch Progress: {entries_in_current_batch}/{batch_size}")
            
            total_time = datetime.now() - start_time
            print(f"\n🎉 AUTOMATION COMPLETED!")
            print(f"⏱️  Total time: {total_time}")
            print(f"📊 Final Statistics:")
            print(f"   ✅ Successful submissions: {successful_submissions}")
            print(f"   ❌ Failed submissions: {failed_submissions}")
            if successful_submissions + failed_submissions > 0:
                print(f"   📈 Success rate: {(successful_submissions/(successful_submissions+failed_submissions)*100):.1f}%")
            print(f"   🎯 Entries processed: {successful_submissions + failed_submissions}")
            
            return True
            
        except Exception as e:
            logging.error(f"❌ Error in automation: {e}")
            return False

def main():
    print("🚀 FULLY AUTOMATED DMSReg Form Filler")
    print("=" * 50)
    print("✅ Connects to existing Chrome browser")
    print("✅ Automatic form submission")
    print("✅ Automatic 'Submit another response'")
    print(f"✅ Batch processing ({BATCH_SIZE} forms per batch)")
    print("✅ Speed optimized for maximum efficiency")
    print("✅ Real-time progress tracking")
    print("=" * 50)
    
    print(f"📄 Excel file: {EXCEL_FILE_PATH}")
    print(f"🌐 Google Form: {GOOGLE_FORM_URL}")
    print(f"📊 Processing entries: {START_INDEX + 1} to {END_INDEX if END_INDEX else 'end'}")
    print()
    
    print("💡 TIP: Use 'start_chrome_debug.bat' to start Chrome with remote debugging")
    print()
    
    automation = RobustAutomation()
    success = automation.run_automation()
    
    if success:
        print("\n🎉 Robust automation completed!")
    else:
        print("\n❌ Automation failed. Check the log file.")

if __name__ == "__main__":
    main()
