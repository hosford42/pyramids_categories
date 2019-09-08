import os

from pyramids.language import Language
from pyramids.loader import ModelLoader
from pyramids.plugin import Plugin

from pyramids_english.tokenization import EnglishTokenizer

LANGUAGE = Language('English', 'en', 'eng')

PLUGIN = Plugin()

TOKENIZER_NAME = 'Pyramids English Tokenizer'
TOKENIZER_TYPE = EnglishTokenizer
PLUGIN.register_tokenizer_type(TOKENIZER_NAME, LANGUAGE, TOKENIZER_TYPE)

MODEL_NAME = 'Pyramids English Model'
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'data')
MODEL_LOADER = ModelLoader(MODEL_NAME, MODEL_PATH, verbose=False)
PLUGIN.register_model(MODEL_NAME, LANGUAGE, MODEL_LOADER)
