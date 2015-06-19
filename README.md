summarize.py
============

Quick python-based implementation of Flipboard's summarization algorithm.


Setup
-----

Before using, call `import nltk; nltk.download()` from a python shell and download `stopwords` and `punkt` packages.


Usage
-----

	from summarize import summarize
	summarize(u"Alice and Bob are friends. Alice is fun and cuddly."
	          u" Bob is cute and quirky. Together they go on wonderful"
	          u" adventures in the land of tomorrow. Alice's cuddlines"
	          u" and Bob's cuteness allow them to reach their goals."
	          u" But before they get to them, they have to go past their"
	          u" mortal enemy — Mr. Boredom. He is ugly and mean. They"
	          u" will surely defeat him. He is no match for their abilities.")


Online demo
-----------

https://evening-atoll-8940.herokuapp.com/
