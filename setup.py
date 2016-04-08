# -*- coding: utf-8 -*-
# Authors: Teon Brooks <teon.brooks@gmail.com>
#
# License: BSD (3-clause)
'''
Basic ``setup.py``, intended for::
    $ python setup.py develop
Incomplete, does not specify dependencies etc.
After:
http://packages.python.org/distribute/setuptools.html#basic-use
Created on Apr 8, 2016
@author: Teon Brooks
'''


from setuptools import setup, find_packages

setup(
    name = "mne_openbci",
    version = "0.1dev",
    packages = find_packages(),
    install_requires = ['mne'],
)
