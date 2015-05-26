__author__ = 'kasi'

import matplotlib.pyplot as plt
from collections import OrderedDict

# calculates the frequency of words based on their length and plots a graph of the words.
class WordFrequencyCounter(object):

    characters_to_remove = ',.?!'

    def __init__(self, top_posts):
        self.top_posts = top_posts
        self.word_count = {}

    # calculates frequency in data collected.
    def get_frequency(self):

        for i in range(0, 30):
            self.word_count[i] = 0

        for post in self.top_posts:
            words = self.filter_message(post['data']['body'])

            for word in words:
                word_length = len(word)

                if word_length in self.word_count.keys():
                    self.word_count[word_length] += 1

        self.word_count = OrderedDict(sorted(self.word_count.items()))

        # create graph
        plt.bar(self.word_count.keys(), self.word_count.values(), alpha=0.4, align='center', label=self.word_count.keys())
        plt.ylabel('times used')
        plt.xlabel('letters in word')
        plt.savefig('frequency_piechart')

    # removes characters that are in the string characters to remove and new lines.
    def filter_message(self, post_message):

        return ''.join([character for character in post_message.replace('/n', '') if character not in self.characters_to_remove]).split()