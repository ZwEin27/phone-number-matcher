# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-06-14 16:17:20
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-06-16 08:32:01

"""
preprocess digits that must not belong to phone number

"""
import os
import json
import re
from pnmatcher.core.common import datetime
import string


class Preprocessor():

    """
    remove money digits

    samples:
        $200tel3365551212
        $276 3235551212
    """
    money_regex = r"(?:\$\d+[a-z\s]+)"

    """
    remove digits before unit

    samples:
        I'm 5'6\" 140 lbs.
    """
    units = ['lbs', 'kg']
    unit_regex = r"(?:\d+[\s\W]+(" + r"|".join(units) + "))"

    # isolate_digits_regex = r"(?:[a-z][\s_-][0-9]{,10}[\s_-][a-z])"

    others_regexes = [
        r"24/7",
        r"#\d", 
        r"\d+\'\d+", 
        r"\d+\%"
    ]
    other_regex = r"(?:" + "|".join(others_regexes) + ")"

    all_regexes = [unit_regex, other_regex]
    all_regex = r"(" + r"|".join(all_regexes) + ")"
    # print "|".join(all_regexes)

    datetime_regexes = [
        r"(?:\d{2}[ _-]\d{2}[ _-]\d{4})",
        r"(?:\d{4}[ _-]\d{2}[ _-]\d{2})"
    ]
    datetime_regex = r"(?:" + r"|".join(datetime_regexes) + ")"

    def prep_datetime(self, raw):
        m = re.findall(Preprocessor.datetime_regex, raw)
        for d in m:
            # to be optimize
            # re_digit = re.compile(r"\d+")
            # dd = ''.join(re_digit.findall(d))
            dd = d.translate(string.maketrans("",""), string.punctuation)
            dd = ''.join(dd.split())
            if datetime.is_valid_datetime(dd, '%Y%m%d') or datetime.is_valid_datetime(dd, '%m%d%Y'):
                raw = raw.replace(d, "")
        return raw

    def preprocess(self, raw):
        raw = raw.lower()
        raw = raw.encode('ascii', 'ignore')
        raw = self.prep_datetime(raw)
        # raw = re.sub(r'(\$\d+|24/7|\d+\'\d+)', '', raw, flags=re.I)
        raw = re.sub(Preprocessor.all_regex, '', raw, flags=re.I)

        

        return raw


if __name__ == '__main__':
    samples = ['$200tel3365551212', 
                '$276 3235551212',]

    preprocessor = Preprocessor()
    for sample in samples:
        print preprocessor.preprocess(sample)