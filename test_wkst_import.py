
#!/usr/bin/env python3
try:
    # Try to import wkst directly from impacket
    from impacket.dcerpc.v5 import wkst
    print("Successfully imported wkst directly from impacket")
    print(f"wkst module: {wkst}")
    print(f"wkst module file: {wkst.__file__}")
    
    # Check if MSRPC_UUID_WKST exists
    if hasattr(wkst, 'MSRPC_UUID_WKST'):
        print(f"MSRPC_UUID_WKST: {wkst.MSRPC_UUID_WKST}")
    
    # Check if hNetrWkstaGetInfo exists
    if hasattr(wkst, 'hNetrWkstaGetInfo'):
        print(f"hNetrWkstaGetInfo: {wkst.hNetrWkstaGetInfo}")
        
except Exception as e:
    print(f"Error importing wkst: {e}")
    import traceback
    print(traceback.format_exc())

try:
    # Try to import through apt_framework_fixed
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).parent))
    
    from apt_framework_fixed import wkst as apt_wkst
    print("\nSuccessfully imported wkst from apt_framework_fixed")
    print(f"wkst type: {type(apt_wkst)}")
    print(f"wkst value: {apt_wkst}")
    
except Exception as e:
    print(f"\nError importing wkst from apt_framework_fixed: {e}")
    import traceback
    print(traceback.format_exc())
