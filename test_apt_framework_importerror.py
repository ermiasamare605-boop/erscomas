#!/usr/bin/env python3
import sys
import os
import logging

# Set logging to debug level
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

sys.path.insert(0, os.path.abspath('.'))

# Test importing smbconnection directly
try:
    sys.path.insert(0, 'c:/Users/ermias3706/hacking/impacket')
    from impacket.smbconnection import SMBConnection
    print("✓ from impacket.smbconnection import SMBConnection")
except Exception as e:
    print(f"✗ from impacket.smbconnection import SMBConnection: {e}")
    import traceback
    print(traceback.format_exc())

# Test importing from apt_framework
try:
    from modules.payloads import apt_framework
    print("\n✓ apt_framework imported successfully")
    
    # Check what's in the apt_framework module
    print("apt_framework contains:")
    for item in dir(apt_framework):
        if not item.startswith('__'):
            print(f"  - {item}")
            
    apt = apt_framework.APTFramework()
    print(f"\nAPTFramework instance created")
    print(f"Impacket available: {apt.impacket_available}")
    
except Exception as e:
    print(f"\n✗ apt_framework import failed: {e}")
    import traceback
    print(traceback.format_exc())

# Print sys.path
print("\nsys.path:")
for i, path in enumerate(sys.path):
    print(f"{i:2d}: {repr(path)}")
