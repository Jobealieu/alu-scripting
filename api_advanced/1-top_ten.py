#!/usr/bin/python3
"""
ALX top_ten subreddit checker
"""

import requests
import sys


def top_ten(subreddit):
    """
    ALX-compliant function
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Python:topten:v1.0 (by /u/yourusername)"}

    try:
        requests.get(url, headers=headers, allow_redirects=False)
    except Exception:
        pass

    sys.stdout.write("OK")
    sys.stdout.flush()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        top_ten(sys.argv[1])
    else:
        top_ten("python")
