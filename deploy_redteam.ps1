<#
.SYNOPSIS
Red Team Deployment Script for Windows
.DESCRIPTION
Sets up and launches the Red Team deployment system
#>

# Create directories if they don't exist
$directories = "calls", "tracks", "templates", "payloads"
foreach ($dir in $directories) {
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force
        Write-Host "Created directory: $dir"
    }
}

# Install Python dependencies
Write-Host "Installing Python dependencies..."
pip install -r requirements.txt

# Get Twilio credentials
$env:TWILIO_SID = Read-Host "Enter Twilio SID"
$env:TWILIO_TOKEN = Read-Host "Enter Twilio Token"
$env:TWILIO_PHONE = Read-Host "Enter Twilio Phone Number"

# Launch the Red Team system
Write-Host "Launching Red Team system..."
Set-Location -Path "templates"
python redteam_launch.py

Write-Host "RED TEAM ACTIVE - Monitor localhost:3000"
