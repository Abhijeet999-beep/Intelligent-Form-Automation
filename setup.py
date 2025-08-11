"""
Setup script for Intelligent Form Automation Suite
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="intelligent-form-automation",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Professional automation suite for intelligent data entry, form filling, and bulk submissions",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/intelligent-form-automation",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/intelligent-form-automation/issues",
        "Source": "https://github.com/yourusername/intelligent-form-automation",
        "Documentation": "https://github.com/yourusername/intelligent-form-automation#readme",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Office/Business",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: Browsers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Framework :: Selenium",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Text Processing :: Markup :: HTML",
        "Topic :: Utilities",
    ],
    python_requires=">=3.7",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=7.4.3",
            "pytest-cov>=4.1.0",
            "pytest-mock>=3.12.0",
            "flake8>=6.1.0",
            "black>=23.11.0",
            "isort>=5.12.0",
            "mypy>=1.7.1",
            "pre-commit>=3.5.0",
        ],
        "docs": [
            "sphinx>=7.2.6",
            "sphinx-rtd-theme>=1.3.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "form-automation=robust_automation:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.md", "*.txt", "*.bat", "*.sh", "*.xlsx"],
    },
    keywords=[
        "automation",
        "selenium",
        "google-forms",
        "data-entry",
        "web-automation",
        "excel",
        "pandas",
        "chrome",
        "browser-automation",
        "form-filling",
        "bulk-submission",
        "data-processing",
    ],
    platforms=["Windows", "macOS", "Linux"],
    license="MIT",
    zip_safe=False,
    test_suite="tests",
    tests_require=[
        "pytest>=7.4.3",
        "pytest-cov>=4.1.0",
        "pytest-mock>=3.12.0",
    ],
)
