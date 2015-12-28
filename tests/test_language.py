# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from unittest import TestCase

from summarize.language import LanguageProcessor


class ExtractSignificantWordsTestCase(TestCase):
    sample_sentence = ("But before they get to them, they have to go "
                       "past their mortal enemy — Mr. Boredom")

    def setUp(self):
        self.processor = LanguageProcessor('english')

    def test_no_punctuation(self):
        words = self.processor.extract_significant_words(self.sample_sentence)
        self.assertTrue(all(word not in ',.—' for word in words))

    def test_no_stopwords(self):
        stopwords = self.processor.stopwords
        words = self.processor.extract_significant_words(self.sample_sentence)
        self.assertTrue(all(word not in stopwords for word in words))
