# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import nltk
from unittest import TestCase

from summarize.utils import get_words, get_stopwords


class GetWordsTestCase(TestCase):
    sample_sentence = ("But before they get to them, they have to go "
                       "past their mortal enemy — Mr. Boredom")

    @classmethod
    def setUpClass(cls):
        nltk.download(['stopwords'])
        cls.stopwords = get_stopwords('english')

    def test_no_punctuation(self):
        words = get_words(self.sample_sentence, self.stopwords)
        self.assertTrue(all(word not in ',.—' for word in words))

    def test_no_stopwords(self):
        words = get_words(self.sample_sentence, self.stopwords)
        self.assertTrue(all(word not in self.stopwords for word in words))


class GetStopwordsTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        nltk.download(['stopwords'])

    def test_returns_non_empty_set(self):
        stopwords = get_stopwords('english')
        self.assertGreater(len(stopwords), 0)
