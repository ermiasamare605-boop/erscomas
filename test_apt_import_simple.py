#!/usr/bin/env python3
"""Simple test to check if apt_framework can import impacket"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.abspath('.'))

try:
    # Import apt_framework
    from modules.payloads import apt_framework
    
    # Check if impacket path was added
    print("=== sys.path ===")
    for path in sys.path:
        if "impacket" in path:
            print(path)
    
    # Create instance and check impacket availability
    apt = apt_framework.APTFramework()
    print(f"\nImpacket available: {apt.impacket_available}")
    
except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")
    import traceback
    print("Stack trace:")
    print(traceback.format_exc())
