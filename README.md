summarize.py
============

Quick python2-based implementation of Flipboard's summarization algorithm.

Setup
-----

Before using, call `import nltk; nltk.download()` from a python shell and download stopwords corpus and punkt trained models.

Examples
--------

Call it directly with a filename:

    $ python summarize.py text_to_summarize.txt

Use as a library:

	from summarize import summarize
	summarize("Welcome to the world of tomorrow! There's nothing here, so move along.")

Online demo
-----------

https://evening-atoll-8940.herokuapp.com/

