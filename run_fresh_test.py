#!/usr/bin/env python3
import sys
import os
import tempfile

# Create a fresh test script to avoid any caching
test_content = """#!/usr/bin/env python3
import sys
sys.path.insert(0, '{working_dir}')

from modules.payloads import apt_framework
apt = apt_framework.APTFramework()
print('IMPACKET_AVAILABLE:', apt.impacket_available)
print('SMBConnection type:', type(apt_framework.SMBConnection))
print('SMBConnection value:', apt_framework.SMBConnection)
""".format(working_dir=os.path.abspath('.').replace('\\', '\\\\'))

# Create temporary file
with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as f:
    f.write(test_content)
    temp_filename = f.name

try:
    # Run the fresh test
    import subprocess
    result = subprocess.run(
        [sys.executable, temp_filename],
        capture_output=True,
        text=True,
        cwd=os.path.abspath('.')
    )
    
    print("=== Test Output ===")
    print(result.stdout)
    
    if result.stderr:
        print("\n=== Errors ===")
        print(result.stderr)
        
    print(f"\nReturn code: {result.returncode}")
        
finally:
    # Cleanup
    try:
        os.remove(temp_filename)
        pyc_file = temp_filename + 'c'
        if os.path.exists(pyc_file):
            os.remove(pyc_file)
    except Exception:
        pass
