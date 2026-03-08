#!/usr/bin/env python3
"""Test script to debug path calculation in apt_framework.py"""

import sys
from pathlib import Path
import os

print("=== Current Directory ===")
print(f"cwd: {os.getcwd()}")
print()

print("=== Testing Path Calculation ===")
apt_framework_path = Path(__file__).parent / "modules" / "payloads" / "apt_framework.py"
print(f"apt_framework.py: {apt_framework_path}")

# Calculate directories
apt_framework_dir = apt_framework_path.parent
print(f"apt_framework_dir: {apt_framework_dir}")

parent_dir1 = apt_framework_dir.parent
print(f"parent_dir1: {parent_dir1}")

parent_dir2 = parent_dir1.parent
print(f"parent_dir2: {parent_dir2}")

parent_dir3 = parent_dir2.parent
print(f"parent_dir3: {parent_dir3}")

print()
print("=== Calculating impacket path ===")
impacket_dir1 = apt_framework_dir.parent.parent / "impacket"
print(f"apt_framework_dir.parent.parent/impacket: {impacket_dir1}")
print(f"Exists: {impacket_dir1.exists()}")

impacket_dir2 = Path(__file__).parent / "impacket"
print(f"Path(__file__).parent/impacket: {impacket_dir2}")
print(f"Exists: {impacket_dir2.exists()}")

impacket_dir3 = Path.cwd() / "impacket"
print(f"cwd/impacket: {impacket_dir3}")
print(f"Exists: {impacket_dir3.exists()}")

print()
print("=== Checking impacket directory contents ===")
if impacket_dir2.exists():
    try:
        for item in impacket_dir2.iterdir():
            if item.is_file() and item.name.endswith('.py'):
                print(f"  File: {item.name}")
            elif item.is_dir():
                print(f"  Dir: {item.name}")
    except Exception as e:
        print(f"Error reading impacket directory: {e}")
