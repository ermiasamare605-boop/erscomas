#!/usr/bin/env python3
"""
Comprehensive test script for all main components of the project
"""

import sys
import traceback

def test_apt_framework():
    """Test apt_framework functionality"""
    print("=== Testing apt_framework ===")
    try:
        import apt_framework_fixed
        print("✅ apt_framework_fixed imported successfully")
        
        import apt_toolkit
        print("✅ apt_toolkit imported successfully")
        
        import apt_master
        print("✅ apt_master imported successfully")
        
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        print(f"Stack trace: {traceback.format_exc()}")
        return False

def test_social_hacker():
    """Test social_hacker module"""
    print("\n=== Testing social_hacker ===")
    try:
        import social_hacker
        print("✅ social_hacker imported successfully")
        
        # Create instance
        hacker = social_hacker.SocialHacker()
        print("✅ SocialHacker instance created successfully")
        
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        print(f"Stack trace: {traceback.format_exc()}")
        return False

def test_c2_server():
    """Test c2_server module"""
    print("\n=== Testing c2_server ===")
    try:
        import c2_server
        print("✅ c2_server imported successfully")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        print(f"Stack trace: {traceback.format_exc()}")
        return False

def test_cloud_pivot():
    """Test cloud_pivot module"""
    print("\n=== Testing cloud_pivot ===")
    try:
        import cloud_pivot
        print("✅ cloud_pivot imported successfully")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        print(f"Stack trace: {traceback.format_exc()}")
        return False

def test_burp_ext():
    """Test burp_ext module"""
    print("\n=== Testing burp_ext ===")
    try:
        import burp_ext
        print("✅ burp_ext imported successfully")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        print(f"Stack trace: {traceback.format_exc()}")
        return False

def test_lateral():
    """Test lateral movement module"""
    print("\n=== Testing lateral movement ===")
    try:
        import lateral
        print("✅ lateral imported successfully")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        print(f"Stack trace: {traceback.format_exc()}")
        return False

def test_persistence():
    """Test persistence module"""
    print("\n=== Testing persistence ===")
    try:
        import persistence_config
        print("✅ persistence_config imported successfully")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        print(f"Stack trace: {traceback.format_exc()}")
        return False

def main():
    """Main test function"""
    print("=" * 50)
    print("COMPREHENSIVE PROJECT TEST SUITE")
    print("=" * 50)
    
    tests = [
        test_apt_framework,
        test_social_hacker,
        test_c2_server,
        test_cloud_pivot,
        test_burp_ext,
        test_lateral,
        test_persistence
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"❌ Test failed with exception: {e}")
            failed += 1
    
    print("\n" + "=" * 50)
    print(f"TEST SUMMARY: {passed} PASSED, {failed} FAILED")
    print("=" * 50)
    
    return failed == 0

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
