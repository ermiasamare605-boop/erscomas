#!/usr/bin/env python3
"""Test script to verify impacket imports (simple version without Unicode)"""

import sys
from pathlib import Path

# Add local impacket directory to path
impacket_dir = Path(__file__).parent / "impacket"
if impacket_dir.exists():
    sys.path.insert(0, str(impacket_dir))

print("Python version:", sys.version)
print("sys.path:", sys.path)

try:
    print("\nTesting impacket.smbconnection import:")
    from impacket.smbconnection import SMBConnection
    print("Success: SMBConnection imported")
except Exception as e:
    print("Failed:", e)

try:
    print("\nTesting impacket.dcerpc.v5.transport import:")
    from impacket.dcerpc.v5.transport import DCERPCTransportFactory
    print("Success: DCERPCTransportFactory imported")
except Exception as e:
    print("Failed:", e)

try:
    print("\nTesting impacket.dcerpc.v5.wkst import:")
    import impacket.dcerpc.v5.wkst
    print("Success: wkst module imported")
except Exception as e:
    print("Failed:", e)

try:
    print("\nTesting impacket.dcerpc.v5.rpcrt import:")
    from impacket.dcerpc.v5.rpcrt import RPC_C_AUTHN_LEVEL_PKT_PRIVACY, RPC_C_AUTHN_GSS_NEGOTIATE
    print("Success: RPC constants imported")
except Exception as e:
    print("Failed:", e)

try:
    print("\nTesting impacket.ntlm import:")
    from impacket import ntlm
    print("Success: ntlm imported")
except Exception as e:
    print("Failed:", e)

print("\n" + "="*50 + "\n")
print("Note: Pylance errors in VSCode might be due to Python environment configuration")
print("rather than actual code issues. The imports might work fine when running.")
