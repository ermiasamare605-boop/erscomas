#!/usr/bin/env python3
"""Test script to verify apt_framework_fixed.py import functionality"""

import sys
from pathlib import Path

# Add the current directory to the Python path
sys.path.insert(0, str(Path(__file__).parent))

try:
    from apt_framework_fixed import APTFramework, IMPACKET_AVAILABLE, DCERPCTransportFactory, SMBConnection
    
    print("✓ Successfully imported apt_framework_fixed module")
    
    # Create an instance of APTFramework
    framework = APTFramework()
    
    # Check if impacket is available
    print(f"Impacket available: {framework.check_impacket_available()}")
    print(f"Global IMPACKET_AVAILABLE: {IMPACKET_AVAILABLE}")
    
    # Test the imported classes are not mocks when impacket is available
    if IMPACKET_AVAILABLE:
        print("DCERPCTransportFactory type:", type(DCERPCTransportFactory))
        print("SMBConnection type:", type(SMBConnection))
        
        # Verify they are not the mock classes
        from apt_framework_fixed import MockTransportModule, MockSMBConnection
        assert DCERPCTransportFactory != MockTransportModule.DCERPCTransportFactory
        assert SMBConnection != MockSMBConnection
        print("✓ Imported classes are real impacket implementations")
    
    print("\n✅ All tests passed!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    print(traceback.format_exc())
