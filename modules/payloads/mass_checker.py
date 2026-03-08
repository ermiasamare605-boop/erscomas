#!/usr/bin/env python3
"""
Mass Vulnerability Checker Module
This module provides functionality to scan multiple targets for common
social media platform vulnerabilities in bulk.
"""

import os
import logging
import csv
import json
from datetime import datetime
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class MassVulnerabilityChecker:
    """
    Class to check multiple targets for vulnerabilities
    """
    
    def __init__(self):
        self.targets = []
        self.results = []
        self.vulnerability_types = [
            'xss',
            'sql_injection',
            'csrf',
            'open_redirect',
            'insecure_headers',
            'weak_password'
        ]
        
    def add_targets_from_file(self, filename: str) -> int:
        """
        Add targets from a file
        
        Args:
            filename (str): File containing targets
            
        Returns:
            int: Number of targets added
        """
        logger.info(f"Reading targets from file: {filename}")
        
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                if filename.endswith('.csv'):
                    reader = csv.DictReader(f)
                    self.targets.extend([row for row in reader])
                elif filename.endswith('.json'):
                    data = json.load(f)
                    self.targets.extend(data)
                else:
                    # Simple list of URLs
                    self.targets.extend([{'url': line.strip()} for line in f if line.strip()])
                    
            logger.info(f"Successfully added {len(self.targets)} targets")
            return len(self.targets)
        except Exception as e:
            logger.error(f"Error reading targets from {filename}: {e}")
            return 0
            
    def add_target(self, target: dict) -> None:
        """
        Add a single target
        
        Args:
            target (dict): Target information
        """
        self.targets.append(target)
        logger.debug(f"Target added: {target}")
        
    def check_vulnerability(self, target: dict, vuln_type: str) -> dict:
        """
        Check target for specific vulnerability type
        
        Args:
            target (dict): Target information
            vuln_type (str): Vulnerability type to check
            
        Returns:
            dict: Check results
        """
        logger.debug(f"Checking {vuln_type} for target: {target.get('url', 'unknown')}")
        
        try:
            # Simulate vulnerability checking
            result = {
                'vulnerability': vuln_type,
                'detected': False,
                'severity': 'low',
                'description': '',
                'timestamp': datetime.now().isoformat()
            }
            
            # Randomly detect vulnerabilities for testing purposes
            import random
            detected = random.choice([True, False])
            result['detected'] = detected
            
            if detected:
                severities = ['low', 'medium', 'high', 'critical']
                result['severity'] = random.choice(severities)
                
                descriptions = {
                    'xss': 'Cross-site scripting vulnerability detected',
                    'sql_injection': 'SQL injection vulnerability detected',
                    'csrf': 'CSRF vulnerability detected',
                    'open_redirect': 'Open redirect vulnerability detected',
                    'insecure_headers': 'Insecure HTTP headers detected',
                    'weak_password': 'Weak password policy detected'
                }
                
                result['description'] = descriptions.get(vuln_type, 'Vulnerability detected')
                
            logger.debug(f"Vulnerability check completed: {vuln_type}")
            return result
        except Exception as e:
            logger.error(f"Error checking {vuln_type} for {target.get('url')}: {e}")
            return {
                'vulnerability': vuln_type,
                'detected': False,
                'severity': 'unknown',
                'description': f'Error: {e}',
                'timestamp': datetime.now().isoformat()
            }
            
    def scan_target(self, target: dict) -> dict:
        """
        Scan a single target for all vulnerability types
        
        Args:
            target (dict): Target information
            
        Returns:
            dict: Scan results
        """
        logger.info(f"Scanning target: {target.get('url')}")
        
        scan_result = {
            'target': target,
            'scanned_at': datetime.now().isoformat(),
            'vulnerabilities': []
        }
        
        for vuln_type in self.vulnerability_types:
            vuln_result = self.check_vulnerability(target, vuln_type)
            scan_result['vulnerabilities'].append(vuln_result)
            
        # Calculate overall score
        scan_result['total_vulnerabilities'] = sum(1 for vuln in scan_result['vulnerabilities'] if vuln['detected'])
        scan_result['highest_severity'] = max((vuln['severity'] for vuln in scan_result['vulnerabilities'] if vuln['detected']), default='none')
        
        logger.info(f"Target scan completed: {target.get('url')} - {scan_result['total_vulnerabilities']} vulnerabilities found")
        return scan_result
            
    def scan_all_targets(self) -> List[dict]:
        """
        Scan all targets
        
        Returns:
            list: All scan results
        """
        logger.info(f"Starting mass scan on {len(self.targets)} targets")
        
        self.results = []
        
        for i, target in enumerate(self.targets):
            logger.info(f"Scanning target {i+1}/{len(self.targets)}: {target.get('url')}")
            result = self.scan_target(target)
            self.results.append(result)
            
            # Add delay between scans to avoid detection
            import time
            time.sleep(0.5)
            
        logger.info("Mass scan completed")
        return self.results
            
    def get_statistics(self) -> dict:
        """
        Get scan statistics
        
        Returns:
            dict: Statistics about the scan
        """
        stats = {
            'total_targets': len(self.targets),
            'scanned_targets': len(self.results),
            'targets_with_vulnerabilities': sum(1 for res in self.results if res['total_vulnerabilities'] > 0),
            'total_vulnerabilities': sum(res['total_vulnerabilities'] for res in self.results),
            'vulnerabilities_by_severity': {
                'critical': 0,
                'high': 0,
                'medium': 0,
                'low': 0
            },
            'vulnerabilities_by_type': {vuln: 0 for vuln in self.vulnerability_types}
        }
        
        for res in self.results:
            for vuln in res['vulnerabilities']:
                if vuln['detected']:
                    if vuln['severity'] in stats['vulnerabilities_by_severity']:
                        stats['vulnerabilities_by_severity'][vuln['severity']] += 1
                    if vuln['vulnerability'] in stats['vulnerabilities_by_type']:
                        stats['vulnerabilities_by_type'][vuln['vulnerability']] += 1
                        
        return stats
            
    def save_results(self, filename: str) -> bool:
        """
        Save scan results to file
        
        Args:
            filename (str): Output filename
            
        Returns:
            bool: Success status
        """
        logger.info(f"Saving scan results to: {filename}")
        
        try:
            if filename.endswith('.csv'):
                self._save_to_csv(filename)
            elif filename.endswith('.json'):
                self._save_to_json(filename)
            else:
                self._save_to_text(filename)
                
            logger.info("Results saved successfully")
            return True
        except Exception as e:
            logger.error(f"Error saving results: {e}")
            return False
            
    def _save_to_json(self, filename: str) -> None:
        """Save results to JSON file"""
        data = {
            'scan_info': {
                'timestamp': datetime.now().isoformat(),
                'statistics': self.get_statistics()
            },
            'results': self.results
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False, default=str)
            
    def _save_to_csv(self, filename: str) -> None:
        """Save results to CSV file"""
        fieldnames = [
            'url',
            'scanned_at',
            'total_vulnerabilities',
            'highest_severity',
            'xss',
            'sql_injection',
            'csrf',
            'open_redirect',
            'insecure_headers',
            'weak_password'
        ]
        
        with open(filename, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            
            for res in self.results:
                row = {
                    'url': res['target'].get('url', ''),
                    'scanned_at': res['scanned_at'],
                    'total_vulnerabilities': res['total_vulnerabilities'],
                    'highest_severity': res['highest_severity']
                }
                
                for vuln in res['vulnerabilities']:
                    row[vuln['vulnerability']] = 'Yes' if vuln['detected'] else 'No'
                    
                writer.writerow(row)
                
    def _save_to_text(self, filename: str) -> None:
        """Save results to text file"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("="*80 + "\n")
            f.write("MASS VULNERABILITY SCAN REPORT\n")
            f.write("="*80 + "\n\n")
            
            stats = self.get_statistics()
            f.write("SCAN STATISTICS:\n")
            f.write("-"*80 + "\n")
            for key, value in stats.items():
                if isinstance(value, dict):
                    f.write(f"{key.upper()}:\n")
                    for k, v in value.items():
                        f.write(f"  {k}: {v}\n")
                else:
                    f.write(f"{key.replace('_', ' ').upper()}: {value}\n")
                    
            f.write("\n" + "-"*80 + "\n\n")
            f.write("DETAILED RESULTS:\n")
            f.write("-"*80 + "\n\n")
            
            for i, res in enumerate(self.results):
                f.write(f"Target {i+1}: {res['target'].get('url')}\n")
                f.write(f"Scanned at: {res['scanned_at']}\n")
                f.write(f"Total vulnerabilities: {res['total_vulnerabilities']}\n")
                f.write(f"Highest severity: {res['highest_severity']}\n")
                
                if res['total_vulnerabilities'] > 0:
                    f.write("Vulnerabilities:\n")
                    for vuln in res['vulnerabilities']:
                        if vuln['detected']:
                            f.write(f"  - {vuln['vulnerability']} ({vuln['severity']}): {vuln['description']}\n")
                        
                f.write("\n" + "-"*50 + "\n\n")
                
    def display_results(self) -> None:
        """Display results in console"""
        stats = self.get_statistics()
        
        print("="*80)
        print("MASS VULNERABILITY SCAN REPORT")
        print("="*80)
        print()
        
        print("SCAN STATISTICS:")
        print("-"*80)
        for key, value in stats.items():
            if isinstance(value, dict):
                print(f"{key.upper()}:")
                for k, v in value.items():
                    print(f"  {k}: {v}")
            else:
                print(f"{key.replace('_', ' ').upper()}: {value}")
                
        print()
        print("DETAILED RESULTS:")
        print("-"*80)
        
        for i, res in enumerate(self.results):
            print()
            print(f"Target {i+1}: {res['target'].get('url')}")
            print(f"Scanned at: {res['scanned_at']}")
            print(f"Total vulnerabilities: {res['total_vulnerabilities']}")
            print(f"Highest severity: {res['highest_severity']}")
            
            if res['total_vulnerabilities'] > 0:
                print("Vulnerabilities:")
                for vuln in res['vulnerabilities']:
                    if vuln['detected']:
                        print(f"  - {vuln['vulnerability']} ({vuln['severity']}): {vuln['description']}")


# Module entry point for testing
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Mass Vulnerability Checker')
    parser.add_argument('targets', help='File containing targets (txt, csv, or json)')
    parser.add_argument('-o', '--output', help='Output file for results')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    parser.add_argument('--types', nargs='+', help='Vulnerability types to check')
    
    args = parser.parse_args()
    
    checker = MassVulnerabilityChecker()
    
    if args.verbose:
        logger.setLevel(logging.DEBUG)
        
    if args.types:
        # Filter valid vulnerability types
        valid_types = [vuln for vuln in args.types if vuln in checker.vulnerability_types]
        if valid_types:
            checker.vulnerability_types = valid_types
        else:
            print("Invalid vulnerability types. Using defaults.")
            
    # Add targets from file
    count = checker.add_targets_from_file(args.targets)
    
    if count > 0:
        print(f"Loaded {count} targets")
        
        # Start scan
        print("Starting mass vulnerability scan...")
        results = checker.scan_all_targets()
        
        # Display results
        checker.display_results()
        
        # Save to file if specified
        if args.output:
            checker.save_results(args.output)
            print(f"\nResults saved to {args.output}")
    else:
        print("No valid targets found")
