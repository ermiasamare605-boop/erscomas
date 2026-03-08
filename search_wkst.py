
import os
import re

def search_wkst():
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if 'wkst' in content:
                            print(f"Found 'wkst' in: {file_path}")
                            # Show lines containing 'wkst'
                            lines = content.split('\n')
                            for i, line in enumerate(lines, 1):
                                if 'wkst' in line:
                                    print(f"  Line {i}: {line.strip()}")
                except Exception as e:
                    pass

if __name__ == "__main__":
    search_wkst()
