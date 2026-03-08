#!/usr/bin/env python3
import sys
sys.path.insert(0, 'c:/Users/ermias3706/hacking/impacket')

print("sys.path includes:", sys.path[0])

try:
    print("\n=== Attempting to import impacket.smbconnection ===")
    import impacket.smbconnection
    print("Success: impacket.smbconnection imported")
    
except ImportError as e:
    print("Error: ImportError:", e)
    import traceback
    print("\nStack trace:")
    print(traceback.format_exc())
    
except Exception as e:
    print("Error: Exception", type(e).__name__, ":", e)
    import traceback
    print("\nStack trace:")
    print(traceback.format_exc())

try:
    print("\n=== Attempting to import impacket ===")
    import impacket
    print("Success: impacket imported")
    print("impacket.__file__:", impacket.__file__)
    print("impacket.__path__:", impacket.__path__)
    
    print("\nContents of impacket module:")
    print(dir(impacket))
    
except Exception as e:
    print("Error: Exception", type(e).__name__, ":", e)
    import traceback
    print("\nStack trace:")
    print(traceback.format_exc())
