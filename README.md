summarize.py
============

[![Build Status](https://travis-ci.org/despawnerer/summarize.svg?branch=master)](https://travis-ci.org/despawnerer/summarize)

Simple Python and NLTK-based implementation of text summarization.


Installation
------------

	$ pip install pysummarize


Setup
-----

Before using, make sure you have `stopwords` and `punkt` NLTK packages downloaded:

```python
import nltk
nltk.download(['stopwords', 'punkt'])
```


Usage
-----

```python
from summarize import summarize
summarize(u"Alice and Bob are friends. Alice is fun and cuddly."
          u" Bob is cute and quirky. Together they go on wonderful"
          u" adventures in the land of tomorrow. Alice's cuddlines"
          u" and Bob's cuteness allow them to reach their goals."
          u" But before they get to them, they have to go past their"
          u" mortal enemy — Mr. Boredom. He is ugly and mean. They"
          u" will surely defeat him. He is no match for their abilities.")
```


Online demo
-----------

http://summarize.plansfortheday.org/ ([source](https://github.com/despawnerer/summarize-demo))


Credits
-------
Original description of the algorithm: http://engineering.flipboard.com/2014/10/summarization/
