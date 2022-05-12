#!/usr/bin/python3
import re


class ReEval(object):
    @staticmethod
    def eval(pattern, text):
        return re.search(pattern, text)

    @staticmethod
    def match(pattern, text):
        return re.match(pattern, text)