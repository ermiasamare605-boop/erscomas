#!/usr/bin/env python3
"""
Phishing Platform Module
A comprehensive platform for managing phishing campaigns, templates, and payloads
"""

import os
import sys
import logging
import smtplib
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class PhishPlatform:
    """
    Main class for the phishing platform
    """
    
    def __init__(self):
        """Initialize the phishing platform"""
        self.templates_dir = 'phish_templates'
        self.payloads_dir = 'payloads'
        self.tracking_dir = 'tracks'
        
        # Ensure directories exist
        os.makedirs(self.templates_dir, exist_ok=True)
        os.makedirs(self.payloads_dir, exist_ok=True)
        os.makedirs(self.tracking_dir, exist_ok=True)
        
        # SMTP configuration (default values)
        self.smtp_server = 'localhost'
        self.smtp_port = 25
        self.smtp_username = None
        self.smtp_password = None
        self.use_tls = False
        
        logger.info("Phish Platform initialized")
    
    def configure_smtp(self, server, port=25, username=None, password=None, use_tls=False):
        """
        Configure SMTP settings for sending phishing emails
        
        Args:
            server (str): SMTP server address
            port (int): SMTP port
            username (str): SMTP username (optional)
            password (str): SMTP password (optional)
            use_tls (bool): Whether to use TLS encryption
        """
        self.smtp_server = server
        self.smtp_port = port
        self.smtp_username = username
        self.smtp_password = password
        self.use_tls = use_tls
        logger.info(f"SMTP configured: {server}:{port}")
    
    def create_phishing_email(self, sender, recipient, subject, body, html_body=None, attachments=None):
        """
        Create a phishing email with optional HTML content and attachments
        
        Args:
            sender (str): Sender email address
            recipient (str): Recipient email address
            subject (str): Email subject
            body (str): Plain text body
            html_body (str): HTML body (optional)
            attachments (list): List of file paths to attach (optional)
            
        Returns:
            MIMEMultipart: Email message object
        """
        msg = MIMEMultipart('alternative')
        msg['From'] = sender
        msg['To'] = recipient
        msg['Subject'] = subject
        
        # Add plain text part
        text_part = MIMEText(body, 'plain')
        msg.attach(text_part)
        
        # Add HTML part if provided
        if html_body:
            html_part = MIMEText(html_body, 'html')
            msg.attach(html_part)
        
        # Add attachments if provided
        if attachments:
            for file_path in attachments:
                if os.path.exists(file_path):
                    with open(file_path, 'rb') as f:
                        filename = os.path.basename(file_path)
                        part = MIMEImage(f.read(), name=filename)
                        part.add_header('Content-Disposition', f'attachment; filename="{filename}"')
                        msg.attach(part)
        
        logger.info(f"Email created: {sender} -> {recipient}")
        return msg
    
    def send_email(self, msg):
        """
        Send an email using the configured SMTP settings
        
        Args:
            msg (MIMEMultipart): Email message to send
            
        Returns:
            bool: Success status
        """
        try:
            # Connect to SMTP server
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            
            if self.use_tls:
                server.starttls()
            
            # Login if credentials provided
            if self.smtp_username and self.smtp_password:
                server.login(self.smtp_username, self.smtp_password)
            
            # Send email
            server.send_message(msg)
            server.quit()
            
            logger.info("Email sent successfully")
            return True
            
        except Exception as e:
            logger.error(f"Failed to send email: {str(e)}")
            return False
    
    def load_template(self, template_name):
        """
        Load a phishing template from file
        
        Args:
            template_name (str): Name of the template file (without extension)
            
        Returns:
            dict: Template content
        """
        template_path = os.path.join(self.templates_dir, f"{template_name}.json")
        
        if os.path.exists(template_path):
            try:
                with open(template_path, 'r', encoding='utf-8') as f:
                    template = json.load(f)
                logger.info(f"Template loaded: {template_name}")
                return template
            except Exception as e:
                logger.error(f"Failed to load template: {str(e)}")
        else:
            logger.error(f"Template not found: {template_name}")
        
        return None
    
    def save_template(self, template_name, template_data):
        """
        Save a phishing template to file
        
        Args:
            template_name (str): Name of the template file (without extension)
            template_data (dict): Template content
            
        Returns:
            bool: Success status
        """
        template_path = os.path.join(self.templates_dir, f"{template_name}.json")
        
        try:
            with open(template_path, 'w', encoding='utf-8') as f:
                json.dump(template_data, f, indent=2)
            logger.info(f"Template saved: {template_name}")
            return True
        except Exception as e:
            logger.error(f"Failed to save template: {str(e)}")
            return False


if __name__ == "__main__":
    # Example usage
    platform = PhishPlatform()
    
    # Configure SMTP (example settings)
    platform.configure_smtp('smtp.gmail.com', 587, 'your-email@gmail.com', 'your-password', use_tls=True)
    
    # Create a simple phishing email
    msg = platform.create_phishing_email(
        sender='noreply@company.com',
        recipient='target@example.com',
        subject='Password Reset Required',
        body='Please reset your password immediately',
        html_body='<html><body><h1>Password Reset</h1><p>Please click <a href="http://fake-login.com">here</a> to reset your password.</p></body></html>'
    )
    
    # Send the email
    if platform.send_email(msg):
        print("Email sent successfully!")
    else:
        print("Failed to send email.")
