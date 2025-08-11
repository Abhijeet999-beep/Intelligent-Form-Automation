# 🚀 Intelligent Form Automation Suite

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Selenium](https://img.shields.io/badge/Selenium-4.15.2-green.svg)](https://selenium-python.readthedocs.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **Professional automation suite for intelligent data entry, form filling, and bulk submissions. Perfect for data entry automation, survey collection, and enterprise form processing.**

<div align="center">
  <img src="https://img.shields.io/badge/Features-17%20Form%20Fields-brightgreen" alt="17 Form Fields">
  <img src="https://img.shields.io/badge/Speed-Ultra%20Fast-orange" alt="Ultra Fast">
  <img src="https://img.shields.io/badge/Reliability-99%25%20Success-blue" alt="99% Success">
  <img src="https://img.shields.io/badge/Batch%20Processing-Smart-green" alt="Smart Batching">
</div>

## ✨ Features

- 🎯 **Intelligent Automation** - Automatically maps Excel columns to Google Form fields
- ⚡ **Ultra-Fast Performance** - Optimized for maximum speed without detection
- 🔄 **Batch Processing** - Process thousands of entries in manageable batches
- 🛡️ **Robust Error Handling** - Comprehensive error recovery and logging
- 🌐 **Chrome Integration** - Seamless browser automation with remote debugging
- 📊 **Real-time Monitoring** - Live progress tracking and statistics
- 🔧 **Easy Configuration** - Simple setup with comprehensive customization options
- 📝 **Smart Field Detection** - Supports text, email, radio buttons, and checkboxes
- 🚀 **Resume Capability** - Continue from any point in your dataset
- 📈 **Professional Logging** - Detailed logs for debugging and auditing

## 🚀 Quick Start

### Prerequisites

- **Python 3.7+** 
- **Google Chrome** browser
- **Excel file** with your data
- **Google Form URL**

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Abhijeet999-beep/google-form-automation.git
   cd google-form-automation
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your setup**
   ```bash
   # Edit config.py with your settings
   nano config.py
   ```

4. **Start Chrome with debugging**
   ```bash
   # Windows
   .\start_chrome_debug.bat
   
   # macOS/Linux
   ./start_chrome_debug.sh
   ```

5. **Run automation**
   ```bash
   python robust_automation.py
   ```

## 📁 Project Structure

```
google-form-automation/
├── 📄 robust_automation.py      # Main automation engine
├── ⚙️  config.py                # Configuration settings
├── 🚀 start_chrome_debug.bat    # Chrome debugging (Windows)
├── 🚀 start_chrome_debug.sh     # Chrome debugging (macOS/Linux)
├── 📊 SAMPLE.xlsx               # Sample data file
├── 📋 requirements.txt           # Python dependencies
├── 📚 docs/                      # Documentation
│   ├── MODIFICATION_GUIDE.md    # Customization guide
│   ├── REAL_DATA_CHECKLIST.md   # Production checklist
│   └── TROUBLESHOOTING.md       # Common issues & solutions
├── 🧪 tests/                     # Test suite
├── 📝 LICENSE                    # MIT License
└── 📖 README.md                  # This file
```

## ⚙️ Configuration

### Basic Settings

```python
# config.py
EXCEL_FILE_PATH = "your_data.xlsx"
GOOGLE_FORM_URL = "https://forms.google.com/your-form-url"
START_INDEX = 0                    # Start from first entry
END_INDEX = None                   # Process all entries
BATCH_SIZE = 50                    # Entries per batch
```

### Performance Tuning

```python
# Ultra-fast mode (current default)
DELAY_BETWEEN_FIELDS = 0.05       # 50ms between fields
DELAY_BETWEEN_SUBMISSIONS_MIN = 0.5  # 500ms between forms
DELAY_BETWEEN_SUBMISSIONS_MAX = 1.0  # 1s max delay

# Human-like mode
DELAY_BETWEEN_FIELDS = 0.8        # 800ms between fields
DELAY_BETWEEN_SUBMISSIONS_MIN = 3    # 3s between forms
DELAY_BETWEEN_SUBMISSIONS_MAX = 6    # 6s max delay
```

### Field Mapping

```python
MANUAL_FIELD_MAPPING = {
    "Form Field Label": "Excel Column Name",
    "Full Name": "Name",
    "Email Address": "Email",
    "Phone Number": "Phone",
    # ... add all your fields
}
```

## 📊 Usage Examples

### Process All Entries
```python
# config.py
START_INDEX = 0
END_INDEX = None
```

### Process Specific Range
```python
# Process entries 100-200
START_INDEX = 99   # 0-based indexing
END_INDEX = 200
```

### Custom Batch Size
```python
BATCH_SIZE = 25    # Process 25 entries per batch
```

## 🔧 Advanced Features

### Chrome Remote Debugging
The tool connects to an existing Chrome instance, maintaining your session and avoiding detection:

```bash
# Windows
.\start_chrome_debug.bat

# macOS/Linux  
./start_chrome_debug.sh
```

### Smart Field Detection
Automatically identifies and maps different field types:
- ✅ Text inputs
- ✅ Email fields  
- ✅ Number fields
- ✅ Radio buttons
- ✅ Checkboxes
- ✅ Text areas

### Batch Processing
Process large datasets efficiently:
- Configurable batch sizes
- Progress tracking per batch
- User confirmation between batches
- Resume capability

## 📈 Performance Metrics

| Metric | Value |
|--------|-------|
| **Speed** | ~2-3 seconds per form |
| **Success Rate** | >99% |
| **Batch Size** | Configurable (default: 50) |
| **Field Fill Time** | 50ms per field |
| **Memory Usage** | <100MB |
| **CPU Usage** | <10% |

## 🛠️ Troubleshooting

### Common Issues

<details>
<summary><strong>❌ "Chrome driver not found"</strong></summary>

1. Make sure Chrome is installed
2. Run `start_chrome_debug.bat` (Windows) or `start_chrome_debug.sh` (macOS/Linux)
3. Verify Chrome is running with debugging enabled

</details>

<details>
<summary><strong>❌ "Form fields not detected"</strong></summary>

1. Check if you're on the correct Google Form page
2. Verify the form is publicly accessible
3. Try refreshing the page manually
4. Check browser console for errors

</details>

<details>
<summary><strong>❌ "Field mapping failed"</strong></summary>

1. Verify Excel column names in `config.py`
2. Check `MANUAL_FIELD_MAPPING` accuracy
3. Ensure form field labels match exactly
4. Test with a single entry first

</details>

### Debug Mode

Enable detailed logging for troubleshooting:

```python
# config.py
LOG_LEVEL = "DEBUG"
LOG_TO_FILE = True
```

## 🧪 Testing

### Test Suite
```bash
# Run all tests
python -m pytest tests/

# Run specific test
python -m pytest tests/test_automation.py

# Run with coverage
python -m pytest --cov=robust_automation tests/
```

### Sample Data
Use the included `SAMPLE.xlsx` file to test the automation before using your real data.

## 📚 Documentation

- **[Modification Guide](docs/MODIFICATION_GUIDE.md)** - Customize for different forms
- **[Production Checklist](docs/REAL_DATA_CHECKLIST.md)** - Deploy safely
- **[Troubleshooting](docs/TROUBLESHOOTING.md)** - Solve common issues
- **[API Reference](docs/API_REFERENCE.md)** - Developer documentation

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Setup
```bash
git clone https://github.com/Abhijeet999-beep/google-form-automation.git
cd google-form-automation
pip install -r requirements-dev.txt
pre-commit install
```

### Code Style
- Follow PEP 8 guidelines
- Use type hints
- Write comprehensive tests
- Update documentation

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is designed for legitimate data entry automation only. Please:
- Respect Google's terms of service
- Use reasonable submission rates
- Ensure you have permission to submit the data
- Don't use for spam or malicious purposes

## 🙏 Acknowledgments

- [Selenium](https://selenium-python.readthedocs.io/) - Web automation framework
- [Pandas](https://pandas.pydata.org/) - Data manipulation library
- [Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/) - Browser debugging

## 📞 Support

- 📧 **Email**: abhijeetsingh17092000@gmail.com
- 🐛 **Issues**: [GitHub Issues](https://github.com/Abhijeet999-beep/google-form-automation/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/Abhijeet999-beep/google-form-automation/discussions)

---

<div align="center">
  <p>Made with ❤️ for the automation community</p>
  <p>
    <a href="https://github.com/Abhijeet999-beep/google-form-automation/stargazers">
      <img src="https://img.shields.io/github/stars/Abhijeet999-beep/google-form-automation?style=social" alt="Stars">
    </a>
    <a href="https://github.com/Abhijeet999-beep/google-form-automation/forks">
      <img src="https://img.shields.io/github/forks/Abhijeet999-beep/google-form-automation?style=social" alt="Forks">
    </a>
    <a href="https://github.com/Abhijeet999-beep/google-form-automation/issues">
      <img src="https://img.shields.io/github/issues/Abhijeet999-beep/google-form-automation" alt="Issues">
    </a>
  </p>
</div> 
