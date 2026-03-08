#!/usr/bin/env python3
"""Direct test of apt_framework module with traceback"""

import sys
import os
sys.path.insert(0, os.path.abspath('.'))

try:
    from modules.payloads.apt_framework import APTFramework
    print("Import successful")
    
    framework = APTFramework()
    print(f"Impacket available: {framework.impacket_available}")
    
except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")
    import traceback
    print(traceback.format_exc())
