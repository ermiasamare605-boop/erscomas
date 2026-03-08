#!/usr/bin/env python3
"""
Vishing Module
Voice phishing functionality using Twilio and Google Text-to-Speech
"""

import os
import sys
import time
import random
import json
from twilio.rest import Client
from gtts import gTTS
import pyttsx3

class VishingModule:
    """Voice phishing module"""
    
    def __init__(self, twilio_sid, twilio_token, twilio_phone):
        """Initialize the vishing module with Twilio credentials"""
        self.twilio_sid = twilio_sid
        self.twilio_token = twilio_token
        self.twilio_phone = twilio_phone
        self.client = Client(twilio_sid, twilio_token)
        
    def generate_voice_script(self, language='en'):
        """Generate a random vishing script based on common scenarios"""
        scripts = {
            'en': [
                {
                    'title': 'Bank Security Alert',
                    'content': 'Hello, this is a security alert from your bank. We have detected unusual activity on your account. Please press 1 to verify your identity immediately or your account will be suspended.',
                    'category': 'Banking'
                },
                {
                    'title': 'IRS Tax Warning',
                    'content': 'This is a final notice from the Internal Revenue Service. You have failed to pay your taxes for the year 2023. If you do not call us back within 24 hours, you will be subject to immediate arrest. Please press 1 to speak with an agent.',
                    'category': 'Government'
                },
                {
                    'title': 'Amazon Order Issue',
                    'content': 'Hello, this is Amazon customer service. We noticed an issue with your recent order. Your package was damaged during shipping and we need to verify your address to send a replacement. Please press 1 to confirm your details.',
                    'category': 'E-Commerce'
                },
                {
                    'title': 'Tech Support Scam',
                    'content': 'This is Microsoft technical support. We have detected a virus on your computer that is causing critical errors. To prevent your system from crashing, please press 1 to speak with a technician immediately.',
                    'category': 'Tech Support'
                },
                {
                    'title': 'Social Security Scam',
                    'content': 'This is a call from the Social Security Administration. Your Social Security number has been compromised and is being used fraudulently. Please press 1 to verify your identity and protect your benefits.',
                    'category': 'Government'
                }
            ],
            'es': [
                {
                    'title': 'Alerta de Seguridad Bancaria',
                    'content': 'Hola, este es un aviso de seguridad de su banco. Hemos detectado actividad inusual en su cuenta. Por favor, pulse 1 para verificar su identidad inmediatamente o su cuenta será suspendida.',
                    'category': 'Bancario'
                },
                {
                    'title': 'Aviso de Impuestos',
                    'content': 'Este es un aviso final de la Agencia Tributaria. No ha pagado sus impuestos del año 2023. Si no nos llama dentro de las próximas 24 horas, estará sujeto a arresto inmediato. Por favor, pulse 1 para hablar con un agente.',
                    'category': 'Gobierno'
                },
                {
                    'title': 'Problema con el Pedido',
                    'content': 'Hola, este es el servicio al cliente de Amazon. Notamos un problema con su pedido reciente. Su paquete se dañó durante el envío y necesitamos verificar su dirección para enviar un reemplazo. Por favor, pulse 1 para confirmar sus detalles.',
                    'category': 'Comercio Electrónico'
                }
            ]
        }
        
        return random.choice(scripts.get(language, scripts['en']))
    
    def create_voice_recording(self, script, language='en', output_file=None):
        """Create a voice recording from text using Google TTS"""
        if output_file is None:
            timestamp = int(time.time())
            output_file = f"calls/vishing_{timestamp}.mp3"
            
        try:
            tts = gTTS(text=script, lang=language, slow=False)
            tts.save(output_file)
            print(f"Voice recording created: {output_file}")
            return output_file
        except Exception as e:
            print(f"Error creating voice recording: {e}")
            return None
            
    def send_vishing_call(self, to_number, recording_url):
        """Send a vishing call using Twilio"""
        try:
            call = self.client.calls.create(
                url=f"http://your-server-ip:3000/api/play_audio?file={recording_url}",
                to=to_number,
                from_=self.twilio_phone
            )
            
            print(f"Call initiated: {call.sid}")
            
            # Save call details
            call_details = {
                'sid': call.sid,
                'to': to_number,
                'from': self.twilio_phone,
                'timestamp': int(time.time()),
                'status': 'initiated',
                'recording': recording_url
            }
            
            self.save_call_details(call_details)
            
            return call.sid
        except Exception as e:
            print(f"Error sending call: {e}")
            return None
            
    def save_call_details(self, call_details):
        """Save call details to a file"""
        filename = f"calls/call_{call_details['sid']}.json"
        try:
            with open(filename, 'w') as f:
                json.dump(call_details, f)
            print(f"Call details saved to: {filename}")
        except Exception as e:
            print(f"Error saving call details: {e}")
            
    def launch_campaign(self, target_list, language='en', batch_size=1):
        """Launch a vishing campaign against a list of targets"""
        print(f"Launching vishing campaign with {len(target_list)} targets")
        
        results = []
        
        for i, target in enumerate(target_list):
            if i > 0 and i % batch_size == 0:
                print(f"Waiting 60 seconds before next batch...")
                time.sleep(60)
                
            print(f"Processing target {i+1}/{len(target_list)}: {target}")
            
            # Get script
            script_data = self.generate_voice_script(language)
            print(f"Using script: {script_data['title']}")
            
            # Create recording
            recording_file = self.create_voice_recording(script_data['content'], language)
            
            if recording_file:
                # Send call
                call_sid = self.send_vishing_call(target, recording_file)
                
                results.append({
                    'target': target,
                    'call_sid': call_sid,
                    'recording': recording_file,
                    'script': script_data['title'],
                    'category': script_data['category'],
                    'timestamp': int(time.time())
                })
                
                print(f"Call scheduled for {target}")
                
        return results
        
    def list_calls(self):
        """List all previous calls"""
        calls_dir = 'calls'
        calls = []
        
        if os.path.exists(calls_dir):
            for filename in os.listdir(calls_dir):
                if filename.startswith('call_') and filename.endswith('.json'):
                    try:
                        with open(os.path.join(calls_dir, filename), 'r') as f:
                            call_data = json.load(f)
                            calls.append(call_data)
                    except Exception as e:
                        print(f"Error reading call file {filename}: {e}")
                        
        return calls
        
    def get_call_details(self, call_sid):
        """Get detailed information about a specific call"""
        try:
            call_file = f"calls/call_{call_sid}.json"
            
            if os.path.exists(call_file):
                with open(call_file, 'r') as f:
                    return json.load(f)
                    
            return None
        except Exception as e:
            print(f"Error getting call details: {e}")
            return None
            
    def play_recording(self, file_path):
        """Play a voice recording locally (for testing)"""
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            return False
            
        try:
            engine = pyttsx3.init()
            with open(file_path, 'rb') as f:
                engine.play_recording(f)
            return True
        except Exception as e:
            print(f"Error playing recording: {e}")
            return False

