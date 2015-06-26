# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from unittest import TestCase

from summarize import summarize


class SummarizeTestCase(TestCase):
    def test_that_it_runs(self):
        text = summarize(
            "Alice and Bob are friends. Alice is fun and cuddly."
            " Bob is cute and quirky. Together they go on wonderful"
            " adventures in the land of tomorrow. Alice's cuddlines"
            " and Bob's cuteness allow them to reach their goals."
            " But before they get to them, they have to go past their"
            " mortal enemy — Mr. Boredom. He is ugly and mean. They"
            " will surely defeat him. He is no match for their abilities.")
        self.assertTrue(bool(text))

    def test_doesnt_crash_on_empty_sentences(self):
        try:
            summarize('. . .')
        except Exception as e:
            self.fail(e)
