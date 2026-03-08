#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, '')

print("=== Checking apt_framework impacket imports ===")

try:
    from modules.payloads import apt_framework
    
    print(f"IMPACKET_AVAILABLE: {apt_framework.IMPACKET_AVAILABLE}")
    
    # Check if we can access the impacket imports through apt_framework
    print()
    print("Checking SMBConnection:")
    if hasattr(apt_framework, 'SMBConnection'):
        print(f"  Success: {apt_framework.SMBConnection}")
    else:
        print("  Error: SMBConnection not in apt_framework")
        
    print()
    print("Checking DCERPCTransportFactory:")
    if hasattr(apt_framework, 'DCERPCTransportFactory'):
        print(f"  Success: {apt_framework.DCERPCTransportFactory}")
    else:
        print("  Error: DCERPCTransportFactory not in apt_framework")
        
    print()
    print("Checking ntlm:")
    if hasattr(apt_framework, 'ntlm'):
        print(f"  Success: {apt_framework.ntlm}")
    else:
        print("  Error: ntlm not in apt_framework")
        
    print()
    print("Checking wkst:")
    if hasattr(apt_framework, 'wkst'):
        print(f"  Success: {apt_framework.wkst}")
    else:
        print("  Error: wkst not in apt_framework")
        
    print()
    print("Checking RPC constants:")
    if hasattr(apt_framework, 'RPC_C_AUTHN_LEVEL_PKT_PRIVACY'):
        print(f"  Success: RPC_C_AUTHN_LEVEL_PKT_PRIVACY = {apt_framework.RPC_C_AUTHN_LEVEL_PKT_PRIVACY}")
    else:
        print("  Error: RPC_C_AUTHN_LEVEL_PKT_PRIVACY not in apt_framework")
        
    if hasattr(apt_framework, 'RPC_C_AUTHN_GSS_NEGOTIATE'):
        print(f"  Success: RPC_C_AUTHN_GSS_NEGOTIATE = {apt_framework.RPC_C_AUTHN_GSS_NEGOTIATE}")
    else:
        print("  Error: RPC_C_AUTHN_GSS_NEGOTIATE not in apt_framework")
        
    # Check if the imports are actually from impacket
    print()
    print("Checking if imports are from impacket:")
    smb_impacket = "impacket" in str(apt_framework.SMBConnection).lower()
    print(f"  SMBConnection from impacket: {smb_impacket}")
    
    dce_impacket = "impacket" in str(apt_framework.DCERPCTransportFactory).lower()
    print(f"  DCERPCTransportFactory from impacket: {dce_impacket}")
    
    ntlm_impacket = "impacket" in str(apt_framework.ntlm).lower()
    print(f"  ntlm from impacket: {ntlm_impacket}")
    
    wkst_impacket = "impacket" in str(apt_framework.wkst).lower()
    print(f"  wkst from impacket: {wkst_impacket}")
    
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    print(traceback.format_exc())
