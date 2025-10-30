#!/usr/bin/python3
"""Module to query Reddit API for hot posts."""

import requests


def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit: The name of the subreddit to query

    Returns:
        None
    """
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': 'python:subreddit.posts:v1.0'
    }
    params = {'limit': 10}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

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
            print(None)

    except Exception:
        print(None)
