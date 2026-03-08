#!/usr/bin/env python3
from pathlib import Path

script_path = Path(__file__).resolve()
print("Script path:", script_path)

apt_framework_path = Path("modules/payloads/apt_framework.py").resolve()
print("apt_framework.py path:", apt_framework_path)

# Current calculation in apt_framework.py
current_calculation = str(apt_framework_path.parent.parent.parent / "impacket")
print("Current impacket path calculation:", current_calculation)

# Correct calculation - go up to hacking directory
correct_calculation = str(apt_framework_path.parent.parent.parent / "impacket")
print("Parent directories:")
print(f"  Level 1 (parent): {apt_framework_path.parent}")
print(f"  Level 2 (grandparent): {apt_framework_path.parent.parent}")
print(f"  Level 3 (great-grandparent): {apt_framework_path.parent.parent.parent}")

# Check if the calculated path exists
import os
print(f"\nCurrent path exists: {os.path.exists(current_calculation)}")
print(f"Current path is dir: {os.path.isdir(current_calculation)}")

# Check what's at the calculated path
if os.path.exists(current_calculation):
    print("\nContents of current calculation path:")
    print(os.listdir(current_calculation))
