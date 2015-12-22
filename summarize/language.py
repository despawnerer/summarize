# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from funcy import memoize

from nltk import corpus, tokenize


__all__ = ['split_sentences', 'split_words', 'get_stopwords']


def split_sentences(text, language):
    return tokenize.sent_tokenize(text, language)


def split_words(sentence, stopwords):
    return set(
        word for word in tokenize.word_tokenize(sentence)
        if word.isalnum() and word not in stopwords
    )


@memoize
def get_stopwords(language):
    return set(corpus.stopwords.words(language))
