#!/usr/bin/env python3
"""Test script to verify smbconnection import"""

import sys
from pathlib import Path

# Calculate impacket dir path
impacket_dir = Path(__file__).parent / "impacket"
print("Impacket directory:", impacket_dir)
print("Directory exists:", impacket_dir.exists())

sys.path.insert(0, str(impacket_dir))

print("\n=== Testing smbconnection import ===")
try:
    from impacket import smbconnection
    print("Successfully imported smbconnection")
    print("Module type:", type(smbconnection))
    print("Module attributes:", dir(smbconnection))
except Exception as e:
    print(f"Failed to import smbconnection: {e}")
    import traceback
    print("\nStack trace:")
    print(traceback.format_exc())

print("\n=== Testing direct import from file ===")
try:
    import impacket.smbconnection
    print("Successfully imported impacket.smbconnection")
    print("Module type:", type(impacket.smbconnection))
    print("Module attributes:", dir(impacket.smbconnection))
except Exception as e:
    print(f"Failed to import impacket.smbconnection: {e}")
    import traceback
    print("\nStack trace:")
    print(traceback.format_exc())
