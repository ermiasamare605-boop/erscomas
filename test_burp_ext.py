#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script to verify the Burp Suite extension structure
"""

import sys

def test_burp_extension():
    """
    Test function to check if the Burp extension structure is valid
    """
    try:
        # Try to import the extension
        from burp_ext import BurpExtender, BURP_AVAILABLE
        print("BurpExtender class imported successfully")
        
        # Check if BURP_AVAILABLE flag is correctly set
        if BURP_AVAILABLE:
            print("Running in Burp Suite environment")
        else:
            print("Running in dummy/test environment")
        
        # Check if it has required methods
        required_methods = ['registerExtenderCallbacks', 'getTabCaption', 'getUiComponent']
        for method in required_methods:
            if hasattr(BurpExtender, method):
                print(f"BurpExtender has {method} method")
            else:
                print(f"BurpExtender missing {method} method")
                return False
        
        # Test creating an instance
        extender = BurpExtender()
        print("BurpExtender instance created successfully")
        
        print("\nExtension structure is valid!")
        return True
        
    except ImportError as e:
        print(f"Import error: {e}")
        return False
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        print(traceback.format_exc())
        return False

if __name__ == "__main__":
    print("Testing Burp Suite Extension Structure...\n")
    success = test_burp_extension()
    
    if not success:
        print("\nTest failed")
        sys.exit(1)
    else:
        print("\nAll tests passed")
        sys.exit(0)