#!/usr/bin/python3
"""Module to query Reddit API for top 10 hot posts"""
import requests


def top_ten(subreddit):
    """Prints titles of first 10 hot posts for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'python:top_ten:v1.0 (by /u/Jobealieu)'}
    params = {'limit': 10}
    
    try:
        response = requests.get(url, headers=headers, params=params,
                              allow_redirects=False, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            
            for post in posts:
                print(post.get('data', {}).get('title'))
        else:
            print(None)
    except Exception:
        print(None)
