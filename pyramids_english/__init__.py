#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Pyramids: English
=================
English language model for the Pyramids parser.
"""

from pyramids_english.plugin import MODEL_LOADER

__author__ = 'Aaron Hosford'
__version__ = '2.0.0'
__all__ = [
    '__author__',
    '__version__',
    'main'
]


def main():
    from pyramids.repl import repl
    repl(MODEL_LOADER)
