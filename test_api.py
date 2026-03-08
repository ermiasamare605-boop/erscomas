#!/usr/bin/env python3
"""
Test script to verify C2 server API functionality
"""

import requests
import json

C2_SERVER = "http://localhost:5000"

def test_health_check():
    """Test health check endpoint"""
    print("=== Testing Health Check ===")
    try:
        response = requests.get(f"{C2_SERVER}/health")
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        print()
    except Exception as e:
        print(f"Error: {e}")
        print()

def test_get_sessions():
    """Test getting sessions"""
    print("=== Testing Get Sessions ===")
    try:
        response = requests.get(f"{C2_SERVER}/sessions")
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        print()
    except Exception as e:
        print(f"Error: {e}")
        print()

def test_get_payloads():
    """Test getting payloads"""
    print("=== Testing Get Payloads ===")
    try:
        response = requests.get(f"{C2_SERVER}/payloads")
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        print()
    except Exception as e:
        print(f"Error: {e}")
        print()

def test_create_payload():
    """Test creating a payload"""
    print("=== Testing Create Payload ===")
    try:
        payload = {
            "session_id": 1,
            "payload_type": "credential_harvest",
            "target": "testuser1"
        }
        response = requests.post(
            f"{C2_SERVER}/payloads",
            json=payload
        )
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        print()
    except Exception as e:
        print(f"Error: {e}")
        print()

def test_dashboard_access():
    """Test dashboard access"""
    print("=== Testing Dashboard Access ===")
    try:
        response = requests.get("http://localhost:3000")
        print(f"Status: {response.status_code}")
        print(f"Content Type: {response.headers['Content-Type']}")
        print(f"Content Length: {len(response.text)} bytes")
        print()
    except Exception as e:
        print(f"Error: {e}")
        print()

def test_phishing_server():
    """Test phishing server access"""
    print("=== Testing Phishing Server ===")
    try:
        response = requests.get("http://localhost:8000")
        print(f"Status: {response.status_code}")
        print(f"Content Type: {response.headers['Content-Type']}")
        print(f"Content Length: {len(response.text)} bytes")
        print()
    except Exception as e:
        print(f"Error: {e}")
        print()

if __name__ == "__main__":
    print("Testing Social C2 API\n")
    
    # Test all endpoints
    test_health_check()
    test_get_sessions()
    test_get_payloads()
    test_create_payload()
    test_dashboard_access()
    test_phishing_server()
    
    print("=== All tests completed ===")
