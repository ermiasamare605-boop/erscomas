#!/usr/bin/env python3
import sys
import os
import logging

# Temporarily disable all logging
logging.disable(logging.CRITICAL)

sys.path.insert(0, os.path.abspath('.'))

from modules.payloads import apt_framework
apt = apt_framework.APTFramework()
print('IMPACKET_AVAILABLE:', apt.impacket_available)
print('SMBConnection type:', type(apt_framework.SMBConnection))
print('SMBConnection value:', apt_framework.SMBConnection)

# Restore logging
logging.disable(logging.NOTSET)
