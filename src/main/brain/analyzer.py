#!/usr/bin/env python3
import unicodedata
from .mapping import math_symbols_mapping
import re
from string import punctuation
from nltk import ne_chunk, pos_tag, word_tokenize, RegexpParser
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
from nltk import download
download('stopwords')
download('punkt')


class NLP:
    # stopword list to use
    spanish_stopwords = stopwords.words('spanish')
    # spanish stemmer
    stemmer = SnowballStemmer('spanish')
    # punctuation to remove
    non_words = list(punctuation)
    # we add spanish punctuation
    non_words.extend(['¿', '¡'])
    # self.non_words.extend(map(str,range(10)))

    def __init__(self):
        pass

    @staticmethod
    def is_positive_answer(answer):
        return answer in ['si', 'yes']

    @staticmethod
    def is_negative_answer(answer):
        return answer in ['no']

    @staticmethod
    def create_parts_of_speech(text):
        tokens = word_tokenize(text)
        pt = pos_tag(tokens)
        chunked = ne_chunk(pt)
        chunked = [w for w in chunked if not w in NLP.spanish_stopwords]
        return chunked

    @staticmethod
    def is_question_with_modal(parts_of_speech):
        grammar = 'QS: {<MD><PRP><VB>}'
        cp = RegexpParser(grammar)
        result = cp.parse(parts_of_speech)
        for subtree in result.subtrees():
            if subtree.label() in ['MD', 'WD', 'QS']:
                return True

    @staticmethod
    def is_question_with_inversion(parts_of_speech):
        grammar = 'QS: {<VBP><PRP>}'
        cp = RegexpParser(grammar)
        result = cp.parse(parts_of_speech)
        for subtree in result.subtrees():
            if subtree.label() in ['QS']:
                return True

    # extraer verbo
    @staticmethod
    def extract_verb(parts_of_speech):
        for part in parts_of_speech:
            if part[1] in ['VB']:
                return part[0]
        return ' '

    # extraer modelo
    @staticmethod
    def extract_modal(parts_of_speech):
        for part in parts_of_speech:
            if part[1] in ['MD']:
                return part[0]
        return ' '

    # extract_sustantivo
    @staticmethod
    def extract_noun(parts_of_speech):
        for part in parts_of_speech:
            if part[1] in ['NN', 'NNS', 'NNP', 'NNPS']:
                return part[0]
        return ' '


class Analyzer:

    _INSTANCE = None

    def __init__(self):
        pass

    def getInstance():
        if not Analyzer._INSTANCE:
            Analyzer._INSTANCE = Analyzer()
        return Analyzer._INSTANCE

    def extract(self, user_transcript) -> tuple[str, any]:
        return self.tokenize(user_transcript)

    def replaceMathSymbolsWithWords(self, transcript):
        replaced_transcript = ''
        for word in transcript.split():
            if word in math_symbols_mapping.values():
                for key, value in math_symbols_mapping.items():
                    if value == word:
                        replaced_transcript += ' ' + key
            else:
                replaced_transcript += ' ' + word
        return replaced_transcript

    def stem_tokens(self, tokens, stemmer):
        stemmed = []
        for item in tokens:
            stemmed.append(stemmer.stem(item))
        return stemmed

    def tokenize(self, text) -> tuple[str, any]:
        # remove links from tweets
        text = re.sub(r"http\S+", "https", text)
        # remove repeated characters
        text = re.sub(r'(.)\1+', r'\1\1', text)
        parts = NLP.create_parts_of_speech(text)
        parts = [w[0] for w in parts]
        return " ".join(parts), parts

    def strip_accents(self, text):
        """
        Strip accents from input String.
        :param text: The input string.
        :type text: String.
        :returns: The processed String.
        :rtype: String.
        """
        try:
            text = unicode(text, 'utf-8')
        except (TypeError, NameError):  # unicode is a default on python 3
            pass
        text = unicodedata.normalize('NFD', text)
        text = text.encode('ascii', 'ignore')
        text = text.decode("utf-8")
        return str(text)
