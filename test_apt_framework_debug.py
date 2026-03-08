#!/usr/bin/env python3
import sys
import os
import logging

# Add current directory to path
sys.path.insert(0, os.path.abspath('.'))

# Set logging to debug level
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    from modules.payloads import apt_framework
    
    print("\n=== Module imported ===")
    
    apt = apt_framework.APTFramework()
    print(f"\nImpacket available: {apt.impacket_available}")
    
except Exception as e:
    print(f"\nError: {type(e).__name__}: {e}")
    import traceback
    print("\nStack trace:")
    print(traceback.format_exc())
