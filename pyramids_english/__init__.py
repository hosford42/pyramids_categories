#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Pyramids: English
=================
English language grammar for the Pyramids Parser.
"""
import os

from pyramids.loader import ModelLoader
from pyramids.parsing import Parser
from pyramids.repl import repl
from pyramids_english.tokenization import EnglishTokenizer

__author__ = 'Aaron Hosford'
__version__ = '2.0.0'
__all__ = [
    '__author__',
    '__version__',
    'load_model',
    'get_parser',
    'tokenize',
    'parse',
    'main',
]

# TODO: Someday, add code to automatically generate the .ctg files from
#       Kevin Atkinson's wordlist.


def get_model_loader(path=None, verbose=False):
    path = path or os.path.join(os.path.dirname(__file__), 'data')
    return ModelLoader('english', path, verbose=verbose)


def load_model(path=None, verbose=False):
    model_loader = get_model_loader(path, verbose)
    return model_loader.load_model()


def get_parser(model=None):
    if model is None:
        model = load_model()
    return Parser(model)


def tokenize(text: str, discard_spaces: bool = True):
    return EnglishTokenizer(discard_spaces).tokenize(text)


_parser = None


def parse(text: str, category=None, fast=False, timeout=None, fresh=True, emergency=False):
    global _parser
    if _parser is None:
        _parser = get_parser()
    return _parser.parse(text, category, fast, timeout, fresh, emergency)


def main():
    model_loader = get_model_loader()
    repl(model_loader)
