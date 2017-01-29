#!/usr/bin/env python

from __future__ import unicode_literals
from __init__ import __version__

try:
    from setuptools.core import setup
except ImportError:
    from distutils.core import setup


setup(
    name='Dictsensors',
    version=__version__,
    description='Python Distribution Utilities',
    author='Jiri Dubansky',
    author_email='jiri@dubansky.cz',
    url='https://github.com/MrS1lentcz/dictsensors',
    license='LICENSE.txt',
    test_suite='tests',
    py_modules=['sensors'],
)
