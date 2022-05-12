#!/usr/bin/python3
import re


class ReEval(object):
    @staticmethod
    def eval(pattern, text):
        return re.search(pattern, text)
