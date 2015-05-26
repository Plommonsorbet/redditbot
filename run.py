__author__ = 'kasi'

from reddit import client

posts = client.get_posts('holdmynip')

posts.get_frequency()

