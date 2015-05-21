__author__ = 'kasi'

from reddit import client

posts = client.get_posts()

posts.get_frequency()

