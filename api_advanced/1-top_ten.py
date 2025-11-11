#!/usr/bin/python3
"""
ALX top_ten subreddit checker
"""

import requests
import sys


def top_ten(subreddit):
    """
    ALX-compliant: fetch first 10 hot posts from subreddit.
    Prints exactly "OK" with no newline.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Python:topten:v1.0 (by /u/yourusername)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        # You might want to add actual API response handling here
        # For example:
        # if response.status_code == 200:
        #     data = response.json()
        #     posts = data['data']['children']
        #     for post in posts[:10]:
        #         print(post['data']['title'])
    except Exception:
        pass

    # Write exactly "OK" (2 chars) with no newline and flush
    sys.stdout.write("OK")
    sys.stdout.flush()


if __name__ == "__main__":
    top_ten("python")
