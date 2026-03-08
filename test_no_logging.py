#!/usr/bin/env python3
import sys
import os
import importlib

sys.path.insert(0, os.path.abspath('.'))

try:
    # Clear module cache
    for key in list(sys.modules.keys()):
        if key.startswith('modules') or key.startswith('impacket'):
            del sys.modules[key]
            
    # Import the module
    from modules.payloads.apt_framework import APTFramework
    
    framework = APTFramework()
    print('Impacket available:', framework.check_impacket_available())
    
    if framework.check_impacket_available():
        print('All imports succeeded')
        
except Exception as e:
    print(f'Error: {type(e).__name__}: {e}')
    import traceback
    print(traceback.format_exc())
