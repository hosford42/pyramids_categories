#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Setup script for Pyramids Categories."""

from setuptools import setup
from codecs import open
from os import path

from pyramids_english import __author__, __version__


here = path.abspath(path.dirname(__file__))


# Default long description
long_description = """

Pyramids Categories
===================

*Pre-compiled category files for the Pyramids Parser.*

See 'Pyramids <https://github.com/hosford42/pyramids>`__ for the Pyramids
Parser itself.

""".strip()


# Get the long description from the relevant file. First try README.rst,
# then fall back on the default string defined here in this file.
if path.isfile(path.join(here, 'README.rst')):
    with open(path.join(here, 'README.rst'),
              encoding='utf-8',
              mode='rU') as description_file:
        long_description = description_file.read()


# See https://pythonhosted.org/setuptools/setuptools.html for a full list
# of parameters and their meanings.
setup(
    name='pyramids_english',
    version=__version__,
    author=__author__,
    author_email='hosford42@gmail.com',
    url='https://github.com/hosford42/pyramids_categories',
    license='MIT',
    platforms=['any'],
    description='Pyramids Categories: '
                'Pre-compiled category files for the Pyramids Parser',
    long_description=long_description,

    # See https://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular,
        # ensure that you indicate whether you support Python 2, Python 3
        # or both.
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='pyramids parser categories category files',
    packages=['pyramids_english'],
    include_package_data=True,
    zip_safe=False
)
