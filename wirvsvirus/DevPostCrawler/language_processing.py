# -*- coding: utf-8 -*-


from collections import Counter
import googletrans as gt
import spacy
from spacy_langdetect import LanguageDetector
from DevPostCrawler.extra_stop_words import EXTRA_STOP_WORDS


class LanguageProcessing(object):

    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.nlp.add_pipe(LanguageDetector(), name="language_detector",
                          last=True)
        self.translator = gt.Translator()
        self.nlp.Defaults.stop_words |= EXTRA_STOP_WORDS

    def ggl_get_language(self, text):
        return gt.LANGUAGES[self.translator.detect(text).lang]

    def get_language(self, text):
        return gt.LANGUAGES[self.nlp(text)._.language['language']]

    def ggl_translate(self, text):
        translation = self.translator.translate(text)
        return [translation.text, gt.LANGUAGES[translation.lang]]

    def get_keyword(self, text):
        doc = self.nlp(text)
        lang = doc._.language
        if lang['language'] != 'en' or lang['score'] < 0.9:
            doc = self.nlp(self.ggl_translate(text)[0])

        key_words = []
        for chunk in doc:
            if chunk.is_alpha and not chunk.is_stop:
                key_words.append(chunk.text.lower())

        return [word.title() for word, _
                in Counter(key_words).most_common(5)]
