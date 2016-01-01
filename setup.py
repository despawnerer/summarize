from setuptools import setup, find_packages

setup(
    name='pysummarize',
    version='0.6.0',
    description='Simple multi-language Python and NLTK-based implementation of text summarization',
    url='https://github.com/despawnerer/summarize',
    author='Aleksei Voronov',
    author_email='despawn@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Text Processing',
        'Natural Language :: English',
        'Natural Language :: Spanish',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='language nltk linguistics nlp',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=[
        'Distance>=0.1.3',
        'networkx>=1.9.1',
        'nltk>=3.0.3',
    ],
)
