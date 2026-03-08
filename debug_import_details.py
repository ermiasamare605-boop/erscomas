#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.abspath('.'))

# Enable debug output
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

try:
    # Import the apt_framework module
    from modules.payloads.apt_framework import APTFramework
    
    # Check impacket availability
    framework = APTFramework()
    logger.info("Impacket available: %s", framework.check_impacket_available())
    
    # Debug what modules were imported
    logger.info("All impacket modules in sys.modules:")
    for key in list(sys.modules.keys()):
        if key.startswith('impacket'):
            logger.info("  %s: %s", key, sys.modules[key])
            
    # Try to directly import SMBConnection
    if framework.check_impacket_available():
        logger.info("\nTrying to import SMBConnection directly:")
        try:
            from impacket.smbconnection import SMBConnection
            logger.info("  Success: %s", SMBConnection)
        except Exception as e:
            logger.error("  Error: %s", e)
            import traceback
            logger.error("  Stack trace: %s", traceback.format_exc())
            
except Exception as e:
    logger.error("Error: %s", e)
    import traceback
    logger.error("Stack trace: %s", traceback.format_exc())
