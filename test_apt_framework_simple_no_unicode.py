#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, '')

print("=== Simple test for apt_framework ===")

try:
    from modules.payloads import apt_framework
    print("SUCCESS: apt_framework imported")
    
    apt = apt_framework.APTFramework()
    print(f"IMPACKET AVAILABLE: {apt.impacket_available}")
    
    # Test if we can access SMBConnection and DCERPCTransportFactory
    if hasattr(apt_framework, 'SMBConnection'):
        print("SUCCESS: SMBConnection in apt_framework")
        
    if hasattr(apt_framework, 'DCERPCTransportFactory'):
        print("SUCCESS: DCERPCTransportFactory in apt_framework")
        
    if apt.impacket_available:
        print("SUCCESS: Impacket imports are working")
        
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    print(traceback.format_exc())
