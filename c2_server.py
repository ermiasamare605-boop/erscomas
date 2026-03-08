#!/usr/bin/env python3
"""
C2 (Command and Control) Server for Social Media Penetration Testing
Provides a REST API to manage attack sessions, deploy payloads, and collect data.
"""

import os
import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import threading
import time

app = Flask(__name__)
CORS(app)

# Database setup
DATABASE = 'c2.db'

def init_db():
    """Initialize the database"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Create sessions table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            target TEXT NOT NULL,
            platform TEXT NOT NULL,
            status TEXT DEFAULT 'active',
            start_time DATETIME DEFAULT CURRENT_TIMESTAMP,
            end_time DATETIME,
            data TEXT
        )
    ''')
    
    # Create payloads table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS payloads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id INTEGER,
            payload_type TEXT,
            target TEXT,
            deployed_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            status TEXT DEFAULT 'pending',
            result TEXT,
            FOREIGN KEY (session_id) REFERENCES sessions (id)
        )
    ''')
    
    # Create credentials table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS credentials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id INTEGER,
            username TEXT,
            password TEXT,
            platform TEXT,
            harvested_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (session_id) REFERENCES sessions (id)
        )
    ''')
    
    conn.commit()
    conn.close()

@app.route('/sessions', methods=['GET'])
def get_sessions():
    """Get all active sessions"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT * FROM sessions 
        WHERE status = 'active' 
        ORDER BY start_time DESC
    ''')
    
    sessions = cursor.fetchall()
    conn.close()
    
    return jsonify([dict(session) for session in sessions])

@app.route('/sessions', methods=['POST'])
def create_session():
    """Create a new session"""
    data = request.json or {}
    target = data.get('target')
    platform = data.get('platform')
    
    if not target or not platform:
        return jsonify({'error': 'Target and platform are required'}), 400
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute(
        'INSERT INTO sessions (target, platform, status) VALUES (?, ?, ?)',
        (target, platform, 'active')
    )
    
    session_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return jsonify({'id': session_id, 'target': target, 'platform': platform, 'status': 'active'}), 201

@app.route('/sessions/<int:session_id>', methods=['GET'])
def get_session(session_id):
    """Get a specific session"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM sessions WHERE id = ?', (session_id,))
    session = cursor.fetchone()
    
    if not session:
        conn.close()
        return jsonify({'error': 'Session not found'}), 404
    
    # Get associated payloads
    cursor.execute('SELECT * FROM payloads WHERE session_id = ?', (session_id,))
    payloads = cursor.fetchall()
    
    # Get associated credentials
    cursor.execute('SELECT * FROM credentials WHERE session_id = ?', (session_id,))
    credentials = cursor.fetchall()
    
    conn.close()
    
    return jsonify({
        'session': dict(session),
        'payloads': [dict(payload) for payload in payloads],
        'credentials': [dict(credential) for credential in credentials]
    })

@app.route('/sessions/<int:session_id>/payloads', methods=['POST'])
def deploy_payload(session_id):
    """Deploy a payload to a session"""
    data = request.json or {}
    payload_type = data.get('type')
    target = data.get('target')
    
    if not payload_type or not target:
        return jsonify({'error': 'Payload type and target are required'}), 400
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute(
        'INSERT INTO payloads (session_id, payload_type, target) VALUES (?, ?, ?)',
        (session_id, payload_type, target)
    )
    
    payload_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return jsonify({'id': payload_id, 'session_id': session_id, 'type': payload_type, 'status': 'pending'}), 201

@app.route('/sessions/<int:session_id>/credentials', methods=['POST'])
def add_credentials(session_id):
    """Add harvested credentials to a session"""
    data = request.json or {}
    username = data.get('username')
    password = data.get('password')
    platform = data.get('platform')
    
    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute(
        '''
        INSERT INTO credentials (session_id, username, password, platform) 
        VALUES (?, ?, ?, ?)
        ''',
        (session_id, username, password, platform)
    )
    
    credential_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return jsonify({'id': credential_id, 'session_id': session_id, 'username': username}), 201

@app.route('/sessions/<int:session_id>', methods=['PUT'])
def update_session(session_id):
    """Update session status"""
    data = request.json or {}
    status = data.get('status')
    
    if status not in ['active', 'completed', 'failed']:
        return jsonify({'error': 'Invalid status'}), 400
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    end_time = datetime.now().isoformat() if status in ['completed', 'failed'] else None
    
    cursor.execute(
        'UPDATE sessions SET status = ?, end_time = ? WHERE id = ?',
        (status, end_time, session_id)
    )
    
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Session updated successfully'})

@app.route('/payloads/<int:payload_id>', methods=['PUT'])
def update_payload(payload_id):
    """Update payload status and results"""
    data = request.json or {}
    status = data.get('status')
    result = data.get('result')
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute(
        'UPDATE payloads SET status = ?, result = ? WHERE id = ?',
        (status, result, payload_id)
    )
    
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Payload updated successfully'})

@app.route('/payloads', methods=['GET'])
def get_payloads():
    """Get all payloads"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT * FROM payloads 
        ORDER BY deployed_at DESC
    ''')
    
    payloads = cursor.fetchall()
    conn.close()
    
    return jsonify([dict(payload) for payload in payloads])

@app.route('/payloads', methods=['POST'])
def create_payload():
    """Create a new payload"""
    data = request.json or {}
    session_id = data.get('session_id')
    payload_type = data.get('payload_type')
    target = data.get('target')
    
    if not session_id or not payload_type or not target:
        return jsonify({'error': 'Session ID, payload type, and target are required'}), 400
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute(
        'INSERT INTO payloads (session_id, payload_type, target) VALUES (?, ?, ?)',
        (session_id, payload_type, target)
    )
    
    payload_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return jsonify({'id': payload_id, 'session_id': session_id, 'payload_type': payload_type, 'target': target, 'status': 'pending'}), 201

@app.route('/sessions/<int:session_id>', methods=['DELETE'])
def delete_session(session_id):
    """Delete a session"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute('UPDATE sessions SET status = ?, end_time = ? WHERE id = ?', 
                  ('completed', datetime.now().isoformat(), session_id))
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Session ended successfully'})

@app.route('/dashboard', methods=['GET'])
def dashboard():
    """Serve the dashboard HTML"""
    return app.send_static_file('dashboard.html')

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'ok', 'timestamp': datetime.now().isoformat()})

def start_c2_server():
    """Start the C2 server"""
    print("Starting C2 Server on port 5000...")
    init_db()
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=False
    )

if __name__ == '__main__':
    start_c2_server()
