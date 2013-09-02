#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='ThePirateBay',
    version='0.0.1',
    install_requires=['BeautifulSoup4>=4.3.1',],
    author='Karan Goel',
    author_email='karan@goel.im',
    packages=['tpb',],
    url='https://github.com/thekarangoel/TPB/',
    license='GNU General Public License',
    description='Unofficial Python API for ThePirateBay.',
    long_description='Unofficial Python API for ThePirateBay. Usage: https://github.com/thekarangoel/TPB.',
)