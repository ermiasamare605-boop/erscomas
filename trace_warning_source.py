#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.abspath('.'))

import logging
import traceback
import warnings

# Create custom logger to track where warnings are coming from
class TrackedLogger(logging.Logger):
    def warning(self, msg, *args, **kwargs):
        stack_trace = ''.join(traceback.format_stack())
        print(f"=== WARNING DETECTED ===")
        print(f"Message: {msg}")
        print(f"Stack trace:\n{stack_trace}")
        super().warning(msg, *args, **kwargs)

# Replace the logger
original_getLogger = logging.getLogger
def getLogger(name):
    logger = original_getLogger(name)
    if name == 'root' or name == __name__ or name == 'modules.payloads.apt_framework':
        logger.__class__ = TrackedLogger
    return logger
logging.getLogger = getLogger

# Capture all warnings
def warn_with_stacktrace(message, category, filename, lineno, file=None, line=None):
    print(f"=== PYTHON WARNING DETECTED ===")
    print(f"Message: {message}")
    print(f"Category: {category}")
    print(f"File: {filename}:{lineno}")
    stack_trace = ''.join(traceback.format_stack())
    print(f"Stack trace:\n{stack_trace}")
    warnings.showwarning = original_warn

original_warn = warnings.showwarning
warnings.showwarning = warn_with_stacktrace

try:
    from modules.payloads import apt_framework
    apt = apt_framework.APTFramework()
    print(f"\nAPTFramework.impacket_available: {apt.impacket_available}")
    
    if apt.impacket_available:
        print(f"\nImports successful:")
        print(f"SMBConnection: {apt_framework.SMBConnection}")
        print(f"DCERPCTransportFactory: {apt_framework.DCERPCTransportFactory}")
        print(f"wkst: {apt_framework.wkst}")
        print(f"ntlm: {apt_framework.ntlm}")
        
except Exception as e:
    print(f"\nERROR: {e}")
    print(traceback.format_exc())
