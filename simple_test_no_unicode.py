#!/usr/bin/env python3
"""Test script to verify apt_framework impacket imports (without Unicode)"""

import sys
from pathlib import Path

# Add the hacking directory to path
sys.path.insert(0, str(Path(__file__).parent))

# Test importing apt_framework
try:
    from modules.payloads.apt_framework import APTFramework
    print("Successfully imported APTFramework")
    
    # Create instance
    framework = APTFramework()
    print(f"Framework created, impacket available: {framework.impacket_available}")
    
    if framework.impacket_available:
        print("Impacket library is available")
        
except Exception as e:
    print(f"Error: {e}")
    import traceback
    print(traceback.format_exc())
