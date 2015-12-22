# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from unittest import TestCase

from summarize.language import split_words, get_stopwords


class SplitWordsTestCase(TestCase):
    sample_sentence = ("But before they get to them, they have to go "
                       "past their mortal enemy — Mr. Boredom")

    @classmethod
    def setUpClass(cls):
        cls.stopwords = get_stopwords('english')

    def test_no_punctuation(self):
        words = split_words(self.sample_sentence, self.stopwords)
        self.assertTrue(all(word not in ',.—' for word in words))

    def test_no_stopwords(self):
        words = split_words(self.sample_sentence, self.stopwords)
        self.assertTrue(all(word not in self.stopwords for word in words))


class GetStopwordsTestCase(TestCase):
    def test_returns_non_empty_set(self):
        stopwords = get_stopwords('english')
        self.assertGreater(len(stopwords), 0)
