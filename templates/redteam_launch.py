#!/usr/bin/env python3
"""
Red Team Launch Server - Simplified Version (without Twilio)
Main entry point for the Red Team deployment system
"""

import os
import sys
import threading
from flask import Flask, render_template, request, jsonify, send_file
from gtts import gTTS
from playwright.sync_api import sync_playwright
import requests
import time

# Initialize Flask app
app = Flask(__name__, template_folder=os.path.abspath('.'))

@app.route('/')
def index():
    """Main dashboard"""
    return render_template('redteam_dashboard.html')

@app.route('/api/launch_vishing', methods=['POST'])
def launch_vishing():
    """Launch a vishing (voice phishing) attack (simulated)"""
    try:
        data = request.json
        phone_number = data.get('phone_number')
        script = data.get('script')
        language = data.get('language', 'en')
        
        # Generate voice file
        audio_file = f"calls/vishing_{int(time.time())}.mp3"
        tts = gTTS(text=script, lang=language)
        tts.save(audio_file)
        
        return jsonify({
            "success": True,
            "message": f"Vishing attack simulated. Audio file generated: {audio_file}",
            "audio_file": audio_file
        })
            
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@app.route('/api/launch_spearphish', methods=['POST'])
def launch_spearphish():
    """Launch a spear phishing attack (simulated)"""
    try:
        data = request.json
        email = data.get('email')
        subject = data.get('subject')
        template = data.get('template')
        
        # Generate phishing email
        html_content = render_template(f"phish_templates/{template}.html", 
                                     email=email,
                                     timestamp=int(time.time()))
        
        return jsonify({
            "success": True,
            "message": f"Phishing email prepared for {email}",
            "html_content": html_content
        })
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@app.route('/api/recon', methods=['POST'])
def run_recon():
    """Run reconnaissance on a target (simulated)"""
    try:
        data = request.json
        target = data.get('target')
        
        print(f"Running reconnaissance on {target}")
        # Simulate reconnaissance
        time.sleep(2)
        
        return jsonify({
            "success": True,
            "target": target,
            "findings": [
                "LinkedIn profile found",
                "Twitter account active",
                "Company website vulnerable to XSS",
                "Email address found: john.doe@company.com"
            ]
        })
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@app.route('/api/get_templates')
def get_templates():
    """Get available phishing templates"""
    try:
        templates_dir = 'templates/phish_templates'
        if not os.path.exists(templates_dir):
            os.makedirs(templates_dir)
            return jsonify({"templates": []})
            
        templates = [f.split('.')[0] for f in os.listdir(templates_dir) if f.endswith('.html')]
        return jsonify({"templates": templates})
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@app.route('/api/get_targets')
def get_targets():
    """Get target list from targets.txt"""
    try:
        if os.path.exists('targets.txt'):
            with open('targets.txt', 'r') as f:
                targets = [line.strip() for line in f.readlines() if line.strip()]
            return jsonify({"targets": targets})
        return jsonify({"targets": []})
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@app.route('/api/add_target', methods=['POST'])
def add_target():
    """Add a new target to targets.txt"""
    try:
        data = request.json
        target = data.get('target')
        
        with open('targets.txt', 'a') as f:
            f.write(f"{target}\n")
            
        return jsonify({"success": True, "message": f"Target {target} added"})
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@app.route('/api/screenshot', methods=['POST'])
def take_screenshot():
    """Take a screenshot of a website"""
    try:
        data = request.json
        url = data.get('url')
        
        screenshot_file = f"screenshots/{int(time.time())}_screenshot.png"
        
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(url)
            page.screenshot(path=screenshot_file)
            browser.close()
            
        return send_file(screenshot_file, mimetype='image/png')
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == '__main__':
    # Create directories if they don't exist
    for dir_name in ['calls', 'tracks', 'payloads', 'static', 'templates/phish_templates', 'screenshots']:
        os.makedirs(dir_name, exist_ok=True)
    
    print("=" * 60)
    print("RED TEAM DEPLOYMENT SYSTEM ACTIVE")
    print("=" * 60)
    print("Twilio integration disabled (simplified version)")
    print("=" * 60)
    
    try:
        # Start Flask server
        app.run(host='0.0.0.0', port=3000, debug=True)
    except Exception as e:
        print(f"Error starting server: {e}")
        print("Trying to start on port 8080 instead...")
        app.run(host='0.0.0.0', port=8080, debug=True)
