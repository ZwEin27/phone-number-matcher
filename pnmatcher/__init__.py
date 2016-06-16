#!/usr/bin/python

# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-06-13 23:15:52
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-06-16 11:20:08

"""
main file for phone number matcher

"""

import sys
import os

from pnmatcher.core.preprocessor import Preprocessor
from pnmatcher.core.tokenizer import Tokenizer
from pnmatcher.core.extractor import Extractor
from pnmatcher.core.cleaner import Cleaner
from pnmatcher.core.validator import Validator

sys.path.append(os.path.join(os.path.abspath('.'), 'vendor'))

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

    





