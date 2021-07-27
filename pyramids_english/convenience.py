from typing import Union, TYPE_CHECKING

from pyramids.parsing import Parser
from pyramids_english.plugin import MODEL_LOADER

if TYPE_CHECKING:
    from pyramids.categorization import Category
    from pyramids.parsing import ParseResult
    from pyramids.tokenization import TokenSequence


__all__ = [
    'MODEL_LOADER',
    'PARSER',
    'tokenize',
    'parse',
]


PARSER = Parser(MODEL_LOADER.load_model())


def tokenize(text: str) -> 'TokenSequence':
    return PARSER.model.tokenizer.tokenize(text)


def parse(text: str, category: 'Union[Category, str]' = None, fast: bool = False,
          timeout: float = None, fresh: bool = True, emergency: bool = False) -> 'ParseResult':
    return PARSER.parse(text, category, fast, timeout, fresh, emergency)
