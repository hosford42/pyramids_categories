#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Pyramids: English
=================
English language grammar for the Pyramids Parser.
"""
import os

from pyramids.loader import ModelLoader
from pyramids.repl import repl

__author__ = 'Aaron Hosford'
__version__ = '2.0.0'
__all__ = [
    '__author__',
    '__version__',
    'load_model',
    'main',
]

# TODO: Someday, add code to automatically generate the .ctg files from
#       Kevin Atkinson's wordlist.


def get_model_loader(verbose=False):
    return ModelLoader('english', os.path.join(os.path.dirname(__file__), 'data'), verbose=verbose)


def load_model(verbose=False):
    model_loader = get_model_loader(verbose)
    return model_loader.load_model()


def main():
    model_loader = get_model_loader()
    repl(model_loader)
