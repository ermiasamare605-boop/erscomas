#!/usr/bin/env python3
import sys
import os
import subprocess

print("=== Running apt_framework import step by step ===")
print()

# Check Python version and paths
print("Python executable:", sys.executable)
print("Python version:", sys.version)
print()

# Test if test_import_impacket_from_apt_dir works
print("=== Testing test_import_impacket_from_apt_dir ===")
try:
    result = subprocess.run([
        sys.executable, 'test_import_impacket_from_apt_dir.py'
    ], capture_output=True, text=True)
    print("STDOUT:")
    print(result.stdout)
    if result.stderr:
        print("STDERR:")
        print(result.stderr)
    print("Return code:", result.returncode)
    print()
except Exception as e:
    print(f"Error running test: {e}")
    print()

# Check what's in modules/payloads
print("=== modules/payloads contents ===")
try:
    for item in os.listdir('modules/payloads'):
        print(f"  {item}")
    print()
except Exception as e:
    print(f"Error: {e}")
    print()

# Check what's in impacket directory
print("=== impacket directory structure ===")
try:
    from pathlib import Path
    for item in Path('impacket').rglob('*.py'):
        rel_item = item.relative_to('impacket')
        if 'dcerpc' in str(rel_item) or 'smbconnection' in str(rel_item):
            print(f"  {rel_item}")
    print()
except Exception as e:
    print(f"Error: {e}")
    print()

# Now try importing apt_framework
print("=== Importing apt_framework ===")
try:
    sys.path.insert(0, '')
    from modules.payloads import apt_framework
    
    print("apt_framework imported successfully")
    
    apt = apt_framework.APTFramework()
    print(f"APTFramework instance created")
    print(f"Impacket available: {apt.impacket_available}")
    
    # Check what's available in apt_framework
    print()
    print("apt_framework module contents:")
    for attr in dir(apt_framework):
        if not attr.startswith('__'):
            print(f"  {attr}")
            
except Exception as e:
    print(f"Error importing apt_framework: {type(e).__name__}: {e}")
    import traceback
    print()
    print("Stack trace:")
    print(traceback.format_exc())
