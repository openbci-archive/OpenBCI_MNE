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


descr = "A Python converter of OpenBCI Processing output for MNE."

DISTNAME = 'mne_openbci'
DESCRIPTION = descr
MAINTAINER = 'Teon Brooks'
MAINTAINER_EMAIL = 'teon.brooks@gmail.com'
URL = 'https://github.com/OpenBCI/mne_openbci'
LICENSE = 'MIT'
DOWNLOAD_URL = 'https://github.com/OpenBCI/mne_openbci'
VERSION = "0.1dev"

setup(
     name = "mne_openbci",
     packages = find_packages(),
     install_requires = ['mne'],
     maintainer=MAINTAINER,
     include_package_data=True,
     maintainer_email=MAINTAINER_EMAIL,
     description=DESCRIPTION,
     license=LICENSE,
     url=URL,
     version=VERSION,
     download_url=DOWNLOAD_URL,
)
