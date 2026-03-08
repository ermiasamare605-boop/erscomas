#!/usr/bin/env python3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

try:
    from apt_framework_fixed import (
        APTFramework,
        IMPACKET_AVAILABLE,
        DCERPCTransportFactory,
        SMBConnection,
        wkst,
        ntlm,
        RPC_C_AUTHN_LEVEL_PKT_PRIVACY,
        RPC_C_AUTHN_GSS_NEGOTIATE,
        impacket
    )
    
    print("Successfully imported all symbols from apt_framework_fixed")
    
    framework = APTFramework()
    assert framework.check_impacket_available() == IMPACKET_AVAILABLE
    print("APTFramework.impacket_available matches global IMPACKET_AVAILABLE")
    
    if IMPACKET_AVAILABLE:
        print("\nTesting real impacket implementations:")
        print(f"DCERPCTransportFactory: {DCERPCTransportFactory}")
        print(f"SMBConnection: {SMBConnection}")
        print(f"wkst module: {wkst}")
        print(f"ntlm module: {ntlm}")
        print(f"RPC_C_AUTHN_LEVEL_PKT_PRIVACY: {RPC_C_AUTHN_LEVEL_PKT_PRIVACY}")
        print(f"RPC_C_AUTHN_GSS_NEGOTIATE: {RPC_C_AUTHN_GSS_NEGOTIATE}")
        
        # Verify DCERPCTransportFactory is callable
        assert callable(DCERPCTransportFactory)
        print("DCERPCTransportFactory is callable")
        
        # Verify SMBConnection is a class
        assert isinstance(SMBConnection, type)
        print("SMBConnection is a class")
        
    else:
        print("\nTesting mock implementations (impacket not available):")
        print("Mock implementations are provided")
    
    print("\nAll tests passed! apt_framework_fixed.py is working correctly.")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    print(traceback.format_exc())
