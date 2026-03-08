#!/usr/bin/env python3
import sys
import os

# Run in completely clean environment
def clean_import():
    # Clear all previous modules
    sys.modules.clear()
    
    # Reset system paths
    import sys as sys_module
    sys_module.path = []
    
    # Add only current directory
    current_dir = os.path.abspath('.')
    sys_module.path.insert(0, current_dir)
    
    # Import apt_framework
    from modules.payloads.apt_framework import APTFramework
    framework = APTFramework()
    return framework.check_impacket_available()

if __name__ == "__main__":
    try:
        available = clean_import()
        print(f"Impacket available: {available}")
    except Exception as e:
        print(f"Error: {type(e).__name__}: {e}")
        import traceback
        print(traceback.format_exc())
