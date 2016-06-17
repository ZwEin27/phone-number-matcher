# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-06-09 13:43:42
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-06-17 12:59:57

"""
tokenize original content formated in 'text' or 'url' separately, and removing punctuations

"""


import string
import re

from pnmatcher.vendor.crf.crf_tokenizer import CrfTokenizer
from urlparse import urlparse

SOURCE_TYPE_TEXT = 'text'
SOURCE_TYPE_URL = 'url'

class Tokenizer():

    re_2_digts_only_in_url_regex = re.compile(r'(?<=[-_])\d{2}(?=[_/])')
    re_all_alphabet_in_url_regex = re.compile(r'\w+')

    def __init__(self, source_type='text'):
        self.set_source_type(source_type)
        self.source_type = source_type      # text or url

    def set_source_type(self, source_type):
        """ 
        'text' or 'url'

        """
        st = source_type.lower()
        if source_type.lower() not in [SOURCE_TYPE_TEXT, SOURCE_TYPE_URL] :
            raise Exception(source_type + ' is not a source type, which should be "text" or "url"')

        self.source_type = source_type

    def remove_punctuation(self, raw):
        return raw.translate(string.maketrans("",""), string.punctuation)

    def tokenize(self, raw):
        result = None
        if self.source_type == SOURCE_TYPE_TEXT:
            result = self.tokenize_text(raw)
        elif self.source_type == SOURCE_TYPE_URL:
            result = self.tokenize_url(raw)
        return ' '.join(result.split())

    def tokenize_text(self, raw):
        t = CrfTokenizer()
        t.setRecognizeHtmlEntities(True)
        t.setRecognizeHtmlTags(True)
        t.setSkipHtmlTags(True)
        t.setRecognizePunctuation(True)
        tokens = t.tokenize(raw)
        tokens = ' '.join(tokens)
        tokens = self.remove_punctuation(tokens)
        return tokens

    def tokenize_url(self, raw):
        SEPARATOR = ' '

        url_obj = urlparse(raw)
        
        # parse netloc
        netloc = url_obj.netloc.split('.')[:-2]   # get rid of port numbers, ext and domain name

        # parse path
        path = url_obj.path
        path = Tokenizer.re_2_digts_only_in_url_regex.sub('', path)
        path = path.split('/')

        content = netloc + path

        content = [SEPARATOR.join(Tokenizer.re_all_alphabet_in_url_regex.findall(_)) for _ in content]

        # parse params
        # url_obj.params
        
        # parse query
        # url_obj.query
        return ' sep '.join(content)
   




    
