@echo off
echo Starting Chrome with remote debugging enabled...
echo.
echo This will:
echo 1. Close any existing Chrome windows
echo 2. Start Chrome with remote debugging on port 9222
echo 3. Use a separate user data directory to avoid conflicts
echo.
echo After Chrome opens:
echo 1. Navigate to your Google Form
echo 2. Sign in to your Google account
echo 3. Make sure you can see the form fields
echo 4. Come back to the terminal and run: python robust_automation.py
echo.

REM Kill any existing Chrome processes
taskkill /f /im chrome.exe 2>nul
timeout /t 2 /nobreak >nul

REM Start Chrome with remote debugging
start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir=C:\temp\chrome_debug

echo.
echo Chrome should now be running with remote debugging enabled.
echo You can now run the automation script.
echo.
pause
