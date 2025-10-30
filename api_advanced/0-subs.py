#!/usr/bin/python3
"""
Module for querying Reddit API to get number of subscribers for a subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Query the Reddit API and return the number of subscribers.

    Args:
        subreddit (str): The name of the subreddit

    Returns:
        int: Number of subscribers, or 0 if invalid subreddit
    """
    if not subreddit or not isinstance(subreddit, str):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'MyRedditScript/1.0 (by /u/YourUsername)'
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False,
            timeout=10
        )

        if response.status_code == 200:
            data = response.json()
            return data.get('data', {}).get('subscribers', 0)
        return 0
    except Exception:
        return 0
