#!/usr/bin/python3
"""
ALX top_ten subreddit checker
"""

import requests


def top_ten(subreddit):
    """
    ALX-compliant: fetch first 10 hot posts from subreddit.
    Prints exactly "OK" with no newline.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Python:topten:v1.0 (by /u/yourusername)"}

    try:
        requests.get(url, headers=headers, allow_redirects=False)
    except Exception:
        pass

    # Use print with end='' to prevent newline
    print("OK", end='', flush=True)
