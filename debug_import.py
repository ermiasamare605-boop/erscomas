#!/usr/bin/env python3
"""Debug script to isolate the impacket import issue"""

import sys
from pathlib import Path

# Test paths
correct_impacket_path = str(Path(__file__).parent / "impacket")
print("Expected impacket path:", correct_impacket_path)

# Clear any existing paths
for i in reversed(range(len(sys.path))):
    path = sys.path[i]
    if path and "impacket" in path:
        del sys.path[i]
if '' in sys.path:
    sys.path.remove('')

# Add our path
sys.path.insert(0, correct_impacket_path)
print("sys.path after inserting path:", sys.path)

# Check if we can find impacket
try:
    import impacket
    print("✓ Imported impacket module")
    print("impacket.__file__:", impacket.__file__)
    
    # Try to import specific modules
    print("\nTesting module imports:")
    
    try:
        from impacket.dcerpc.v5.transport import DCERPCTransportFactory
        print("✓ Imported DCERPCTransportFactory")
    except Exception as e:
        print(f"✗ Failed to import DCERPCTransportFactory: {e}")
        
    try:
        from impacket.dcerpc.v5 import wkst
        print("✓ Imported wkst")
        print("wkst module file:", wkst.__file__)
    except Exception as e:
        print(f"✗ Failed to import wkst: {e}")
        
    try:
        from impacket.smbconnection import SMBConnection
        print("✓ Imported SMBConnection")
    except Exception as e:
        print(f"✗ Failed to import SMBConnection: {e}")
        
    try:
        from impacket import ntlm
        print("✓ Imported ntlm")
    except Exception as e:
        print(f"✗ Failed to import ntlm: {e}")
        
except Exception as e:
    print(f"✗ Failed to import impacket: {e}")
    import traceback
    print(traceback.format_exc())
