#!/usr/bin/python3
"""
ALX top_ten subreddit checker
"""

import requests
import sys


def top_ten(subreddit):
    """
    Fetches and prints the titles of the first 10 hot posts in a subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Python:topten:v1.0 (by /u/yourusername)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            
            for i, post in enumerate(posts[:10], 1):
                title = post['data']['title']
                print("{}. {}".format(i, title))
        else:
            print("None")
            
    except Exception as e:
        print("None")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        top_ten(sys.argv[1])
    else:
        top_ten("python")
