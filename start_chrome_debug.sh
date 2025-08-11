#!/bin/bash

echo "Starting Chrome with remote debugging enabled..."
echo ""
echo "This will:"
echo "1. Close any existing Chrome windows"
echo "2. Start Chrome with remote debugging on port 9222"
echo "3. Use a separate user data directory to avoid conflicts"
echo ""
echo "After Chrome opens:"
echo "1. Navigate to your Google Form"
echo "2. Sign in to your Google account"
echo "3. Make sure you can see the form fields"
echo "4. Come back to the terminal and run: python robust_automation.py"
echo ""

# Kill any existing Chrome processes
pkill -f "Google Chrome" 2>/dev/null
sleep 2

# Detect OS and Chrome path
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    CHROME_PATH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    USER_DATA_DIR="$HOME/Library/Application Support/Chrome Debug"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    CHROME_PATH="/usr/bin/google-chrome"
    if [ ! -f "$CHROME_PATH" ]; then
        CHROME_PATH="/usr/bin/chromium-browser"
    fi
    if [ ! -f "$CHROME_PATH" ]; then
        CHROME_PATH="/usr/bin/chromium"
    fi
    USER_DATA_DIR="$HOME/.config/chrome-debug"
else
    echo "Unsupported operating system: $OSTYPE"
    exit 1
fi

# Check if Chrome exists
if [ ! -f "$CHROME_PATH" ]; then
    echo "Error: Chrome not found at $CHROME_PATH"
    echo "Please install Google Chrome or update the path in this script"
    exit 1
fi

# Create user data directory
mkdir -p "$USER_DATA_DIR"

# Start Chrome with remote debugging
echo "Starting Chrome with remote debugging..."
"$CHROME_PATH" --remote-debugging-port=9222 --user-data-dir="$USER_DATA_DIR" &

echo ""
echo "Chrome should now be running with remote debugging enabled."
echo "You can now run the automation script."
echo ""
read -p "Press Enter to continue..."
