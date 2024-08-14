#!/usr/bin/python3

import requests 
 

def number_of_subscribers(subreddit):
    """ Returns a number of subscribersfor a given subreddit. 
    Args:
      subreddit: The name of the subreddit.

    Returns:
      The number of subscribers for the subreddit. If the subreddit is invalid, 
      returns 0."""

    headers = { "User-Agent" : "your-username/0.1 "}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        print(response.status_code)
        
        # Set response encoding to utf-8 to handle special characters
        response.encoding = 'utf-8'

        if response.status_code == 200:
            data =response.json()
            print(data)
            return data.get('data',{}).get('subscribers', 0)
        elif response.status_code == 404:
            return 0
    except Exception as e:
        print("Exceptions: {}".format(e))
        return 0
