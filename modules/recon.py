#!/usr/bin/env python3
"""
Reconnaissance Module with Social Media Scraping
This module provides functionality to gather information from various social media
platforms and online sources for reconnaissance purposes.
"""

import logging
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class SocialMediaRecon:
    """
    Class to perform social media reconnaissance
    """
    
    def __init__(self):
        self.instaloader = None
        self._initialize_instaloader()
    
    def _initialize_instaloader(self):
        """
        Initialize Instaloader if available
        """
        try:
            import instaloader
            self.instaloader = instaloader.Instaloader()
            self._instaloader_module = instaloader
            logger.info("Instaloader initialized successfully")
        except ImportError:
            logger.warning("Instaloader library not found. Instagram functionality will be limited.")
            logger.warning("Install with: pip install instaloader")
            self.instaloader = None
            self._instaloader_module = None
    
    def scrape_instagram_profile(self, username: str) -> Optional[Dict]:
        """
        Scrape Instagram profile information
        
        Args:
            username (str): Instagram username to scrape
            
        Returns:
            dict: Profile information or None if failed
        """
        if not self.instaloader or not self._instaloader_module:
            logger.error("Instaloader not initialized. Cannot scrape Instagram.")
            return None
        
        try:
            logger.info(f"Scraping Instagram profile: {username}")
            
            # Fetch profile
            profile = self._instaloader_module.Profile.from_username(self.instaloader.context, username)
            
            # Extract profile information
            profile_data = {
                'username': profile.username,
                'full_name': profile.full_name,
                'biography': profile.biography,
                'followers': profile.followers,
                'following': profile.followees,
                'posts': profile.mediacount,
                'is_private': profile.is_private,
                'external_url': profile.external_url,
                'profile_pic_url': profile.profile_pic_url
            }
            
            logger.info(f"Successfully scraped profile: {username}")
            return profile_data
            
        except Exception as e:
            logger.error(f"Error scraping Instagram profile {username}: {e}")
            return None
    
    def scrape_instagram_posts(self, username: str, max_posts: int = 10) -> List[Dict]:
        """
        Scrape recent Instagram posts
        
        Args:
            username (str): Instagram username
            max_posts (int): Maximum number of posts to scrape
            
        Returns:
            list: List of post information
        """
        if not self.instaloader or not self._instaloader_module:
            logger.error("Instaloader not initialized. Cannot scrape Instagram posts.")
            return []
        
        try:
            logger.info(f"Scraping Instagram posts for: {username} (max: {max_posts})")
            
            profile = self._instaloader_module.Profile.from_username(self.instaloader.context, username)
            posts = []
            
            for i, post in enumerate(profile.get_posts()):
                if i >= max_posts:
                    break
                
                post_data = {
                    'shortcode': post.shortcode,
                    'caption': post.caption,
                    'likes': post.likes,
                    'comments': post.comments,
                    'timestamp': post.date_utc.isoformat(),
                    'is_video': post.is_video,
                    'video_view_count': post.video_view_count if post.is_video else None
                }
                
                posts.append(post_data)
            
            logger.info(f"Successfully scraped {len(posts)} posts from {username}")
            return posts
            
        except Exception as e:
            logger.error(f"Error scraping Instagram posts for {username}: {e}")
            return []


class Reconnaissance:
    """
    Main reconnaissance class providing various information gathering methods
    """
    
    def __init__(self):
        self.social_media = SocialMediaRecon()
    
    def gather_target_info(self, target: str) -> Dict:
        """
        Gather comprehensive information about a target
        
        Args:
            target (str): Target identifier (username, email, etc.)
            
        Returns:
            dict: Comprehensive target information
        """
        logger.info(f"Starting reconnaissance on target: {target}")
        
        info = {
            'target': target,
            'social_media': {},
            'sources': []
        }
        
        # Scrape Instagram
        instagram_profile = self.social_media.scrape_instagram_profile(target)
        if instagram_profile:
            info['social_media']['instagram'] = instagram_profile
            info['sources'].append('instagram')
            
            # Get recent posts
            instagram_posts = self.social_media.scrape_instagram_posts(target, 5)
            info['social_media']['instagram']['recent_posts'] = instagram_posts
        
        logger.info(f"Reconnaissance completed for target: {target}")
        return info


# Module entry point for testing
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Reconnaissance Module')
    parser.add_argument('target', help='Target username or identifier to recon')
    parser.add_argument('-o', '--output', help='Output file to save reconnaissance results')
    
    args = parser.parse_args()
    
    recon = Reconnaissance()
    results = recon.gather_target_info(args.target)
    
    print(f"\n=== Reconnaissance Results for {args.target} ===")
    print(f"\nSources: {', '.join(results['sources'])}")
    
    if 'instagram' in results['social_media']:
        insta = results['social_media']['instagram']
        print(f"\nInstagram Profile:")
        print(f"  Username: {insta['username']}")
        print(f"  Full Name: {insta['full_name']}")
        print(f"  Followers: {insta['followers']}")
        print(f"  Following: {insta['following']}")
        print(f"  Posts: {insta['posts']}")
        print(f"  Private: {insta['is_private']}")
        if insta['biography']:
            print(f"  Bio: {insta['biography']}")
        
        if 'recent_posts' in insta and insta['recent_posts']:
            print(f"\nRecent Posts ({len(insta['recent_posts'])}):")
            for i, post in enumerate(insta['recent_posts']):
                print(f"  Post {i+1}:")
                print(f"    Likes: {post['likes']}")
                print(f"    Comments: {post['comments']}")
                print(f"    Date: {post['timestamp']}")
                if post['caption']:
                    print(f"    Caption: {post['caption'][:100]}...")
    
    if args.output:
        try:
            import json
            with open(args.output, 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=2, ensure_ascii=False)
            print(f"\nResults saved to {args.output}")
        except Exception as e:
            logger.error(f"Error saving results: {e}")
