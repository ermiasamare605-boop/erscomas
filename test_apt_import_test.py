#!/usr/bin/env python3
"""Test script to verify APTFramework impacket import"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.abspath('.'))

try:
    from modules.payloads.apt_framework import APTFramework
    print("APTFramework imported successfully")
    
    apt = APTFramework()
    print(f"Impacket available: {apt.impacket_available}")
    
    if apt.impacket_available:
        print("✓ Impacket imported successfully")
        # Test that the real impacket classes are available
        from modules.payloads.apt_framework import SMBConnection, DCERPCTransportFactory
        print("✓ SMBConnection and DCERPCTransportFactory available")
        
    else:
        print("✗ Impacket not available - using fallback")
        
except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")
    import traceback
    print("Stack trace:")
    print(traceback.format_exc())

# Print sys.path for debugging
print("\nsys.path:")
for path in sys.path:
    print(path)
