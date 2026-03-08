#!/usr/bin/env python3
"""Fixed APT Framework Module - Handles impacket imports correctly"""

from __future__ import annotations
import logging
import sys
from pathlib import Path
from typing import List, Dict, Any, Optional

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Define module public API
__all__ = [
    'APTFramework',
    'SMBConnection',
    'DCERPCTransportFactory',
    'impacket',
    'IMPACKET_AVAILABLE',
    'wkst',
    'ntlm',
    'RPC_C_AUTHN_LEVEL_PKT_PRIVACY',
    'RPC_C_AUTHN_GSS_NEGOTIATE',
    'dcom',
    'samr',
    'lsad'
]

# Define mock classes first (always available)
class MockSMBConnection:
    def __init__(self, *args, **kwargs):
        pass

    def login(self, *args, **kwargs):
        pass

    def logoff(self):
        pass

class MockDCERPCTransport:
    def set_credentials(self, *args, **kwargs):
        pass

    def get_dce_rpc(self):
        class MockDCE:
            def connect(self):
                pass

            def bind(self, *args, **kwargs):
                pass

            def disconnect(self):
                pass

        return MockDCE()

class MockTransport:
    class DCERPCTransportFactory:
        def __init__(self, string_binding):
            self.string_binding = string_binding

        def get_dce_rpc(self):
            return MockDCERPCTransport()

class MockWkst:
    MSRPC_UUID_WKSTA = None

    @staticmethod
    def hNetrWkstaGetInfo(*args, **kwargs):
        return {
            'ServerName': b'UNKNOWN',
            'Domain': b'WORKGROUP',
            'verMajor': 0,
            'verMinor': 0
        }

# Create mock classes for all imported modules
class MockDcom:
    pass

class MockSamr:
    pass

class MockLsad:
    pass

class MockTransportModule:
    class DCERPCTransportFactory:
        def __init__(self, string_binding):
            self.transport = MockDCERPCTransport()

        def __call__(self, string_binding):
            return self.transport

        def set_credentials(self, **kwargs):
            pass

        def get_dce_rpc(self):
            class MockDCE:
                def connect(self):
                    pass

                def bind(self, *args, **kwargs):
                    pass

                def disconnect(self):
                    pass

                def set_credentials(self, **kwargs):
                    pass

            return MockDCE()

    DCERPCTransport = MockDCERPCTransport

class MockWkstModule:
    MSRPC_UUID_WKSTA = None
    
    @staticmethod
    def hNetrWkstaGetInfo(*args, **kwargs):
        return {
            'ServerName': b'UNKNOWN',
            'Domain': b'WORKGROUP',
            'verMajor': 0,
            'verMinor': 0
        }

class MockNtlmModule:
    @staticmethod
    def compute_lmhash(x):
        return b''
    
    @staticmethod
    def compute_nthash(x):
        return b''

# Initialize default mock values
IMPACKET_AVAILABLE = False
SMBConnection = MockSMBConnection
DCERPCTransportFactory = MockTransportModule.DCERPCTransportFactory
wkst = MockWkstModule()
dcom = MockDcom()
samr = MockSamr()
lsad = MockLsad()
ntlm = MockNtlmModule()
RPC_C_AUTHN_LEVEL_PKT_PRIVACY = 0
RPC_C_AUTHN_GSS_NEGOTIATE = 0
impacket = None

# Try to import impacket modules
try:
    # Calculate impacket path - impacket module is in ./impacket/impacket
    correct_impacket_path = str(Path(__file__).parent / "impacket")
    
    # Ensure correct path for imports
    if correct_impacket_path not in sys.path:
        sys.path.insert(0, correct_impacket_path)
    
    logger.debug("sys.path: %s", sys.path)
    
    # Try to import impacket
    import impacket
    logger.debug("Imported impacket module from: %s", impacket.__file__)
    
    # Import modules one by one with IDE error suppression
    try:
        from impacket.dcerpc.v5.transport import DCERPCTransportFactory  # pyright: ignore
        from impacket.dcerpc.v5 import wkst  # pyright: ignore
        from impacket.smbconnection import SMBConnection  # pyright: ignore
        from impacket import ntlm  # pyright: ignore
        from impacket.dcerpc.v5.rpcrt import RPC_C_AUTHN_LEVEL_PKT_PRIVACY, RPC_C_AUTHN_GSS_NEGOTIATE  # pyright: ignore
        
        IMPACKET_AVAILABLE = True
        logger.debug("All impacket imports succeeded")
    except ImportError as e:
        logger.warning("Failed to import specific impacket modules: %s", e)
        logger.warning("Attempting to import from system-installed impacket")
        
        # Try system-installed impacket as fallback
        sys.path = [p for p in sys.path if p != correct_impacket_path]
        from impacket.dcerpc.v5.transport import DCERPCTransportFactory  # pyright: ignore
        from impacket.dcerpc.v5 import wkst  # pyright: ignore
        from impacket.smbconnection import SMBConnection  # pyright: ignore
        from impacket import ntlm  # pyright: ignore
        from impacket.dcerpc.v5.rpcrt import RPC_C_AUTHN_LEVEL_PKT_PRIVACY, RPC_C_AUTHN_GSS_NEGOTIATE  # pyright: ignore
        
        IMPACKET_AVAILABLE = True
        logger.debug("✓ Fallback impacket imports succeeded")
    
except Exception as e:
    logger.warning("Impacket library not available: %s", e)
    logger.warning("Please install impacket using: pip install impacket")
    import traceback
    logger.warning("Stack trace: %s", traceback.format_exc())
    
    # Create a mock impacket module
    class MockImpacket:
        class dcerpc:
            class v5:
                transport = MockTransportModule
                wkst = MockWkstModule
                rpcrt = type('MockRPCRT', (), {
                    'RPC_C_AUTHN_LEVEL_PKT_PRIVACY': 0,
                    'RPC_C_AUTHN_GSS_NEGOTIATE': 0
                })
        smbconnection = type('MockSMBConnectionModule', (), {'SMBConnection': MockSMBConnection})
        ntlm = MockNtlmModule
    
    impacket = MockImpacket()


class APTFramework:
    """
    Class to handle APT-style payload operations using Impacket
    """

    def __init__(self):
        self.impacket_available = IMPACKET_AVAILABLE
        self.smb_connection = None
        self.rpc_transport = None
        # Expose impacket modules as instance attributes for convenience
        self.wkst = wkst
        self.ntlm = ntlm
        self.dcom = dcom
        self.samr = samr
        self.lsad = lsad
        self.impacket = impacket
        self.SMBConnection = SMBConnection
        self.DCERPCTransportFactory = DCERPCTransportFactory
        self.RPC_C_AUTHN_LEVEL_PKT_PRIVACY = RPC_C_AUTHN_LEVEL_PKT_PRIVACY
        self.RPC_C_AUTHN_GSS_NEGOTIATE = RPC_C_AUTHN_GSS_NEGOTIATE

    def check_impacket_available(self) -> bool:
        return self.impacket_available

if __name__ == "__main__":
    framework = APTFramework()
    print(f"Impacket available: {framework.check_impacket_available()}")
