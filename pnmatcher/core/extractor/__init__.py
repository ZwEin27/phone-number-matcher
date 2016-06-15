import re
import sys
import os
import collections

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'vendor'))
import en

class Extractor():

    def __init__(self):
        pass

    phone_number_format_regex = [
        r"(?:[ ]?\d{8}[ ]?\d{3}[ ]?)",
        r"(?:[ ]?\d{7}[ ]?\d{4}[ ]?)",
        r"(?:[ ]?\d{4}[ ]?\d{4}[ ]?\d{2}[ ]?)",
        r"(?:[ ]?\d{3}[ ]?\d{7}[ ]?)",
        r"(?:[ ]?\d{3}[ ]?\d{3}[ ]?\d{4}[ ]?)",
        r"(?:[ ]?\d{2}[ ]?\d{4}[ ]?\d{4}[ ]?)",
        r"(?:[\d ]{20,21})",
        r"[\d ]+"
    ]

    numbers_regex = r"(?:" + r"|".join(phone_number_format_regex) + r")"
    def extract(self, raw):
        raw = re.findall(Extractor.numbers_regex, raw)
        raw = [''.join(_.split()) for _ in raw if len(_.strip()) >= 10]
        
        return '\t'.join(raw)
