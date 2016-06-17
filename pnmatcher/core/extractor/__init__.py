# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-06-13 23:15:52
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-06-17 13:01:17

"""
extract digits that seem good

"""

import re
import sys
import os
import collections

# sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'vendor'))
# import en

class Extractor():

    def __init__(self):
        pass

    phone_number_format_regex = [
        r"(?:" + 10*r"[ ]\d" + r")",
        r"(?:[ ]?\d{10}[ ])",
        r"(?:[ ]?\d{8}[ ]\d{3}[ ]?)",
        r"(?:[ ]?\d{7}[ ]\d{4}[ ]?)",
        r"(?:[ ]?\d{4}[ ]\d{4}[ ]\d{2}[ ]?)",
        r"(?:[ ]?\d{3}[ ]\d{7,8}[ ]?)",
        r"(?:[ ]?\d{3}[ ]\d{3}[ ]\d{4}[ ]?)",
        r"(?:[ ]?\d{3}[ ]\d{3}[ ]\d{1}[ ]\d{3}[ ]?)",
        r"(?:[ ]?\d{2}[ ]\d{4}[ ]\d{4}[ ]?)",
        r"(?:[\d ]{20,22})",
        r"[\d ]+"
    ]

    numbers_regex = r"(?:" + r"|".join(phone_number_format_regex) + r")"
    re_numbers_regex = re.compile(numbers_regex)
    
    def extract(self, raw):
        raw = Extractor.re_numbers_regex.findall(raw)
        raw = [''.join(_.split()) for _ in raw if len(_.strip()) >= 10]

        return '\t'.join(raw)
