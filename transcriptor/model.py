# -*- coding: utf-8 -*-

import re
import functools

from . import languages
from .tengwar import TengwarTable, convert_to_tengwar


class TengwarTableGenerator(object):

    sections = ["consonansts", "vowels", "long_vowels", "palatalization"]

    def generate(self, lang=None):
        tengwar_desc = languages.get_tengwar_description(lang)
        for section in self.sections:
            tengwars = getattr(TengwarTable, section)
            descriptions = getattr(tengwar_desc, section, [])
            if descriptions:
                yield section.replace("_", " ").title(), zip(tengwars, descriptions)
        if hasattr(tengwar_desc, "additional"):
            yield "Additional", tengwar_desc.additional


class TextTranscriptor(object):

    word_pattern = re.compile(r"(\S+)", re.UNICODE)

    def __init__(self, tengwar=True):
        self.tengwar = tengwar

    def encoding_handler(function):
        def _wrap(self, text, *args, **kwargs):
            return function(self, text, *args, **kwargs)
        return _wrap

    def transcribe(self, text, lang=None):
        return self._transcribe(text, languages.get_transcription_map(lang, text))

    @encoding_handler
    def _transcribe(self, text, transacrption_map):
        splited = self.word_pattern.split(text)
        transcribed = [self._transcribe_word(word, transacrption_map) if i % 2 else word for i, word in enumerate(splited)]
        return "".join(transcribed)

    def _transcribe_word(self, word, transacrption_map):
        word_case = self._get_case(word)
        transcribed = functools.reduce(lambda w, kv: w.replace(*kv), transacrption_map, word.lower())
        return convert_to_tengwar(transcribed) if self.tengwar else word_case(transcribed)

    def _get_case(self, word):
        if word.isupper():
            return str.upper
        elif word.istitle():
            return str.title
        else:
            return str.lower
