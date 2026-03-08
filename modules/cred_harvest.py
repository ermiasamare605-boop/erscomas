#!/usr/bin/env python3
"""
Credential Harvesting Module with Form Grabber
This module provides functionality to harvest credentials from various sources
including web forms, login pages, and other authentication mechanisms.
"""

import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class FormGrabber:
    """
    Class to grab and analyze web forms from target URLs
    """
    
    def __init__(self):
        self.session = requests.Session()
        self.forms = []
    
    def grab_forms(self, url, headers=None):
        """
        Grab all forms from a given URL
        
        Args:
            url (str): Target URL to scan for forms
            headers (dict): Optional HTTP headers for the request
            
        Returns:
            list: List of form data dictionaries
        """
        try:
            if headers is None:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                }
            
            response = self.session.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            self.forms = []
            
            for form in soup.find_all('form'):
                form_data = self._extract_form_data(form, url)
                if form_data:
                    self.forms.append(form_data)
            
            logger.info(f"Found {len(self.forms)} forms on {url}")
            return self.forms
            
        except Exception as e:
            logger.error(f"Error grabbing forms from {url}: {e}")
            return []
    
    def _extract_form_data(self, form, base_url):
        """
        Extract detailed information from a single form
        
        Args:
            form (bs4.Tag): BeautifulSoup form tag
            base_url (str): Base URL for resolving relative paths
            
        Returns:
            dict: Form data dictionary
        """
        form_data = {
            'action': form.get('action'),
            'method': form.get('method', 'get'),
            'inputs': [],
            'name': form.get('name'),
            'id': form.get('id')
        }
        
        # Ensure action is string
        if not isinstance(form_data['action'], str):
            form_data['action'] = ''
        # Ensure method is string and lowercase
        if not isinstance(form_data['method'], str):
            form_data['method'] = 'get'
        else:
            form_data['method'] = form_data['method'].lower()
            
        # Resolve relative action URLs
        if form_data['action']:
            form_data['action'] = urljoin(base_url, form_data['action'])
        
        # Extract all form inputs
        for input_tag in form.find_all(['input', 'textarea', 'select']):
            input_data = self._extract_input_data(input_tag)
            if input_data:
                form_data['inputs'].append(input_data)
        
        return form_data
    
    def _extract_input_data(self, input_tag):
        """
        Extract input field information
        
        Args:
            input_tag (bs4.Tag): Input/textarea/select tag
            
        Returns:
            dict: Input field data
        """
        input_data = {
            'type': input_tag.get('type', 'text'),
            'name': input_tag.get('name'),
            'value': input_tag.get('value', ''),
            'id': input_tag.get('id'),
            'placeholder': input_tag.get('placeholder')
        }
        
        # Handle textarea
        if input_tag.name == 'textarea':
            input_data['type'] = 'textarea'
            input_data['value'] = input_tag.text.strip()
        
        # Handle select dropdowns
        if input_tag.name == 'select':
            input_data['type'] = 'select'
            input_data['options'] = []
            for option in input_tag.find_all('option'):
                input_data['options'].append({
                    'value': option.get('value'),
                    'text': option.text.strip(),
                    'selected': option.has_attr('selected')
                })
        
        return input_data
    
    def analyze_forms(self):
        """
        Analyze forms to identify potential credential fields
        
        Returns:
            list: Forms that appear to be login forms
        """
        login_forms = []
        
        for form in self.forms:
            if self._is_login_form(form):
                login_forms.append(form)
        
        logger.info(f"Identified {len(login_forms)} potential login forms")
        return login_forms
    
    def _is_login_form(self, form):
        """
        Determine if a form is likely a login form
        
        Args:
            form (dict): Form data dictionary
            
        Returns:
            bool: True if form appears to be a login form
        """
        # Look for keywords in form attributes or input fields
        login_keywords = ['login', 'logon', 'signin', 'signon', 'auth', 'credentials']
        
        # Check form attributes
        if form.get('name') and any(keyword in form['name'].lower() for keyword in login_keywords):
            return True
        
        if form.get('id') and any(keyword in form['id'].lower() for keyword in login_keywords):
            return True
        
        # Check input fields for username/password
        has_username = False
        has_password = False
        
        for input_field in form['inputs']:
            if input_field.get('name') or input_field.get('id') or input_field.get('placeholder'):
                field_text = ' '.join([
                    str(input_field.get('name', '')),
                    str(input_field.get('id', '')),
                    str(input_field.get('placeholder', ''))
                ]).lower()
                
                # Check for password fields
                if input_field['type'] == 'password':
                    has_password = True
                
                # Check for username/email fields
                if any(keyword in field_text for keyword in ['user', 'username', 'email', 'email', 'login']):
                    has_username = True
        
        return has_username and has_password
    
    def submit_form(self, form_data, payload):
        """
        Submit a form with the given payload
        
        Args:
            form_data (dict): Form data dictionary
            payload (dict): Data to submit
            
        Returns:
            requests.Response: Response object
        """
        try:
            url = form_data['action']
            method = form_data['method']
            
            # Build complete payload with form data
            complete_payload = {}
            for input_field in form_data['inputs']:
                if input_field.get('name'):
                    # Use provided value or default
                    if input_field['name'] in payload:
                        complete_payload[input_field['name']] = payload[input_field['name']]
                    elif input_field['value'] and input_field['type'] not in ['password', 'text', 'textarea']:
                        complete_payload[input_field['name']] = input_field['value']
            
            if method == 'post':
                response = self.session.post(url, data=complete_payload, timeout=10)
            else:
                response = self.session.get(url, params=complete_payload, timeout=10)
            
            logger.info(f"Form submitted to {url} (method: {method})")
            return response
            
        except Exception as e:
            logger.error(f"Error submitting form: {e}")
            return None


