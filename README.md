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

	summarize(text[, sentence_count=5, language='english'])

- `text` — text to be summarized
- `sentence_count` — number of sentences in the result
- `language` — language that the text is in (lowercase)


### Example

```python
from summarize import summarize
summarize("Alice and Bob are friends. Alice is fun and cuddly."
          " Bob is cute and quirky. Together they go on wonderful"
          " adventures in the land of tomorrow. Alice's cuddlines"
          " and Bob's cuteness allow them to reach their goals."
          " But before they get to them, they have to go past their"
          " mortal enemy - Mr. Boredom. He is ugly and mean. They"
          " will surely defeat him. He is no match for their abilities.")
```


Online demo
-----------

http://summarize.plansfortheday.org/ ([source](https://github.com/despawnerer/summarize-demo))


Credits
-------
Original description of the algorithm: http://engineering.flipboard.com/2014/10/summarization/
