#!/usr/bin/env python3
import sys
import os

sys.path.insert(0, 'c:/Users/ermias3706/hacking/impacket')

print("sys.path[0] =", repr(sys.path[0]))
print("os.path.exists(sys.path[0]) =", os.path.exists(sys.path[0]))

impacket_dir = os.path.join(sys.path[0], 'impacket')
print("impacket_dir =", repr(impacket_dir))
print("os.path.exists(impacket_dir) =", os.path.exists(impacket_dir))

if os.path.exists(impacket_dir):
    print("\nContents of impacket_dir:")
    for item in os.listdir(impacket_dir):
        print("  -", repr(item))
        
dcerpc_dir = os.path.join(impacket_dir, 'dcerpc')
print("\ndcerpc_dir =", repr(dcerpc_dir))
print("os.path.exists(dcerpc_dir) =", os.path.exists(dcerpc_dir))

if os.path.exists(dcerpc_dir):
    print("\nContents of dcerpc_dir:")
    for item in os.listdir(dcerpc_dir):
        print("  -", repr(item))

dcerpc_v5_dir = os.path.join(dcerpc_dir, 'v5')
print("\ndcerpc_v5_dir =", repr(dcerpc_v5_dir))
print("os.path.exists(dcerpc_v5_dir) =", os.path.exists(dcerpc_v5_dir))

if os.path.exists(dcerpc_v5_dir):
    print("\nContents of dcerpc_v5_dir:")
    for item in os.listdir(dcerpc_v5_dir):
        print("  -", repr(item))

try:
    import impacket
    print("\n=== import impacket ===")
    print("Success")
    print("impacket.__file__ =", impacket.__file__)
    print("impacket.__path__ =", impacket.__path__)
except Exception as e:
    print("\n=== import impacket ===")
    print(f"Error: {e}")
    import traceback
    print(traceback.format_exc())

try:
    from impacket import dcerpc
    print("\n=== from impacket import dcerpc ===")
    print("Success")
except Exception as e:
    print("\n=== from impacket import dcerpc ===")
    print(f"Error: {e}")
    import traceback
    print(traceback.format_exc())
