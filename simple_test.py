#!/usr/bin/env python3
"""
Simple test script
"""
import sys
sys.path.insert(0, '.')

from modules.payloads import apt_framework
from modules import ad_pivot

print('=== apt_framework ===')
apt = apt_framework.APTFramework()
print(f'Impacket available: {apt.impacket_available}')
print(f'SMBConnection: {apt_framework.SMBConnection}')

print('\n=== ad_pivot ===')
ad = ad_pivot.ADPivot()
print(f'Impacket available: {ad.impacket_available}')