if __name__ == "__main__":
    # Example usage
    if len(sys.argv) < 2:
        print("Usage: python vishing.py <command> [arguments]")
        print("Commands:")
        print("  test - Test voice generation")
        print("  call <phone_number> - Make a test call")
        print("  campaign <target_list.txt> - Launch a campaign")
        sys.exit(1)
        
    command = sys.argv[1]
    
    # Load Twilio credentials from environment variables
    TWILIO_SID = os.environ.get('TWILIO_SID')
    TWILIO_TOKEN = os.environ.get('TWILIO_TOKEN')
    TWILIO_PHONE = os.environ.get('TWILIO_PHONE')
    
    if not all([TWILIO_SID, TWILIO_TOKEN, TWILIO_PHONE]):
        print("Twilio credentials not configured.")
        sys.exit(1)
        
    vm = VishingModule(TWILIO_SID, TWILIO_TOKEN, TWILIO_PHONE)
    
    if command == 'test':
        # Test voice generation
        script = vm.generate_voice_script()
        print(f"Generated script: {script['title']}")
        print(f"Content: {script['content']}")
        
        recording_file = vm.create_voice_recording(script['content'])
        if recording_file:
            print(f"Recording created: {recording_file}")
            print("Playing recording...")
            vm.play_recording(recording_file)
            
    elif command == 'call':
        if len(sys.argv) < 3:
            print("Usage: python vishing.py call <phone_number>")
            sys.exit(1)
            
        phone_number = sys.argv[2]
        vm.launch_campaign([phone_number])
        
    elif command == 'campaign':
        if len(sys.argv) < 3:
            print("Usage: python vishing.py campaign <target_list.txt>")
            sys.exit(1)
            
        target_file = sys.argv[2]
        if not os.path.exists(target_file):
            print(f"Target list file not found: {target_file}")
            sys.exit(1)
            
        targets = []
        with open(target_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and line not in targets:
                    targets.append(line)
                    
        vm.launch_campaign(targets)
