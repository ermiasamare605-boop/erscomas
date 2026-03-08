#!/usr/bin/env python3
"""Test script to directly import from impacket's dcerpc module"""

import sys
import os

# Add the impacket library directory to path
sys.path.insert(0, os.path.abspath('c:/Users/ermias3706/hacking/impacket/impacket'))

print("=== Testing direct impacket imports ===")
print(f"sys.path[0]: {sys.path[0]}")
print()

try:
    print("Testing import from impacket.smbconnection:")
    from impacket.smbconnection import SMBConnection
    print("✓ Success - SMBConnection imported")
except Exception as e:
    print(f"✗ Failed: {e}")

try:
    print("\nTesting import from impacket.dcerpc.v5:")
    from impacket.dcerpc.v5 import wkst
    print("✓ Success - wkst module imported")
except Exception as e:
    print(f"✗ Failed: {e}")

try:
    print("\nTesting import from impacket.dcerpc.v5.transport:")
    from impacket.dcerpc.v5.transport import DCERPCTransportFactory
    print("✓ Success - DCERPCTransportFactory imported")
except Exception as e:
    print(f"✗ Failed: {e}")

try:
    print("\nTesting import from impacket.dcerpc.v5.rpcrt:")
    from impacket.dcerpc.v5.rpcrt import RPC_C_AUTHN_LEVEL_PKT_PRIVACY, RPC_C_AUTHN_GSS_NEGOTIATE
    print("✓ Success - RPC constants imported")
    print(f"  RPC_C_AUTHN_LEVEL_PKT_PRIVACY: {RPC_C_AUTHN_LEVEL_PKT_PRIVACY}")
    print(f"  RPC_C_AUTHN_GSS_NEGOTIATE: {RPC_C_AUTHN_GSS_NEGOTIATE}")
except Exception as e:
    print(f"✗ Failed: {e}")

try:
    print("\nTesting import from impacket.ntlm:")
    from impacket import ntlm
    print("✓ Success - ntlm imported")
    print(f"  Module: {ntlm}")
except Exception as e:
    print(f"✗ Failed: {e}")
