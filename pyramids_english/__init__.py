#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Pyramids: English
=================
English language grammar for the Pyramids Parser.
"""
import os

from pyramids.language import Language

__author__ = 'Aaron Hosford'
__version__ = '1.0.0'
__all__ = [
    '__author__',
    '__version__',
]

# TODO: Someday, add code to automatically generate the .ctg files from
#       Kevin Atkinson's wordlist.


ENGLISH = Language('english', os.path.join(os.path.dirname(__file__), 'data'))


def main():
    ENGLISH.repl()
