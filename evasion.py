#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Evasion Module - Provides evasion techniques for penetration testing
"""

def xor_encrypt(data, key):
    """
    XOR encryption/decryption function (since XOR is symmetric)
    
    Args:
        data (str or bytes): Data to encrypt/decrypt
        key (str or bytes): Encryption key
        
    Returns:
        bytes: Encrypted/decrypted data
        
    Examples:
        >>> encrypted = xor_encrypt("test data", "key123")
        >>> decrypted = xor_encrypt(encrypted, "key123")
        >>> decrypted.decode('utf-8')
        'test data'
    """
    if isinstance(data, str):
        data = data.encode('utf-8')
    if isinstance(key, str):
        key = key.encode('utf-8')
    
    encrypted = bytearray()
    key_length = len(key)
    
    for i, byte in enumerate(data):
        encrypted_byte = byte ^ key[i % key_length]
        encrypted.append(encrypted_byte)
    
    return bytes(encrypted)


def base64_encode(data):
    """
    Base64 encoding for data obfuscation
    
    Args:
        data (str or bytes): Data to encode
        
    Returns:
        str: Base64 encoded string
    """
    import base64
    
    if isinstance(data, str):
        data = data.encode('utf-8')
        
    return base64.b64encode(data).decode('utf-8')


def base64_decode(data):
    """
    Base64 decoding
    
    Args:
        data (str or bytes): Base64 encoded data
        
    Returns:
        bytes: Decoded data
    """
    import base64
    
    if isinstance(data, str):
        data = data.encode('utf-8')
        
    return base64.b64decode(data)


def rot13(text):
    """
    ROT13 encryption/decryption (Caesar cipher with shift 13)
    
    Args:
        text (str): Text to encrypt/decrypt
        
    Returns:
        str: Encrypted/decrypted text
    """
    result = []
    
    for char in text:
        if 'a' <= char <= 'z':
            result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':
            result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
        else:
            result.append(char)
    
    return ''.join(result)


def hex_encode(data):
    """
    Hexadecimal encoding
    
    Args:
        data (str or bytes): Data to encode
        
    Returns:
        str: Hex encoded string
    """
    if isinstance(data, str):
        data = data.encode('utf-8')
        
    return data.hex()


def hex_decode(hex_str):
    """
    Hexadecimal decoding
    
    Args:
        hex_str (str): Hex encoded string
        
    Returns:
        bytes: Decoded data
    """
    return bytes.fromhex(hex_str)


def generate_random_key(length=16):
    """
    Generate a random encryption key
    
    Args:
        length (int): Length of the key in bytes
        
    Returns:
        bytes: Random key
    """
    import os
    return os.urandom(length)


def obfuscate_string(text):
    """
    Multi-layer obfuscation for strings
    
    Args:
        text (str): Text to obfuscate
        
    Returns:
        str: Obfuscated string (base64 encoded XOR encrypted)
    """
    key = generate_random_key(8)
    encrypted = xor_encrypt(text, key)
    obfuscated = base64_encode(key + encrypted)
    
    return obfuscated


def deobfuscate_string(obfuscated_text):
    """
    Deobfuscate a string obfuscated with obfuscate_string()
    
    Args:
        obfuscated_text (str): Obfuscated string
        
    Returns:
        str: Deobfuscated text
    """
    decoded = base64_decode(obfuscated_text)
    key = decoded[:8]
    encrypted_data = decoded[8:]
    decrypted = xor_encrypt(encrypted_data, key)
    
    return decrypted.decode('utf-8')


if __name__ == "__main__":
    # Test the functions
    test_data = "This is a test message for evasion techniques"
    print(f"Original: {test_data}")
    
    # Test XOR encryption
    key = "secretkey"
    encrypted = xor_encrypt(test_data, key)
    decrypted = xor_encrypt(encrypted, key)
    print(f"\nXOR Test:")
    print(f"Encrypted: {encrypted.hex()}")
    print(f"Decrypted: {decrypted.decode('utf-8')}")
    
    # Test obfuscation
    obfuscated = obfuscate_string(test_data)
    deobfuscated = deobfuscate_string(obfuscated)
    print(f"\nObfuscation Test:")
    print(f"Obfuscated: {obfuscated}")
    print(f"Deobfuscated: {deobfuscated}")
    
    # Test ROT13
    rot13_text = rot13(test_data)
    print(f"\nROT13 Test:")
    print(f"Encrypted: {rot13_text}")
    print(f"Decrypted: {rot13(rot13_text)}")
