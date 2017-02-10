#!/usr/bin/env python2

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(
    name = 'mlhelp',
    version = '0.0.1',
    author = 'Sartaj Singh',
    author_email = 'singhsartaj94@gmail.com',
    description = ('Some ML helper functions.'),
    license = 'MIT',
    keywords = 'ml machine learning scikit learn',
    url = 'http://github.com/leosartaj/mlhelp',
    packages=find_packages(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
    ],
)
