#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')
from apt_framework_fixed import APTFramework

framework = APTFramework()
print('Impacket available:', framework.check_impacket_available())
if framework.check_impacket_available():
    print('All imports succeeded')
else:
    print('Some imports failed')
