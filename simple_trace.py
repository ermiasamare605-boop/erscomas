#!/usr/bin/env python3
import sys
import os
import traceback
sys.path.insert(0, os.path.abspath('.'))

try:
    # Import apt_framework and capture any warnings
    import warnings
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        from modules.payloads.apt_framework import APTFramework
        
        if w:
            print(f"Warning caught: {w[-1].message}")
            print(f"Warning category: {w[-1].category}")
            print(f"Warning filename: {w[-1].filename}")
            print(f"Warning line number: {w[-1].lineno}")
            print(f"Warning source: {w[-1].source}")
    
    framework = APTFramework()
    print('Impacket available:', framework.check_impacket_available())
    
except Exception as e:
    print(f'Error: {e}')
    print(traceback.format_exc())
