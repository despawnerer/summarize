#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
import codecs
from itertools import combinations
from operator import itemgetter

from distance import jaccard
from networkx import Graph, pagerank
from pattern.en import tokenize
from pattern.vector import Document, LEMMA


def summarize(text, sentence_count=2):
    sentence_list = tokenize(text)

    # each document's name is the sentence's original index
    # so that we can put them back together later
    docs = [Document(string=sentence, name=index, stemmer=LEMMA)
            for index, sentence in enumerate(sentence_list)]

    graph = Graph()
    for doc_a, doc_b in combinations(docs, 2):
        wordset_a = [x[1] for x in doc_a.keywords()]
        wordset_b = [y[1] for y in doc_b.keywords()]
        similarity = 1 - jaccard(wordset_a, wordset_b)
        if similarity > 0:
            graph.add_edge(doc_a.name, doc_b.name, weight=similarity)

    ranked_sentence_indexes = pagerank(graph).items()
    sentences_by_rank = sorted(
        ranked_sentence_indexes, key=itemgetter(1), reverse=True)
    best_sentences = map(itemgetter(0), sentences_by_rank[:sentence_count])
    best_sentences_in_order = sorted(best_sentences)

    return ' '.join(sentence_list[index] for index in best_sentences_in_order)


if __name__ == "__main__":
    filename = sys.argv[1]
    with codecs.open(filename, encoding='utf-8') as f:
        print summarize(f.read(), 5)
