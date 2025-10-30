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
        'User-Agent': 'Mozilla/5.0'
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
            
            # Check if we have valid data structure
            if 'data' not in data or 'children' not in data.get('data', {}):
                print(None)
                return
            
            children = data['data']['children']
            
            if len(children) == 0:
                print(None)
                return

            for child in children:
                if 'data' in child and 'title' in child['data']:
                    print(child['data']['title'])
        else:
            print(None)

    except Exception:
        print(None)
