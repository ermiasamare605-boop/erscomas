#!/usr/bin/env python3
"""
System overview script to display current state of Social C2 system
"""

import requests
import json

C2_SERVER = "http://localhost:5000"

def print_system_overview():
    """Print system overview"""
    print("=== SOCIAL C2 SYSTEM OVERVIEW ===")
    print()
    
    # Check C2 Server
    try:
        response = requests.get(f"{C2_SERVER}/health")
        if response.status_code == 200:
            data = response.json()
            print(f"[OK] C2 Server: Running (Status: {data['status']})")
        else:
            print(f"[ERROR] C2 Server: Error (Status: {response.status_code})")
    except Exception as e:
        print(f"[ERROR] C2 Server: Error - {e}")
    
    # Check Dashboard
    try:
        response = requests.get("http://localhost:3000")
        if response.status_code == 200:
            print(f"[OK] Dashboard: Running (Status: {response.status_code})")
        else:
            print(f"[ERROR] Dashboard: Error (Status: {response.status_code})")
    except Exception as e:
        print(f"[ERROR] Dashboard: Error - {e}")
    
    # Check Phishing Server
    try:
        response = requests.get("http://localhost:8000")
        if response.status_code == 200:
            print(f"[OK] Phishing Server: Running (Status: {response.status_code})")
        else:
            print(f"[ERROR] Phishing Server: Error (Status: {response.status_code})")
    except Exception as e:
        print(f"[ERROR] Phishing Server: Error - {e}")
    
    print()
    
    # Get sessions
    try:
        response = requests.get(f"{C2_SERVER}/sessions")
        if response.status_code == 200:
            sessions = response.json()
            print(f"=== ACTIVE SESSIONS ({len(sessions)}) ===")
            for session in sessions:
                print(f"  ID: {session['id']}")
                print(f"  Target: {session['target']}")
                print(f"  Platform: {session['platform']}")
                print(f"  Status: {session['status']}")
                print(f"  Start Time: {session['start_time']}")
                if session['end_time']:
                    print(f"  End Time: {session['end_time']}")
                print()
    except Exception as e:
        print(f"❌ Sessions: Error - {e}")
    
    # Get payloads
    try:
        response = requests.get(f"{C2_SERVER}/payloads")
        if response.status_code == 200:
            payloads = response.json()
            print(f"=== DEPLOYED PAYLOADS ({len(payloads)}) ===")
            for payload in payloads:
                print(f"  ID: {payload['id']}")
                print(f"  Session ID: {payload['session_id']}")
                print(f"  Type: {payload['payload_type']}")
                print(f"  Target: {payload['target']}")
                print(f"  Status: {payload['status']}")
                print(f"  Deployed At: {payload['deployed_at']}")
                if payload['result']:
                    print(f"  Result: {payload['result']}")
                print()
    except Exception as e:
        print(f"❌ Payloads: Error - {e}")
    
    print("=== SYSTEM READY ===")

if __name__ == "__main__":
    print_system_overview()
