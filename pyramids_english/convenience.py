from pyramids.parsing import Parser
from pyramids_english.plugin import MODEL_LOADER

__all__ = [
    'MODEL_LOADER',
    'PARSER',
    'tokenize',
    'parse',
]


PARSER = Parser(MODEL_LOADER.load_model())


def tokenize(text: str):
    return PARSER.model.tokenizer.tokenize(text)


def parse(text: str, category=None, fast=False, timeout=None, fresh=True, emergency=False):
    return PARSER.parse(text, category, fast, timeout, fresh, emergency)
