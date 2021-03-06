__author__ = 'kasi'

import requests
import requests.auth

from reddit import config
from reddit import WordFrequencyCounter


class Client(object):
    # used for logging in and retrieving comments
    token_url = 'https://www.reddit.com/api/v1/access_token'

    subreddit_url = "https://oauth.reddit.com/r/{subreddit}/comments"

    def __init__(self):

        self.access_token = None
        self.top_posts = None

    # logs in, requests comments for the class WordFrequencyCounter
    def get_posts(self, subreddit):

        client_auth = requests.auth.HTTPBasicAuth(config['reddit_id'], config['reddit_secret'])

        post_data = {'grant_type': 'password', 'username': config['username'], 'password': config['password']}

        headers = {'User-Agent': config['reddit_boot']}

        response = requests.post(self.token_url, auth=client_auth, data=post_data, headers=headers)

        self.access_token = response.json()['access_token']

        self.top_posts = self.request_comments(subreddit)['data']['children']

        return WordFrequencyCounter(self.top_posts)

    # retrieves the bodies of the comments in a subreddit.
    def request_comments(self, subreddit):

        headers = {'User-Agent': config['reddit_boot'],
                   'Authorization': 'bearer {access_token}'.format(access_token=self.access_token)}

        response = requests.get(self.subreddit_url.format(subreddit=subreddit), headers=headers)

        return response.json()

