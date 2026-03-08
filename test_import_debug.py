#!/usr/bin/env python3
"""Test script to debug impacket import issues"""

import sys
from pathlib import Path

# Debug current directory structure
print("Current working directory:", Path.cwd())
print("Script directory:", Path(__file__).parent)

# Check impacket directory
project_root = Path(__file__).parent
impacket_dir = project_root / "impacket"
print(f"\nImpacket directory: {impacket_dir}")
print(f"Impacket directory exists: {impacket_dir.exists()}")
if impacket_dir.exists():
    print(f"Impacket directory contents: {list(impacket_dir.iterdir())}")
    impacket_module_dir = impacket_dir / "impacket"
    print(f"\nImpacket module directory: {impacket_module_dir}")
    print(f"Impacket module directory exists: {impacket_module_dir.exists()}")
    if impacket_module_dir.exists():
        print(f"Impacket module directory contents: {list(impacket_module_dir.iterdir())}")
        dcerpc_dir = impacket_module_dir / "dcerpc" / "v5"
        print(f"\nDCERPC v5 directory: {dcerpc_dir}")
        print(f"DCERPC v5 directory exists: {dcerpc_dir.exists()}")
        if dcerpc_dir.exists():
            print(f"DCERPC v5 directory contents: {list(dcerpc_dir.iterdir())}")

# Try to import
print("\n--- Attempting impacket import ---")
try:
    sys.path.insert(0, str(impacket_dir))
    print(f"sys.path[0]: {sys.path[0]}")
    
    # Try different import styles
    print("\n1. Importing from impacket.dcerpc.v5.transport directly:")
    try:
        from impacket.dcerpc.v5.transport import DCERPCTransportFactory
        print("SUCCESS: DCERPCTransportFactory imported directly")
        print(f"Type: {type(DCERPCTransportFactory)}")
    except Exception as e:
        print(f"ERROR: {type(e).__name__}: {e}")
        import traceback
        print(traceback.format_exc())
    
    print("\n2. Importing transport module first:")
    try:
        from impacket.dcerpc.v5 import transport
        print("SUCCESS: transport module imported")
        print(f"Module contents: {dir(transport)}")
        if hasattr(transport, 'DCERPCTransportFactory'):
            print("DCERPCTransportFactory found in transport module")
            print(f"Type: {type(transport.DCERPCTransportFactory)}")
    except Exception as e:
        print(f"ERROR: {type(e).__name__}: {e}")
        import traceback
        print(traceback.format_exc())

except Exception as e:
    print(f"CRITICAL ERROR: {e}")
    import traceback
    print(traceback.format_exc())
