#!/usr/bin/env python3
import sys
import os
import pathlib

print("Current directory:", os.getcwd())

# Try running from apt_framework.py's directory
apt_dir = os.path.join(os.getcwd(), "modules", "payloads")
os.chdir(apt_dir)
print("Changed to apt dir:", os.getcwd())

sys.path.insert(0, os.path.abspath(os.path.join(apt_dir, "..", "..", "impacket")))

print("sys.path[0]:", sys.path[0])

# Check if the file exists
dcerpc_path = os.path.join(sys.path[0], "impacket", "dcerpc", "v5", "transport.py")
print("dcerpc transport.py exists:", os.path.exists(dcerpc_path))

if os.path.exists(dcerpc_path):
    print("dcerpc transport.py contents snippet:", repr(open(dcerpc_path, 'rb').read(500)))

try:
    import impacket
    print("import impacket successful")
    print("impacket.__file__:", impacket.__file__)
    print("impacket.__path__:", impacket.__path__)
except Exception as e:
    print(f"import impacket failed: {e}")
    import traceback
    print(traceback.format_exc())

try:
    from impacket.dcerpc.v5.transport import DCERPCTransportFactory
    print("import DCERPCTransportFactory successful")
except Exception as e:
    print(f"import DCERPCTransportFactory failed: {e}")
    import traceback
    print(traceback.format_exc())
