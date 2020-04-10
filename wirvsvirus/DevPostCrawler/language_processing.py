# -*- coding: utf-8 -*-


<<<<<<< HEAD
from collections import Counter
import googletrans as gt
import spacy
from spacy_langdetect import LanguageDetector
=======
import spacy
from collections import Counter
import googletrans as gt
>>>>>>> 68e9b15773d66ab07cc8ff3434b5ec58f7dcd8ac


class LanguageProcessing(object):

    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
<<<<<<< HEAD
        self.nlp.add_pipe(LanguageDetector(), name="language_detector", last=True)
=======
>>>>>>> 68e9b15773d66ab07cc8ff3434b5ec58f7dcd8ac
        self.translator = gt.Translator()
        self.nlp.Defaults.stop_words |= {"solution",
                                         "solutions",
                                         "problem",
                                         "problems",
                                         "team",
                                         "group",
                                         "corona",
                                         "people",
                                         "risk",
                                         "want",
                                         "need",
                                         "time",
                                         "crisis",}

<<<<<<< HEAD
    def ggl_get_language(self, text):
        return gt.LANGUAGES[self.translator.detect(text).lang]

    def get_language(self, text):
        return gt.LANGUAGES[self.nlp(text)._.language['language']]
=======
    def get_language(self, text):
        return gt.LANGUAGES[self.translator.detect(text).lang]
>>>>>>> 68e9b15773d66ab07cc8ff3434b5ec58f7dcd8ac

    def ggl_translate(self, text):
        translation = self.translator.translate(text)
        return [translation.text, gt.LANGUAGES[translation.lang]]

    def get_keyword(self, text):
<<<<<<< HEAD
        doc = self.nlp(text)
        lang = doc._.language
        if lang['language'] != 'en' or lang['score'] < 0.9:
            doc = self.nlp(self.ggl_translate(text)[0])

=======
        text = self.ggl_translate(text)

        doc = self.nlp(text)
>>>>>>> 68e9b15773d66ab07cc8ff3434b5ec58f7dcd8ac
        key_words = []
        for chunk in doc:
            if chunk.is_alpha and not chunk.is_stop:
                key_words.append(chunk.text.lower())

        return [word.title() for word, _
                    in Counter(key_words).most_common(5)]
