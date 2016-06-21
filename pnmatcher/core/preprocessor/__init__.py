# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-06-14 16:17:20
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-06-21 13:32:25

"""
preprocess digits that must not belong to phone number

"""
import os
import json
import re
from pnmatcher.core.common import datetime
import string


class Preprocessor():

    datetime_regexes = [
        r"(?:\d{2}[ _-]\d{2}[ _-]\d{4})",
        r"(?:\d{4}[ _-]\d{2}[ _-]\d{2})"
    ]
    datetime_regex = r"(?:" + r"|".join(datetime_regexes) + ")"

    re_datetime_regex = re.compile(datetime_regex)
    re_digits_regex = re.compile(r"\d+")

    def prep_datetime(self, raw):
        m = Preprocessor.re_datetime_regex.findall(raw)
        for d in m:
            dd = ''.join(Preprocessor.re_digits_regex.findall(d))
            if datetime.is_valid_datetime(dd, '%Y%m%d') or datetime.is_valid_datetime(dd, '%m%d%Y'):
                raw = raw.replace(d, "")
        return raw

    # money_regex = r"(?:\$\d+[a-z\s]+)"
    # isolate_digits_regex = r"(?:[a-z][\s_-][0-9]{,10}[\s_-][a-z])"

    """
    remove digits before unit

    samples:
        I'm 5'6\" 140 lbs.
    """
    units = ['lbs', 'kg']
    unit_regex = r"(?:\d+[\s\W]+(" + r"|".join(units) + "))"

    others_regexes = [
        r"24/7",
        r"#\d", 
        r"\d+\'\d+", 
        r"\d{5}[\W_ ]\d{5}", 
        r"\d+\%"
    ]
    other_regex = r"(?:" + "|".join(others_regexes) + ")"

    all_regexes = [unit_regex, other_regex]
    all_regex = r"(" + r"|".join(all_regexes) + ")"
    re_all_regex = re.compile(all_regex)

    def preprocess(self, raw):
        raw = raw.lower()
        raw = raw.encode('ascii', 'ignore')
        raw = self.prep_datetime(raw)
        raw = Preprocessor.re_all_regex.sub('', raw) # , flags=re.I
        return raw


if __name__ == '__main__':
    samples = ['$200tel3365551212', 
                '$276 3235551212',]

    preprocessor = Preprocessor()
    for sample in samples:
        print preprocessor.preprocess(sample)