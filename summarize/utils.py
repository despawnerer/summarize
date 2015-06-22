from funcy import memoize

from nltk import corpus, tokenize


def get_words(sentence, stopwords):
    return set(
        word for word in tokenize.word_tokenize(sentence)
        if word.isalnum() and word not in stopwords)


@memoize
def get_stopwords(language):
    return set(corpus.stopwords.words(language))
