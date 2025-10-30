#!/usr/bin/python3
"""
Module that queries the Reddit API and prints the titles
of the first 10 hot posts for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query
        
    Returns:
        None: Prints the titles or None if invalid subreddit
    """
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'python:subreddit.top.posts:v1.0 (by /u/yourusername)'
    }
    params = {'limit': 10}
    
    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )
        
        # Check if the request was successful and not redirected
        if response.status_code == 200:
            data = response.json()
            children = data.get('data', {}).get('children', [])
            
            if not children:
                print(None)
                return
            
            for child in children:
                title = child.get('data', {}).get('title')
                if title:
                    print(title)
        else:
            # Invalid subreddit, redirected, or error
            print(None)
            
    except Exception:
        # Any exception means invalid request
        print(None)
