# Linux Preparation Summary

This document outlines the steps taken to prepare the social media pentest tool for running on Linux and uploading to GitHub.

## Key Changes

1. **Created .gitignore File**: Added a comprehensive .gitignore file to exclude:
   - Python bytecode and cache files
   - Virtual environments
   - IDE settings and temporary files
   - Logs and output files
   - Configuration and environment variables
   - Database and data files

2. **Checked Shell Scripts**: Verified that shell scripts have appropriate shebang lines:
   - `full_attack.sh` - has `#!/bin/bash`
   - `instagram_rce_exploit.sh` - has `#!/bin/bash`

3. **Verified Dependencies**: Checked requirements.txt for Linux-compatible packages.

4. **Project Structure**: Confirmed the project structure is appropriate for GitHub:
   - All Python files have shebang lines
   - No hardcoded absolute paths in main project files
   - Configuration is read from relative paths

## Running on Linux

### Prerequisites
- Python 3.8+
- pip3
- git (for GitHub)

### Installation
1. Clone the repository from GitHub
2. Install dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```
3. Install Playwright browsers (if needed):
   ```bash
   playwright install chromium firefox webkit
   ```
4. Make sure shell scripts are executable:
   ```bash
   chmod +x full_attack.sh instagram_rce_exploit.sh
   ```

### Usage
- Run the main tool: `python3 social_hacker.py`
- Run shell scripts: `./full_attack.sh <target> <platform>`

## Notes

- The project includes the `impacket` library which is primarily used for Windows protocol interactions, but it should work fine on Linux.
- No major Windows-specific code was found in the main project files.
- All paths in the codebase are relative and should work on Linux systems.