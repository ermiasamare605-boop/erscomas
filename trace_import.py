#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.abspath('.'))

# Remove any existing modules
for key in list(sys.modules.keys()):
    if key.startswith('modules') or key.startswith('impacket'):
        del sys.modules[key]

# Trace import
import traceback
import importlib
try:
    print("Current sys.path:", sys.path)
    
    with open('modules/payloads/apt_framework.py', 'rb') as f:
        print(f"\napt_framework.py exists, size: {len(f.read())} bytes")
    
    print("\nImporting apt_framework...")
    module = importlib.import_module('modules.payloads.apt_framework')
    
    print(f"\nModule imported successfully")
    print(f"Module file: {module.__file__}")
    print(f"Module dict keys: {list(module.__dict__.keys())}")
    
    print(f"\nIMPACKET_AVAILABLE: {module.IMPACKET_AVAILABLE}")
    if hasattr(module, 'SMBConnection'):
        print(f"SMBConnection: {module.SMBConnection}")
        
except Exception as e:
    print(f"\nERROR: {type(e).__name__}: {e}")
    print("\nStack trace:")
    print(''.join(traceback.format_stack()))
