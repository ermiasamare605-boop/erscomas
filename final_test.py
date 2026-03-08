#!/usr/bin/env python3
import sys
import os
import logging

sys.path.insert(0, os.path.abspath('.'))

# Enable debug logging for testing
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

try:
    logger.info("Starting apt_framework test...")
    
    from modules.payloads import apt_framework
    
    logger.info(f"Module imported successfully")
    logger.info(f"Module file: {apt_framework.__file__}")
    
    apt = apt_framework.APTFramework()
    logger.info(f"APTFramework instance created")
    logger.info(f"IMPACKET_AVAILABLE: {apt.impacket_available}")
    
    if apt.impacket_available:
        logger.info("\n✓ Impacket library available")
        
        logger.info(f"\nChecking imported objects:")
        logger.info(f"SMBConnection: {apt_framework.SMBConnection}")
        logger.info(f"DCERPCTransportFactory: {apt_framework.DCERPCTransportFactory}")
        logger.info(f"wkst module: {apt_framework.wkst}")
        logger.info(f"ntlm module: {apt_framework.ntlm}")
        logger.info(f"RPC_C_AUTHN_LEVEL_PKT_PRIVACY: {apt_framework.RPC_C_AUTHN_LEVEL_PKT_PRIVACY}")
        logger.info(f"RPC_C_AUTHN_GSS_NEGOTIATE: {apt_framework.RPC_C_AUTHN_GSS_NEGOTIATE}")
        
        logger.info(f"\n✓ All expected objects are available")
        
    else:
        logger.warning("❌ Impacket library not available")
        
    logger.info("\n=== Test completed successfully ===")
    
except Exception as e:
    logger.error(f"\n❌ Test failed: {type(e).__name__}: {e}")
    import traceback
    logger.error(f"Stack trace:\n{traceback.format_exc()}")
    sys.exit(1)
