# Configuration file for DMSReg Google Form Automation
# Update these values according to your setup

# File paths
EXCEL_FILE_PATH = "SAMPLE.xlsx"  # Path to your Excel file with data (or rename to "DMSReg V 5.1 - 2K.xlsx")
GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfBzhW78iVBmU8t55ZTy_570J2ECyKrgrx51BRgeSRHaCLfGw/viewform?pli=1"  # Your Google Form URL

# Automation settings
START_INDEX = 1941  # Start from this entry (0-based indexing) - RESET FOR REAL DATA
END_INDEX = None  # End at this entry (None = process all entries)
BATCH_SIZE = 59  # Process entries in batches of 50

# Timing settings (in seconds) - MAXIMUM SPEED - NO MISTAKES
DELAY_BETWEEN_FIELDS = 0.05  # Ultra-fast field filling (50ms)
DELAY_BETWEEN_SUBMISSIONS_MIN = 0.5  # Ultra-fast submissions (500ms)
DELAY_BETWEEN_SUBMISSIONS_MAX = 1.0  # Ultra-fast submissions (1s)
DELAY_AFTER_SUBMISSION = 0.5  # Ultra-fast post-submission (500ms)

# Browser settings
HEADLESS_MODE = False  # Set to True to run browser in background
BROWSER_WINDOW_SIZE = "1920,1080"  # Browser window size

# Logging settings
LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR
LOG_TO_FILE = True  # Save logs to file
LOG_FILE_NAME = "dmsreg_automation_log.txt"

# Field mapping for DMSReg form (17 fields)
# Based on your sample file analysis, these are the exact column names
# Update these mappings based on your actual form field labels
MANUAL_FIELD_MAPPING = {
    # Exact mappings to ensure correct data goes to correct fields
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

# Form field selectors (advanced - only change if needed)
FORM_FIELD_SELECTORS = {
    "text_input": "input[type='text'], input[type='email'], input[type='number'], textarea",
    "choice_options": "div[role='radio'], div[role='checkbox']",
    "submit_button": "div[role='button'][data-value='Submit'], span[data-value='Submit']",
    "form_container": "div[role='main']"
}

# Retry settings
RETRY_FAILED_ENTRIES = True  # Whether to retry failed entries
MAX_RETRIES = 1  # Maximum number of retries per failed entry 