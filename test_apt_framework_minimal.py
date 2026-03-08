#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.abspath('.'))

try:
    from modules.payloads import apt_framework
    print("apt_framework imported successfully")
    
    apt = apt_framework.APTFramework()
    print(f"Impacket available: {apt.impacket_available}")
    
except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")
    import traceback
    print(traceback.format_exc())
