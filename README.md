# Social Media Penetration Testing Tool

A comprehensive ethical hacking framework for social media platforms, designed for penetration testing and security assessment purposes.

## Features

### Core Modules

1. **Reconnaissance** - Gather information from social media profiles and platforms
2. **Credential Harvesting** - Test login forms and capture credentials
3. **Session Hijacking** - Steal and hijack active sessions
4. **Exploitation** - Scan and exploit vulnerabilities (XSS, SQLi, CSRF, etc.)
5. **Mass Vulnerability Checker** - Bulk scan multiple targets for vulnerabilities
6. **Persistence** - Maintain access through backdoors and scheduled tasks

### Supported Platforms

- Facebook
- Twitter
- Instagram
- LinkedIn

## Installation

### Prerequisites

- Python 3.8+
- pip3 (Python package installer)

### Step 1: Install Dependencies

```bash
pip3 install -r requirements.txt
```

### Step 2: Install Playwright Browsers

```bash
playwright install chromium firefox webkit
```

## Usage

### Interactive Mode

Run the main application for interactive mode:

```bash
python social_hacker.py
```

### Command-Line Mode

#### Reconnaissance Mode

```bash
python social_hacker.py -r username -o results.json
```

#### Credential Testing

```bash
python social_hacker.py -t https://example.com/login -u user -p pass -o results.json
```

#### Target Analysis

```bash
python social_hacker.py -t https://example.com -o results.json
```

### Module-Specific Usage

#### Reconnaissance Module

```bash
python modules/recon.py username -o recon_results.json
```

#### Credential Harvesting

```bash
python modules/cred_harvest.py https://example.com/login -u user -p pass -o credentials.txt
```

#### Exploitation Module

```bash
python modules/exploit.py https://example.com -x -s -c -o vulnerabilities.json
```

#### Mass Vulnerability Checker

```bash
python modules/payloads/mass_checker.py targets.txt -o scan_report.json
```

## Configuration

The tool uses `modules/modules/config.json` for configuration. Key settings:

- `general` - General tool configuration (logging, timeout, etc.)
- `reconnaissance` - Social media API credentials and settings
- `credential_harvesting` - Phishing and brute-force settings
- `exploitation` - Vulnerability scanning and exploitation settings
- `persistence` - Backdoor and monitoring configurations
- `payloads` - Default payloads for attacks

## Project Structure

```
social_media_pentest/
├── social_hacker.py          # Main application entry point
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
└── modules/                  # Core functionality modules
    ├── recon.py              # Reconnaissance module
    ├── cred_harvest.py       # Credential harvesting module
    ├── exploit.py            # Exploitation module
    ├── modules/              # Additional modules
    │   ├── session_hijack.py # Session hijacking module
    │   └── config.json       # Configuration file
    └── payloads/             # Attack payloads
        ├── js_inject.js      # JavaScript injection payload
        └── payloads/         # Additional payloads
            ├── capture.php   # Credential capture script
            └── payloads/     # More payload directories
                └── persistence.py     # Persistence module
                └── mass_checker.py    # Mass vulnerability checker
```

## Ethical Use Only

This tool is provided for educational purposes only. Unauthorized use against systems you don't own or have explicit permission to test is illegal and unethical.

## Disclaimer

The creators of this tool are not responsible for any misuse or damage caused by this software. Always obtain proper authorization before conducting any penetration testing activities.
