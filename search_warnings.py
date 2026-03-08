#!/usr/bin/env python3
with open('modules/payloads/apt_framework.py', 'r', encoding='utf-8') as f:
    content = f.read()
    
print("Looking for logger.warning calls in apt_framework.py:")
for i, line in enumerate(content.splitlines(), 1):
    if 'logger.warning' in line:
        print(f"Line {i}: {line.strip()}")
        
print("\n---\nLooking for any warning calls:")
for i, line in enumerate(content.splitlines(), 1):
    if 'warning' in line.lower():
        print(f"Line {i}: {line.strip()}")
