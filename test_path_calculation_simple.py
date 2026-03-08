#!/usr/bin/env python3
"""Test script to verify path calculation in apt_framework (simple version)"""

import sys
from pathlib import Path

# Test path calculation
test_file = Path(__file__).parent / "modules" / "payloads" / "apt_framework.py"
print("Test file path:", test_file)

if test_file.exists():
    print("File exists")
else:
    print("File does NOT exist")

# Calculate impacket dir path as per apt_framework.py
impacket_dir = test_file.parent.parent.parent / "impacket"
print("\nCalculated impacket_dir:", impacket_dir)
print("Directory exists:", impacket_dir.exists())

if impacket_dir.exists():
    print("Contents:", list(impacket_dir.iterdir()))
    
    # Check if it's actually the impacket library
    init_file = impacket_dir / "__init__.py"
    print("__init__.py exists:", init_file.exists())
    
    if init_file.exists():
        with open(init_file, 'r') as f:
            print("\nimpacket/__init__.py contents (first 10 lines):")
            print(f.read(200))
else:
    print("impacket directory NOT found!")
    
print("\nimpacket in sys.path:", 'impacket' in str(sys.path))

print()
print("=== Testing direct import from calculated path ===")
sys.path.insert(0, str(impacket_dir))
try:
    from impacket import smbconnection
    print("Successfully imported smbconnection")
    # Verify module is usable by checking for key class
    if hasattr(smbconnection, 'SMBConnection'):
        print("SMBConnection class is available")
except Exception as e:
    print("Failed:", e)

try:
    from impacket.dcerpc.v5 import wkst
    print("Successfully imported wkst")
except Exception as e:
    print("Failed:", e)

try:
    from impacket.dcerpc.v5.transport import DCERPCTransportFactory
    print("Successfully imported DCERPCTransportFactory")
except Exception as e:
    print("Failed:", e)
