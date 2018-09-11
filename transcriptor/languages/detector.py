# -*- coding: utf-8 -*-

from langdetect.detector_factory import DetectorFactory
from langdetect.utils.lang_profile import LangProfile
from langdetect.lang_detect_exception import LangDetectException


class LanguageDetector(object):

    def __init__(self, language_map):
        self.factory = DetectorFactory()
        lang_count, index = len(language_map), 0
        for name, lang in language_map.items():
            profile = LangProfile(name)
            for word in lang.charset.split():
                profile.add(word)
            self.factory.add_profile(profile, index, lang_count)
            index += 1

    def detect_language(self, text):
        lang = None
        detector = self.factory.create()
        detector.append(text.lower())
        try:
            lang = detector.detect()
        except LangDetectException:
            print("Cannot detect language")
        else:
            print("Detected language:", lang)
        finally:
            return lang
