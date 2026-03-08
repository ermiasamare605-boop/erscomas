#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.abspath('.'))

import sys
import traceback

# Capture all warnings and exceptions
sys.__excepthook__ = lambda type, value, tb: print(
    f"Unhandled exception:\n{type.__name__}: {value}\n"
    f"Stack trace:\n{''.join(traceback.format_stack())}"
)

# Override warning module to track warnings
import warnings
warnings.showwarning = lambda message, category, filename, lineno, file=None, line=None: print(
    f"Warning at {filename}:{lineno}: {category.__name__}: {message}"
)

try:
    from modules.payloads import apt_framework
    apt = apt_framework.APTFramework()
    print(f"APTFramework.impacket_available: {apt.impacket_available}")
    
    print(f"\nsys.path: {sys.path}")
    
    if apt.impacket_available:
        print(f"\nSMBConnection type: {type(apt_framework.SMBConnection)}")
        print(f"DCERPCTransportFactory type: {type(apt_framework.DCERPCTransportFactory)}")
        print(f"wkst type: {type(apt_framework.wkst)}")
        print(f"ntlm type: {type(apt_framework.ntlm)}")
        print(f"RPC constants available: {hasattr(apt_framework, 'RPC_C_AUTHN_LEVEL_PKT_PRIVACY')}")
        
    import impacket
    print(f"\nTop-level impacket module imported: {impacket}")
    print(f"impacket.__file__: {impacket.__file__}")
    
except Exception as e:
    print(f"ERROR: {type(e).__name__}: {e}")
    print(f"Stack trace:\n{''.join(traceback.format_stack())}")
    print()
    import traceback
    print(traceback.format_exc())
