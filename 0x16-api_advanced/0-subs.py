#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """Returns total subscribers  for a specified subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    resp = requests.get(url, allow_redirects=False)
    if resp.status_code == 404:
        return 0
    subscribers = (resp.json().get("data")).get("subscribers")
    return subscribers
