#!/usr/bin/env python3
# Verify that the apt_framework.py file contains our changes
with open('modules/payloads/apt_framework.py', 'r', encoding='utf-8') as f:
    content = f.read()

print("Checking apt_framework.py content:")
if 'logger.error("=== IMPACKET IMPORT FAILURE ===")' in content:
    print("✓ Contains the new error handling")
else:
    print("✗ Missing new error handling")
    
if 'logger.warning("Impacket library not available: %s", e)' in content:
    print("✗ Still contains old warning")
else:
    print("✓ Old warning removed")
    
if 'Please install impacket using: pip install impacket' in content:
    print("✗ Still contains old warning message")
else:
    print("✓ Old warning message removed")
    
print(f"\nLines containing 'logger.warning': {sum(1 for line in content.splitlines() if 'logger.warning' in line)}")
print("These should only be the credential dumping warning.")
