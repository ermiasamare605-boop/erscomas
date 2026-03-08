#!/usr/bin/env python3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

try:
    from apt_framework_fixed import APTFramework, IMPACKET_AVAILABLE
    
    print("Successfully imported apt_framework_fixed module")
    
    framework = APTFramework()
    print("Impacket available:", framework.check_impacket_available())
    print("Global IMPACKET_AVAILABLE:", IMPACKET_AVAILABLE)
    
    if IMPACKET_AVAILABLE:
        print("Impacket imports are working")
    
except Exception as e:
    print("Error:", e)
    import traceback
    print(traceback.format_exc())
