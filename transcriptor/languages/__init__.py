# -*- coding: utf-8 -*-

from . import bulgarian, common, czech, polish, russian, serbian, ukrainian
from .detector import LanguageDetector


language_map = {
    "BG": bulgarian,
    "CZ": czech,
    "PL": polish,
    "RU": russian,
    "SR": serbian,
    "UA": ukrainian
}

detector = LanguageDetector(language_map)


def get_transcription_map(lang_code, text):
    return language_map.get(lang_code, common).transcription_map


def get_tengwar_description(lang_code):
    return language_map.get(lang_code, common).TengwarDescription


def get_available_languages():
    return sorted(language_map.keys())
