#!/usr/bin/env python3
with open('modules/payloads/apt_framework.py', 'r', encoding='utf-8') as f:
    content = f.read()

import re
matches = re.finditer(r'(?:^|\W)impacket\s*=', content, re.MULTILINE)
for match in matches:
    start_pos = max(0, match.start() - 20)
    end_pos = min(len(content), match.end() + 20)
    context = content[start_pos:end_pos]
    print(f"Found 'impacket =' at position {match.start()}:")
    print(repr(context))
    print('-' * 50)
