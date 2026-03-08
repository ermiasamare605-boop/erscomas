#!/usr/bin/env python3
import sys
sys.path.insert(0, 'c:/Users/ermias3706/hacking/impacket')

print("sys.path includes:", sys.path[0])

try:
    print("\n=== Attempting to import impacket.smbconnection ===")
    import impacket.smbconnection
    print("✓ impacket.smbconnection imported successfully")
    
except ImportError as e:
    print(f"✗ ImportError: {e}")
    import traceback
    print("\nStack trace:")
    print(traceback.format_exc())
    
except Exception as e:
    print(f"✗ Exception: {type(e).__name__}: {e}")
    import traceback
    print("\nStack trace:")
    print(traceback.format_exc())

try:
    print("\n=== Attempting to import impacket ===")
    import impacket
    print(f"✓ impacket imported successfully")
    print(f"  impacket.__file__: {impacket.__file__}")
    print(f"  impacket.__path__: {impacket.__path__}")
    
    print(f"\n=== Contents of impacket module ===")
    print(dir(impacket))
    
except Exception as e:
    print(f"✗ Exception: {type(e).__name__}: {e}")
    import traceback
    print("\nStack trace:")
    print(traceback.format_exc())
