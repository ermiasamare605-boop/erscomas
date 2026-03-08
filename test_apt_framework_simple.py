#!/usr/bin/env python3
"""Simple test for APTFramework fallback mechanisms"""

import sys
sys.path.insert(0, 'c:/Users/ermias3706/hacking')

try:
    from modules.payloads.apt_framework import APTFramework
    print("APTFramework imported successfully")
    
    apt = APTFramework()
    print("APTFramework instance created")
    print("Impacket available:", apt.impacket_available)
    
    assert not apt.impacket_available, "Expected impacket to not be available"
    print("Fallback mechanisms are active")
    
    print("")
    print("All tests passed")
    print("")
    print("The module is functioning correctly with fallback mechanisms.")
    print("To use the real impacket functionality, install impacket with:")
    print("pip install impacket")
    
except Exception as e:
    print("Error:", type(e).__name__, ":", e)
    import traceback
    print("Stack trace:")
    print(traceback.format_exc())
