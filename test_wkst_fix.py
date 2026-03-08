#!/usr/bin/env python3
"""Test script to verify the APTFramework.wkst attribute fix"""

import logging
from modules.payloads.apt_framework import APTFramework

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def test_wkst_attribute():
    """Test if APTFramework instance has wkst attribute"""
    logger.info("Creating APTFramework instance...")
    framework = APTFramework()
    
    logger.info("Checking if APTFramework has wkst attribute...")
    if hasattr(framework, 'wkst'):
        logger.info("✓ Success: APTFramework has wkst attribute")
        logger.debug(f"wkst type: {type(framework.wkst)}")
        logger.debug(f"wkst value: {framework.wkst}")
    else:
        logger.error("✗ Failed: APTFramework does not have wkst attribute")
        raise AttributeError("APTFramework instance missing 'wkst' attribute")
    
    logger.info("Checking other impacket-related attributes...")
    required_attributes = [
        'ntlm', 'dcom', 'samr', 'lsad', 'impacket', 
        'SMBConnection', 'DCERPCTransportFactory',
        'RPC_C_AUTHN_LEVEL_PKT_PRIVACY', 'RPC_C_AUTHN_GSS_NEGOTIATE'
    ]
    
    missing_attributes = []
    for attr in required_attributes:
        if hasattr(framework, attr):
            logger.debug(f"✓ {attr} exists")
        else:
            logger.warning(f"✗ {attr} missing")
            missing_attributes.append(attr)
    
    if missing_attributes:
        logger.error(f"Missing attributes: {', '.join(missing_attributes)}")
        raise AttributeError(f"APTFramework missing attributes: {', '.join(missing_attributes)}")
    
    logger.info("All tests passed!")
    return True

if __name__ == "__main__":
    logger.info("=== Testing APTFramework.wkst attribute ===")
    try:
        test_wkst_attribute()
    except Exception as e:
        logger.error(f"Test failed: {e}")
        import traceback
        logger.error(f"Stack trace: {traceback.format_exc()}")
        raise
