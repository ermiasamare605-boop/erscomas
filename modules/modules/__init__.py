"""
Nested modules package for configuration and additional resources
"""

import json
from pathlib import Path

# Load configuration from config.json
def load_config():
    """Load configuration from config.json file"""
    config_path = Path(__file__).parent / "config.json"
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        return config
    except Exception as e:
        print(f"Error loading configuration: {e}")
        return {}

# Load config on module initialization
config = load_config()

# Export configuration
__all__ = ['config', 'load_config']
