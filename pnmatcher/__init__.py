#!/usr/bin/python

"""
@auther: Lingzhe Teng
@version: in coding

"""

""" TODO

4. write script for spark
5. optimize based on linhong's paper for regular expression

"""

import sys
import os

from pnmatcher.core.common.url import URLHelper
from pnmatcher.core.preprocessor import Preprocessor
from pnmatcher.core.tokenizer import Tokenizer
from pnmatcher.core.extractor import Extractor
from pnmatcher.core.cleaner import Cleaner
from pnmatcher.core.validator import Validator

sys.path.append(os.path.join(os.path.abspath('.'), 'vendor'))


class PhoneNumberMatcher():
    def __init__(self):
        self.url_helper = URLHelper()
        self.preprocessor = Preprocessor()
        self.tokenizer = Tokenizer(source_type='text')
        self.extractor = Extractor()
        self.cleaner = Cleaner()
        self.validator = Validator()

    def text_matcher(self, text):
        self.tokenizer = Tokenizer(source_type='text')

    def url_matcher(self, url_string):
        self.tokenizer = Tokenizer(source_type='url')




