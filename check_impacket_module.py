#!/usr/bin/env python3
import sys
import os

sys.path.insert(0, '')
from modules.payloads import apt_framework

print("=== apt_framework.impacket === ")
print("Type:", type(apt_framework.impacket))
print("Value:", apt_framework.impacket)

if hasattr(apt_framework.impacket, '__dict__'):
    print("\nAttributes:", list(apt_framework.impacket.__dict__.keys()))

if hasattr(apt_framework.impacket, '__path__'):
    print("\n__path__:", apt_framework.impacket.__path__)

# Check if dcerpc exists in apt_framework.impacket
print("\n=== Checking for dcerpc in impacket module ===")
try:
    import impacket
    print("top-level impacket module")
    print("impacket.__file__:", impacket.__file__)
    
    try:
        from impacket import dcerpc
        print("dcerpc imported successfully")
        print("dcerpc:", type(dcerpc))
        if hasattr(dcerpc, '__path__'):
            print("dcerpc.__path__:", dcerpc.__path__)
            
        # Check what's in dcerpc
        if hasattr(dcerpc, '__dict__'):
            print("dcerpc contents:", list(dcerpc.__dict__.keys()))
            
        # Try importing transport
        try:
            from impacket.dcerpc.v5 import transport
            print("transport imported successfully")
            print("transport contents:", [x for x in dir(transport) if not x.startswith('__')])
        except Exception as e:
            print(f"Error importing transport: {e}")
            import traceback
            print(traceback.format_exc())
            
    except Exception as e:
        print(f"Error importing dcerpc: {e}")
        import traceback
        print(traceback.format_exc())
        
except Exception as e:
    print(f"Error importing top-level impacket: {e}")
    import traceback
    print(traceback.format_exc())
