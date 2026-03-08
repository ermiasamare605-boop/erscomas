#!/usr/bin/env python3
import sys
import os
import logging
import traceback
import importlib.util

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

sys.path.insert(0, os.path.abspath('.'))

try:
    # Trace import mechanism
    logger.info("=== START IMPORT TRACE ===")
    
    # Check if impacket module exists in any location
    logger.info("Checking sys.path for impacket:")
    for i, path in enumerate(sys.path):
        logger.info(f"  {i}: {path}")
        if os.path.exists(os.path.join(path, 'impacket')):
            logger.info(f"  ✓ impacket directory found at: {os.path.join(path, 'impacket')}")
            logger.info(f"  Contents: {os.listdir(os.path.join(path, 'impacket'))}")
    
    # Clear any existing impacket modules
    logger.info("\nClearing impacket modules from sys.modules:")
    for key in list(sys.modules.keys()):
        if key.startswith('impacket'):
            logger.info(f"  Removing: {key}")
            del sys.modules[key]
    
    # Clear modules cache
    logger.info("\nClearing __pycache__ directories:")
    for cache_dir in ['__pycache__', 'modules/__pycache__', 'modules/payloads/__pycache__']:
        if os.path.exists(cache_dir):
            logger.info(f"  Removing: {cache_dir}")
            import shutil
            shutil.rmtree(cache_dir)
    
    # Import apt_framework module with detailed tracing
    logger.info("\n=== Importing apt_framework ===")
    module_spec = importlib.util.spec_from_file_location(
        "modules.payloads.apt_framework", 
        "modules/payloads/apt_framework.py"
    )
    
    if module_spec is None:
        raise ImportError(f"Could not find module at modules/payloads/apt_framework.py")
        
    module = importlib.util.module_from_spec(module_spec)
    
    logger.info("Loading module code...")
    try:
        if module_spec.loader is None:
            raise ImportError(f"Module spec has no loader for modules.payloads.apt_framework")
            
        module_spec.loader.exec_module(module)
        logger.info("Module loaded successfully")
    except Exception as e:
        logger.error(f"Error loading module: {e}")
        logger.error(f"Stack trace: {traceback.format_exc()}")
        raise
    
    # Test if it works
    logger.info("\n=== Testing APTFramework ===")
    framework = module.APTFramework()
    logger.info(f"Impacket available: {framework.impacket_available}")
    
    if framework.impacket_available:
        logger.info("✓ All impacket imports succeeded")
        logger.info("\nChecking if we can use SMBConnection:")
        try:
            conn = module.SMBConnection
            logger.info(f"  ✓ SMBConnection is available: {conn}")
        except Exception as e:
            logger.error(f"  ✗ Failed to access SMBConnection: {e}")
            logger.error(traceback.format_exc())
            
        logger.info("\nChecking impacket module contents:")
        logger.info(f"  impacket module: {module.impacket}")
        logger.info(f"  impacket module type: {type(module.impacket)}")
        
        if hasattr(module.impacket, 'smbconnection'):
            logger.info(f"  smbconnection module: {module.impacket.smbconnection}")
        else:
            logger.warning("  smbconnection module not found in impacket")
            
        logger.info("\nChecking all impacket-related modules in sys.modules:")
        for key in sorted(sys.modules.keys()):
            if key.startswith('impacket'):
                logger.info(f"  {key}: {sys.modules[key]}")
                
    else:
        logger.warning("✗ impacket library not available")
        
except Exception as e:
    logger.error(f"=== TEST FAILED ===")
    logger.error(f"Error: {e}")
    logger.error(f"Stack trace: {traceback.format_exc()}")
    raise
