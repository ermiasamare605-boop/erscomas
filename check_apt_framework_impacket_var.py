#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, '')
from modules.payloads import apt_framework

print("apt_framework.impacket type:", type(apt_framework.impacket))
print("apt_framework.impacket value:", apt_framework.impacket)

import inspect
# Get the source code that defines the apt_framework.impacket variable
src_lines, start_line = inspect.getsourcelines(apt_framework)
for i, line in enumerate(src_lines):
    if 'impacket' in line and '=' in line:
        print(f"\nLine {start_line + i}: {line.strip()}")
