#!/usr/bin/python3
"""
ALX top_ten subreddit checker
"""
import requests


def top_ten(subreddit):
    """
    Queries Reddit API and prints titles of first 10 hot posts.
    Prints None if subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Python:topten:v1.0 (by /u/yourusername)"}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            
            for post in posts:
                title = post.get('data', {}).get('title', '')
                print(title)
        else:
            print(None)
    except Exception:
        print(None)


if __name__ == "__main__":
    top_ten("python")