class CredentialHarvester:
    """
    Main class for harvesting credentials from various sources
    """
    
    def __init__(self):
        self.form_grabber = FormGrabber()
        self.harvested_credentials = []
    
    def harvest_from_url(self, url, credentials=None):
        """
        Harvest credentials from a specific URL
        
        Args:
            url (str): Target URL
            credentials (dict): Optional credentials to test (username/password)
            
        Returns:
            list: Harvested credentials
        """
        logger.info(f"Starting credential harvest from: {url}")
        
        # Grab and analyze forms
        forms = self.form_grabber.grab_forms(url)
        login_forms = self.form_grabber.analyze_forms()
        
        if not login_forms:
            logger.warning(f"No login forms found on {url}")
            return []
        
        # If credentials are provided, test them
        if credentials:
            for form in login_forms:
                logger.info(f"Testing credentials on form: {form.get('name', form.get('id', 'unknown'))}")
                response = self.form_grabber.submit_form(form, credentials)
                
                if response:
                    # Check if login was successful (simple heuristic)
                    login_success = self._check_login_success(response, url, credentials)
                    if login_success:
                        logger.info("Login successful!")
                        self.harvested_credentials.append({
                            'url': url,
                            'credentials': credentials,
                            'form': form
                        })
        
        return self.harvested_credentials
    
    def _check_login_success(self, response, original_url, credentials):
        """
        Check if login attempt was successful
        
        Args:
            response (requests.Response): Response from login attempt
            original_url (str): Original login URL
            credentials (dict): Credentials used
            
        Returns:
            bool: True if login appears to be successful
        """
        # Simple heuristic checks
        parsed_url = urlparse(original_url)
        
        # Check if we're redirected to a different page
        if response.url != original_url:
            return True
        
        # Check if login failure indicators are not present
        failure_indicators = [
            'invalid', 'incorrect', 'failed', 'error', 'denied',
            'wrong', 'authentication failed', 'login failed'
        ]
        
        response_text = response.text.lower()
        for indicator in failure_indicators:
            if indicator in response_text:
                return False
        
        # Check if we see the username in the response (indicates successful login)
        if 'username' in credentials and credentials['username'] in response_text:
            return True
        
        return False
    
    def get_harvested_credentials(self):
        """
        Get all harvested credentials
        
        Returns:
            list: List of harvested credentials
        """
        return self.harvested_credentials
    
    def save_credentials(self, filename):
        """
        Save harvested credentials to a file
        
        Args:
            filename (str): Output filename
        """
        try:
            import json
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.harvested_credentials, f, indent=2, ensure_ascii=False)
            logger.info(f"Credentials saved to {filename}")
        except Exception as e:
            logger.error(f"Error saving credentials: {e}")


# Module entry point for testing
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Credential Harvesting Module')
    parser.add_argument('url', help='Target URL to scan for credentials')
    parser.add_argument('-u', '--username', help='Username to test')
    parser.add_argument('-p', '--password', help='Password to test')
    parser.add_argument('-o', '--output', help='Output file to save credentials')
    
    args = parser.parse_args()
    
    harvester = CredentialHarvester()
    
    if args.username and args.password:
        credentials = {
            'username': args.username,
            'password': args.password
        }
        harvested = harvester.harvest_from_url(args.url, credentials)
        
        if harvested:
            print(f"Successfully harvested {len(harvested)} credentials")
            if args.output:
                harvester.save_credentials(args.output)
        else:
            print("No credentials harvested")
    else:
        print("Scanning for login forms...")
        forms = harvester.form_grabber.grab_forms(args.url)
        login_forms = harvester.form_grabber.analyze_forms()
        print(f"Found {len(forms)} total forms, {len(login_forms)} potential login forms")
