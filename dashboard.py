#!/usr/bin/env python3
"""
Dashboard Server for Social C2
Serves the HTML dashboard on port 3000
"""

import os
from flask import Flask, render_template
from flask_cors import CORS

# Create Flask app with correct static and template folder configuration
app = Flask(__name__, 
            template_folder='templates', 
            static_folder='static')
CORS(app)

@app.route('/')
def index():
    """Serve the dashboard HTML file"""
    return render_template('dashboard.html')

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return {'status': 'ok'}

def start_dashboard_server():
    """Start the dashboard server"""
    print("Starting Dashboard Server on port 3000...")
    app.run(
        host='0.0.0.0',
        port=3000,
        debug=False
    )

if __name__ == '__main__':
    start_dashboard_server()
