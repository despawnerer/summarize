from setuptools import setup, find_packages

setup(
    name='summarize',
    version='0.2.1',
    description='Simple Python and NLTK-based implementation of text summarization',
    url='https://github.com/despawnerer/summarize',
    author='Aleksei Voronov',
    author_email='despawn@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='language nltk linguistics nlp',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=[
        'Distance>=0.1.3',
        'networkx>=1.9.1',
        'nltk>=3.0.3',
    ],
)
