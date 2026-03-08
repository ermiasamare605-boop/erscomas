#!/usr/bin/env python3
from pathlib import Path
import sys

apt_framework_path = Path("modules/payloads/apt_framework.py").resolve()
print("apt_framework.py path:", apt_framework_path)

correct_impacket_path = str(apt_framework_path.parent.parent.parent / "impacket")
print("Calculated impacket path:", correct_impacket_path)

print("\nsys.path before any changes:", sys.path)

# Remove any existing impacket-related paths from sys.path and remove the
# current directory (empty string) path to avoid namespace module issues
# caused by finding the impacket directory via both the explicit path and the
# current directory.

# Remove existing impacket-related paths
for i in reversed(range(len(sys.path))):
    path = sys.path[i]
    if path and "impacket" in path:
        del sys.path[i]

# Remove current directory path if present
if '' in sys.path:
    sys.path.remove('')

# Add the correct path
sys.path.insert(0, correct_impacket_path)

print("\nsys.path after modification:", sys.path)

print("\nChecking if impacket module exists at calculated path:")
import os
test_path = os.path.join(correct_impacket_path, "impacket")
print(f"impacket directory exists: {os.path.isdir(test_path)}")

if os.path.isdir(test_path):
    print(f"\nContents of {test_path}:")
    for item in os.listdir(test_path):
        item_path = os.path.join(test_path, item)
        if os.path.isdir(item_path) or item.endswith('.py'):
            print(f"  {item}")
            
print("\nChecking for smbconnection module:")
smbconnection_path = os.path.join(test_path, "smbconnection.py")
print(f"smbconnection.py exists: {os.path.exists(smbconnection_path)}")
if os.path.exists(smbconnection_path):
    print(f"File size: {os.path.getsize(smbconnection_path)} bytes")
