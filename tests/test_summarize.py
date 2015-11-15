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

    def test_single_sentence(self):
        text = "Alice is awesome"
        summary = summarize(text)
        self.assertEqual(text, summary)

    def test_when_there_arent_any_words_in_common(self):
        text = (
            "Alice is awesome. I'm hot and you're not. This is pretty sick. "
            "We are all divisive. Nothing common between these sentences. "
            "And here's one more example of that happening."
        )
        summary = summarize(text)
        self.assertEqual(
            summary,
            "Alice is awesome. I'm hot and you're not. This is pretty sick. "
            "We are all divisive. Nothing common between these sentences."
        )
