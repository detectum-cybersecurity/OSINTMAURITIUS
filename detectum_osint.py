#!/usr/bin/env python3
"""
Detectum-OSINT - Advanced OSINT Investigation Tool
Developed by Vishal Coodye for Detectum Cybersecurity, Republic of Mauritius
Copyright (c) 2025 Detectum Cybersecurity. All rights reserved.

A powerful tool for collecting comprehensive dossiers on individuals by username,
checking thousands of websites and gathering available information from web pages.
No API keys required - designed for cybersecurity professionals and investigators.
"""

import argparse
import asyncio
import aiohttp
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Set
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DetectumOSINT:
    """
    Main Detectum-OSINT investigation engine
    """
    
    def __init__(self):
        self.session = None
        self.results = {}
        self.sites_data = self._load_sites_data()
        self.headers = {
            'User-Agent': 'Detectum-OSINT/1.0 (Cybersecurity Investigation Tool)'
        }
        
    def _load_sites_data(self) -> Dict:
        """Load the sites database"""
        sites_file = Path(__file__).parent / "data" / "sites.json"
        if sites_file.exists():
            with open(sites_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    async def _create_session(self):
        """Create aiohttp session with proper configuration"""
        timeout = aiohttp.ClientTimeout(total=30)
        connector = aiohttp.TCPConnector(limit=100, limit_per_host=10)
        self.session = aiohttp.ClientSession(
            timeout=timeout,
            connector=connector,
            headers=self.headers
        )
    
    async def _close_session(self):
        """Close aiohttp session"""
        if self.session:
            await self.session.close()
    
    async def check_username(self, username: str, site_info: Dict) -> Dict:
        """
        Check if username exists on a specific site
        """
        try:
            url = site_info['url'].format(account=username)
            
            async with self.session.get(url, allow_redirects=True) as response:
                if response.status == 200:
                    content = await response.text()
                    
                    # Check for various indicators of account existence
                    exists = False
                    error_type = None
                    
                    # Check for common "not found" patterns
                    not_found_patterns = [
                        'not found', 'doesn\'t exist', 'user not found',
                        'profile not found', 'no such user', 'user doesn\'t exist'
                    ]
                    
                    # Check for common "exists" patterns
                    exists_patterns = [
                        'profile', 'user profile', 'member since',
                        'joined', 'followers', 'following'
                    ]
                    
                    content_lower = content.lower()
                    
                    # Check if account exists
                    for pattern in exists_patterns:
                        if pattern in content_lower:
                            exists = True
                            break
                    
                    # Check if account doesn't exist
                    for pattern in not_found_patterns:
                        if pattern in content_lower:
                            exists = False
                            error_type = 'Not Found'
                            break
                    
                    return {
                        'exists': exists,
                        'url': url,
                        'status_code': response.status,
                        'error_type': error_type,
                        'timestamp': datetime.now().isoformat()
                    }
                    
        except Exception as e:
            return {
                'exists': False,
                'url': site_info.get('url', ''),
                'error_type': str(e),
                'timestamp': datetime.now().isoformat()
            }
    
    async def investigate_username(self, username: str, sites: Optional[List[str]] = None) -> Dict:
        """
        Main investigation method for a username
        """
        await self._create_session()
        
        try:
            # Filter sites if specified
            if sites:
                sites_to_check = {k: v for k, v in self.sites_data.items() if k in sites}
            else:
                # Use top 500 most popular sites by default
                sites_to_check = dict(list(self.sites_data.items())[:500])
            
            logger.info(f"Starting investigation for username: {username}")
            logger.info(f"Checking {len(sites_to_check)} sites...")
            
            tasks = []
            for site_name, site_info in sites_to_check.items():
                task = self.check_username(username, site_info)
                tasks.append((site_name, task))
            
            # Execute all checks concurrently
            results = {}
            for site_name, task in tasks:
                try:
                    result = await task
                    results[site_name] = result
                    
                    if result['exists']:
                        logger.info(f"✅ Found: {username} on {site_name}")
                    else:
                        logger.debug(f"❌ Not found: {username} on {site_name}")
                        
                except Exception as e:
                    logger.error(f"Error checking {site_name}: {e}")
                    results[site_name] = {
                        'exists': False,
                        'error_type': str(e),
                        'timestamp': datetime.now().isoformat()
                    }
            
            # Calculate statistics
            found_sites = [site for site, result in results.items() if result.get('exists', False)]
            total_checked = len(results)
            
            investigation_summary = {
                'username': username,
                'investigation_date': datetime.now().isoformat(),
                'total_sites_checked': total_checked,
                'accounts_found': len(found_sites),
                'success_rate': f"{(len(found_sites) / total_checked * 100):.2f}%" if total_checked > 0 else "0%",
                'found_sites': found_sites,
                'detailed_results': results
            }
            
            return investigation_summary
            
        finally:
            await self._close_session()
    
    def generate_report(self, results: Dict, output_format: str = 'json') -> str:
        """
        Generate investigation report in specified format
        """
        if output_format == 'json':
            return json.dumps(results, indent=2, ensure_ascii=False)
        elif output_format == 'txt':
            report = []
            report.append("=" * 60)
            report.append("DETECTUM-OSINT INVESTIGATION REPORT")
            report.append("=" * 60)
            report.append(f"Username: {results['username']}")
            report.append(f"Investigation Date: {results['investigation_date']}")
            report.append(f"Total Sites Checked: {results['total_sites_checked']}")
            report.append(f"Accounts Found: {results['accounts_found']}")
            report.append(f"Success Rate: {results['success_rate']}")
            report.append("")
            report.append("ACCOUNTS FOUND:")
            report.append("-" * 30)
            
            for site in results['found_sites']:
                report.append(f"✅ {site}")
            
            report.append("")
            report.append("DETAILED RESULTS:")
            report.append("-" * 30)
            
            for site, result in results['detailed_results'].items():
                status = "✅ FOUND" if result.get('exists') else "❌ NOT FOUND"
                report.append(f"{site}: {status}")
                if result.get('url'):
                    report.append(f"  URL: {result['url']}")
                if result.get('error_type'):
                    report.append(f"  Error: {result['error_type']}")
                report.append("")
            
            return "\n".join(report)
        else:
            raise ValueError(f"Unsupported output format: {output_format}")

def main():
    """
    Main CLI interface for Detectum-OSINT
    """
    parser = argparse.ArgumentParser(
        description="Detectum-OSINT - Advanced OSINT Investigation Tool",
        epilog="Developed by Vishal Coodye for Detectum Cybersecurity, Republic of Mauritius"
    )
    
    parser.add_argument(
        'username',
        help='Username to investigate'
    )
    
    parser.add_argument(
        '-s', '--sites',
        nargs='+',
        help='Specific sites to check (default: top 500 popular sites)'
    )
    
    parser.add_argument(
        '-o', '--output',
        choices=['json', 'txt'],
        default='json',
        help='Output format (default: json)'
    )
    
    parser.add_argument(
        '-f', '--output-file',
        help='Output file path (if not specified, prints to stdout)'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose logging'
    )
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Display banner
    print("=" * 70)
    print("🕵️‍♂️  DETECTUM-OSINT - Advanced OSINT Investigation Tool")
    print("=" * 70)
    print("Developed by Vishal Coodye for Detectum Cybersecurity")
    print("Republic of Mauritius | Professional Cybersecurity Solutions")
    print("=" * 70)
    print()
    
    # Initialize tool
    tool = DetectumOSINT()
    
    try:
        # Run investigation
        print(f"🔍 Starting investigation for username: {args.username}")
        print(f"⏱️  This may take several minutes depending on the number of sites...")
        print()
        
        # Run async investigation
        loop = asyncio.get_event_loop()
        results = loop.run_until_complete(
            tool.investigate_username(args.username, args.sites)
        )
        
        # Generate report
        report = tool.generate_report(results, args.output)
        
        # Output results
        if args.output_file:
            with open(args.output_file, 'w', encoding='utf-8') as f:
                f.write(report)
            print(f"📄 Report saved to: {args.output_file}")
        else:
            print("📊 INVESTIGATION RESULTS:")
            print("=" * 50)
            print(report)
        
        # Summary
        print()
        print("=" * 50)
        print(f"🎯 Investigation completed for: {args.username}")
        print(f"📈 Found {results['accounts_found']} accounts out of {results['total_sites_checked']} sites checked")
        print(f"📊 Success rate: {results['success_rate']}")
        print("=" * 50)
        
    except KeyboardInterrupt:
        print("\n⚠️  Investigation interrupted by user")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Investigation failed: {e}")
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
