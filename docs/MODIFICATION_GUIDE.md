# 🚀 DMSReg Automation - Modification Guide

## 📋 **Quick Overview**
This guide shows you how to modify your automation system for different scenarios.

## 🎯 **Main Files You Need to Know**

### **Primary Files:**
- **`robust_automation.py`** - Main automation script (USE THIS ONE)
- **`config.py`** - All settings and configurations
- **`SAMPLE.xlsx`** - Your Excel data file

### **Backup Files (Don't Modify):**
- `dmsreg_robust.py`, `dmsreg_automation.py`, `dmsreg_specialized.py`, `dmsreg_with_auth.py` - Backup scripts

---

## 🔧 **Common Modifications**

### **1. Change Number of Entries to Process**

**File:** `config.py`
**Lines:** 8-9

```python
# Current setting (processes first 3 entries)
START_INDEX = 0  # Start from entry 1
END_INDEX = 3    # End at entry 3

# To process all 2000 entries:
START_INDEX = 0
END_INDEX = None  # None = process all entries

# To process entries 100-200:
START_INDEX = 99  # 0-based, so 99 = entry 100
END_INDEX = 200
```

### **2. Change Excel File**

**File:** `config.py`
**Line:** 4

```python
# Current setting
EXCEL_FILE_PATH = "SAMPLE.xlsx"

# To use a different file:
EXCEL_FILE_PATH = "your_new_file.xlsx"
```

### **3. Change Google Form URL**

**File:** `config.py`
**Line:** 5

```python
# Current setting
GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLScZiMztsJlaKmk673zgCJvGzY83vyzswxK-8xGZlevW3Gz9zg/viewform?usp=dialog"

# To use a different form:
GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/YOUR_NEW_FORM_ID/viewform"
```

### **4. Adjust Timing Delays**

**File:** `config.py`
**Lines:** 12-16

```python
# Current settings (human-like delays)
DELAY_BETWEEN_FIELDS = 0.8  # Seconds between filling each field
DELAY_BETWEEN_SUBMISSIONS_MIN = 3  # Min delay between forms
DELAY_BETWEEN_SUBMISSIONS_MAX = 6  # Max delay between forms
DELAY_AFTER_SUBMISSION = 2  # Delay after submitting form

# For maximum speed (current setting):
DELAY_BETWEEN_FIELDS = 0.1
DELAY_BETWEEN_SUBMISSIONS_MIN = 1
DELAY_BETWEEN_SUBMISSIONS_MAX = 2
DELAY_AFTER_SUBMISSION = 1

# For human-like behavior (slower):
DELAY_BETWEEN_FIELDS = 0.8
DELAY_BETWEEN_SUBMISSIONS_MIN = 3
DELAY_BETWEEN_SUBMISSIONS_MAX = 6
DELAY_AFTER_SUBMISSION = 2
```

---

## 📊 **Field Mapping Modifications**

### **Current Field Mappings (config.py lines 30-47):**

```python
MANUAL_FIELD_MAPPING = {
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
```

### **How to Modify Field Mappings:**

**Format:** `"Form Field Label": "Excel Column Name"`

**Example - If your Excel has different column names:**
```python
MANUAL_FIELD_MAPPING = {
    "Registration Number": "Reg_No",  # Changed from " Registration Number"
    "Name": "Full_Name",              # Changed from "Name"
    "Email Address": "Email",         # Changed from "Email Address"
    # ... rest of mappings
}
```

**Example - If your form has different field labels:**
```python
MANUAL_FIELD_MAPPING = {
    "Reg Number": " Registration Number",  # Changed from "Registration Number"
    "Full Name": "Name",                   # Changed from "Name"
    "Email": "Email Address",              # Changed from "Email Address"
    # ... rest of mappings
}
```

---

## 🚀 **How to Run Modifications**

### **Step 1: Make Your Changes**
Edit the appropriate file (usually `config.py`)

### **Step 2: Test Your Changes**
```cmd
python robust_automation.py
```

### **Step 3: Check Results**
- Monitor the terminal output
- Check the log file: `robust_automation_log.txt`

---

## 📝 **Common Scenarios**

### **Scenario 1: New Excel File with Different Column Names**

1. **Check your Excel column names:**
   - Open your Excel file
   - Note the exact column names in row 1

2. **Update field mappings in `config.py`:**
   ```python
   EXCEL_FILE_PATH = "your_new_file.xlsx"
   
   MANUAL_FIELD_MAPPING = {
       "Registration Number": "Your_Reg_Column_Name",
       "Name": "Your_Name_Column_Name",
       # ... update all mappings
   }
   ```

### **Scenario 2: Different Google Form**

1. **Get the new form URL:**
   - Open your new Google Form
   - Copy the URL from the address bar

2. **Update in `config.py`:**
   ```python
   GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/YOUR_NEW_FORM_ID/viewform"
   ```

3. **Check field labels:**
   - Open the form in browser
   - Note the exact field labels (e.g., "Name", "Email", etc.)
   - Update `MANUAL_FIELD_MAPPING` if needed

### **Scenario 3: Process Specific Range of Entries**

```python
# Process entries 500-600
START_INDEX = 499  # 0-based, so 499 = entry 500
END_INDEX = 600

# Process last 100 entries (if you have 2000 total)
START_INDEX = 1900  # 2000 - 100 = 1900
END_INDEX = None
```

### **Scenario 4: Faster Processing**

```python
# Reduce delays for faster processing
DELAY_BETWEEN_FIELDS = 0.2
DELAY_BETWEEN_SUBMISSIONS_MIN = 1
DELAY_BETWEEN_SUBMISSIONS_MAX = 2
DELAY_AFTER_SUBMISSION = 1
```

---

## ⚠️ **Important Notes**

### **Excel File Requirements:**
- Must be `.xlsx` format
- Column names must match exactly (including spaces)
- Data should start from row 1 (no header row)

### **Google Form Requirements:**
- Must be accessible (not private)
- Field labels must match exactly
- Form should be in "shuffle mode" compatible

### **Troubleshooting:**
- **Wrong data in fields:** Check field mappings
- **Fields not found:** Check field labels match exactly
- **Script not working:** Check Excel file path and form URL

---

## 🎯 **Quick Commands**

### **Run Automation:**
```cmd
python robust_automation.py
```

### **Check Current Settings:**
```cmd
python -c "from config import *; print(f'Excel: {EXCEL_FILE_PATH}'); print(f'Form: {GOOGLE_FORM_URL}'); print(f'Range: {START_INDEX+1} to {END_INDEX if END_INDEX else \"end\"}')"
```

### **View Log File:**
```cmd
type robust_automation_log.txt
```

---

## 📞 **Need Help?**

1. **Check the log file** for error messages
2. **Verify Excel column names** match exactly
3. **Verify form field labels** match exactly
4. **Test with small range** first (1-3 entries)

**Your automation is ready to use!** 🚀
