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

from pnmatcher.core.preprocessor import Preprocessor
from pnmatcher.core.tokenizer import Tokenizer
from pnmatcher.core.extractor import Extractor
from pnmatcher.core.cleaner import Cleaner
from pnmatcher.core.validator import Validator

sys.path.append(os.path.join(os.path.abspath('.'), 'vendor'))

# __all__ = [PhoneNumberMatcher]

class PhoneNumberMatcher():
    def __init__(self):
        self.preprocessor = Preprocessor()
        self.tokenizer = Tokenizer(source_type='text')
        self.extractor = Extractor()
        self.cleaner = Cleaner()
        self.validator = Validator()

    def match(self, content, source_type='text'):
        self.tokenizer.set_source_type(source_type)
        content = self.preprocessor.preprocess(content)
        content = self.tokenizer.tokenize(content)
        content = self.cleaner.clean(content)
        content = self.extractor.extract(content)
        content = self.validator.validate(content)
        return content

    





