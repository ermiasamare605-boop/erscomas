#!/usr/bin/env python3
"""Test script to verify path calculation in apt_framework"""

import sys
from pathlib import Path

# Test path calculation
test_file = Path(__file__).parent / "modules" / "payloads" / "apt_framework.py"
print(f"Test file path: {test_file}")

if test_file.exists():
    print("✓ File exists")
else:
    print("✗ File does NOT exist")

# Calculate impacket dir path as per apt_framework.py
impacket_dir = test_file.parent.parent.parent / "impacket"
print(f"\nCalculated impacket_dir: {impacket_dir}")
print(f"Directory exists: {impacket_dir.exists()}")

if impacket_dir.exists():
    print(f"Contents: {list(impacket_dir.iterdir())}")
    
    # Check if it's actually the impacket library
    init_file = impacket_dir / "__init__.py"
    print(f"__init__.py exists: {init_file.exists()}")
    
    if init_file.exists():
        with open(init_file, 'r') as f:
            print(f"\nimpacket/__init__.py contents (first 10 lines):")
            print(f.read(200))
else:
    print("impacket directory NOT found!")
    
print(f"\nimpacket in sys.path: {'impacket' in str(sys.path)}")

print()
print("=== Testing direct import from calculated path ===")
sys.path.insert(0, str(impacket_dir))
try:
    from impacket import smbconnection
    print("✓ Successfully imported smbconnection")
except Exception as e:
    print(f"✗ Failed: {e}")

try:
    from impacket.dcerpc.v5 import wkst
    print("✓ Successfully imported wkst")
except Exception as e:
    print(f"✗ Failed: {e}")

try:
    from impacket.dcerpc.v5.transport import DCERPCTransportFactory
    print("✓ Successfully imported DCERPCTransportFactory")
except Exception as e:
    print(f"✗ Failed: {e}")
