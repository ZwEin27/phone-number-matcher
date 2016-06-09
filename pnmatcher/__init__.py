#!/usr/bin/python

"""
@auther: Lingzhe Teng
@version: in coding

"""

import sys
import os
sys.path.append(os.path.join(os.path.abspath('.'), 'vendor'))
import en

class PhoneNumberMatcher():
    def __init__(self):
        pass


print en.spelling.correct('2one9')
