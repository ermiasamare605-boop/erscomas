#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.abspath('.'))

# Redirect warnings to file for debugging
import logging
logging.basicConfig(filename='warning_trace.log', level=logging.WARNING, 
                    format='%(asctime)s - %(levelname)s - %(message)s - %(pathname)s:%(lineno)d')

# Enable traceback for warnings
import warnings
from traceback import format_stack

def warn_with_traceback(message, category, filename, lineno, file=None, line=None):
    if file is not None and hasattr(file, 'write'):
        log = file
    else:
        log = sys.stderr
    stack_trace = ''.join(format_stack())
    log.write(warnings.formatwarning(message, category, filename, lineno, line))
    log.write(f"Stack trace: {stack_trace}\n")

warnings.showwarning = warn_with_traceback

try:
    from modules.payloads.apt_framework import APTFramework
    
    framework = APTFramework()
    print('Impacket available:', framework.check_impacket_available())
    
except Exception as e:
    print(f'Error: {e}')
    import traceback
    print(traceback.format_exc())
