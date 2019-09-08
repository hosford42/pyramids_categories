from pyramids.config import ModelConfig
from pyramids.language import Language
from pyramids.tokenization import Tokenizer

__all__ = [
    'EnglishTokenizer',
]


class EnglishTokenizer(Tokenizer):

    @classmethod
    def from_config(cls, config_info: ModelConfig) -> 'EnglishTokenizer':
        return cls(discard_spaces=config_info.discard_spaces, language=config_info.tokenizer_language)

    def __init__(self, discard_spaces=True, language: Language = None):
        self._discard_spaces = bool(discard_spaces)
        self._language = language or Language('English', 'en', 'eng')
        self.contractions = ("'", "'m", "'re", "'s", "'ve", "'d", "'ll")

    @property
    def language(self) -> Language:
        return self._language

    @property
    def discard_spaces(self):
        return self._discard_spaces

    @staticmethod
    def is_word_char(char):
        return char.isalnum() or char == "'"

    def tokenize(self, text):
        last_char = ''
        start = 0
        end = 0
        non_space = False

        for index, char in enumerate(text):
            if start != end and last_char != char and not (self.is_word_char(last_char) and self.is_word_char(char)):
                if not self.discard_spaces or non_space:
                    token = text[start:end]
                    if token.endswith(self.contractions):
                        split = token.split("'")
                        if len(split) > 1 and (len(split) != 2 or split[0]):
                            yield "'".join(split[:-1]), start, end - len(split[-1])
                        yield "'" + split[-1], end - len(split[-1]), end
                    elif token[-2:].lower() in ('am', 'pm') and token[:-2].isdigit():
                        yield token[:-2], start, end - 2
                        yield token[-2:], end - 2, end
                    elif token[-1:].lower() in ('a', 'p') and token[:-1].isdigit():
                        yield token[:-1], start, end - 1
                        yield token[-1:], end - 1, end
                    else:
                        yield token, start, end
                    del token
                start = end
                non_space = False
            end += 1
            last_char = char
            if not char.isspace():
                non_space = True

        if start < end and (not self.discard_spaces or non_space):
            token = text[start:end]
            if token.endswith(self.contractions):
                split = token.split("'")
                if len(split) > 1:
                    yield "'".join(split[:-1]), start, end - len(split[-1])
                yield "'" + split[-1], end - len(split[-1]), end
            elif token[-2:].lower() in ('am', 'pm') and token[:-2].isdigit():
                yield token[:-2], start, end - 2
                yield token[-2:], end - 2, end
            elif token[-1:].lower() in ('a', 'p') and token[:-1].isdigit():
                yield token[:-1], start, end - 1
                yield token[-1:], end - 1, end
            else:
                yield token, start, end
