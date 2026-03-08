@echo off
echo Deploying Social C2 Full Stack...

echo 1. Setting executable permissions...
chmod +x *.py 2>nul || echo Warning: chmod not available on Windows

echo 2. Building Docker image...
docker build -t social_c2 .
if %errorlevel% neq 0 (
    echo Error: Docker build failed
    pause
    exit /b %errorlevel%
)

echo 3. Stopping any existing containers...
docker stop social_c2 2>nul || echo No existing container to stop
docker rm social_c2 2>nul || echo No existing container to remove

echo 4. Running new container...
docker run -d -p 5000:5000 -p 8000:8000 -p 3000:3000 -v "%cd%":/app --name social_c2 social_c2
if %errorlevel% neq 0 (
    echo Error: Docker run failed
    pause
    exit /b %errorlevel%
)

echo 5. Launching auto-pentest campaign...
start /B python auto_pentest.py

echo.
echo Full stack deployed successfully!
echo.
echo Services running:
echo - C2 Server: http://localhost:5000
echo - Phishing Server: http://localhost:8000
echo - Dashboard: http://localhost:3000
echo.
echo Press any key to exit...
pause >nul
