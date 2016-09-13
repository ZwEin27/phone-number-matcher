# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-06-21 12:36:47
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-09-12 22:19:16


import sys
import os
import json
import re
import string
import collections
import phonenumbers
from datetime import datetime
from crf_tokenizer import CrfTokenizer
from urlparse import urlparse
from string import maketrans
from phonenumbers.phonenumberutil import NumberParseException
from difflib import SequenceMatcher


def is_valid_datetime(raw, date_format):
    try:
        datetime.strptime(raw, date_format)
        return True
    except ValueError:
        return False

class Preprocessor():

    re_prep = re.compile(r'[\(\)]')

    reg_simple_format = [
        r'(?:(?<=[ \A\b-\.\?])\d{3}[ \?\.-]\d{3}[ \?\.-]\d{4}(?=[ \Z\b-\.\?]))'
    ]
    re_simple_format = re.compile(r'(?:'+r'|'.join(reg_simple_format)+r')')


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
            if is_valid_datetime(dd, '%Y%m%d') or is_valid_datetime(dd, '%m%d%Y'):
                raw = raw.replace(d, "")
        return raw

    money_regex = r"(?:(?<=[\D])\$\d+(?=[\W_]))"
    # isolate_digits_regex = r"(?:[a-z][\s_-][0-9]{,10}[\s_-][a-z])"

    """
    remove digits before unit

    samples:
        I'm 5'6\" 140 lbs.
    """
    units = ['lbs', 'kg', 'hour', 'hr', 'hh']
    unit_regex = r"(?:\d+[\s\W]*(" + r"|".join(units) + "))"

    others_regexes = [
        r"24/7",
        r"#\d+", 
        r"\d+\'\d+", 
        r"(?<=[\W_])\d{5}[\W_]{1,}\d{5}(?=[\W_])", 
        r"- {1,}\d+$", 
        r"\d+\%"
    ]
    other_regex = r"(?:" + "|".join(others_regexes) + ")"

    all_regexes = [money_regex, unit_regex, other_regex]
    all_regex = r"(" + r"|".join(all_regexes) + ")"
    re_all_regex = re.compile(all_regex)

    def preprocess(self, raw):
        raw = raw.lower()
        raw = raw.encode('ascii', 'ignore')
        raw = self.prep_datetime(raw)
        raw = Preprocessor.re_prep.sub(' ', raw)
        raw = Preprocessor.re_all_regex.sub('', raw)
        raw = Preprocessor.re_simple_format.sub('pnwrapper \g<0> pnwrapper', raw)
        return raw



SOURCE_TYPE_TEXT = 'text'
SOURCE_TYPE_URL = 'url'

class Tokenizer():

    re_2_digts_only_in_url_regex = re.compile(r'(?<=[-_])\d{2}(?=[_/])')
    re_all_alphabet_in_url_regex = re.compile(r'\w+')

    def __init__(self, source_type='text'):
        self.set_source_type(source_type)

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
   



class Cleaner():

    def prep_misspelled_numeral_words(self, raw):
        misspelling_dict = {
            "th0usand": "thousand",
            "th1rteen": "thirteen",
            "f0urteen": "fourteen",
            "e1ghteen": "eighteen",
            "n1neteen": "nineteen",
            "f1fteen": "fifteen",
            "s1xteen": "sixteen",
            "th1rty": "thirty",
            "e1ghty": "eighty",
            "n1nety": "ninety",
            "fourty": "forty",
            "f0urty": "forty",
            "e1ght": "eight",
            "f0rty": "forty",
            "f1fty": "fifty",
            "s1xty": "sixty",
            "zer0": "zero",
            "for": "four",
            "f0ur": "four",
            "f1ve": "five",
            "n1ne": "nine",
            "0ne": "one",
            "too": "two",
            "tw0": "two",
            "to": "two",
            "s1x": "six"
        }

        for key in misspelling_dict.keys():
            raw = raw.replace(key, misspelling_dict[key])
        return raw

    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'siz', 'seven', 'eight', 'nine']

    re_twenty_x = re.compile(r"(two|twenty[\W_]+(?=(\d|" + r"|".join(numbers) + ")))")
    re_thirty_x = re.compile(r"(three|thirty[\W_]+(?=(\d|" + r"|".join(numbers) + ")))")
    re_forty_x = re.compile(r"(four|forty[\W_]+(?=(\d|" + r"|".join(numbers) + ")))")
    re_fifty_x = re.compile(r"(five|fifty[\W_]+(?=(\d|" + r"|".join(numbers) + ")))")
    re_sixty_x = re.compile(r"(six|sixty[\W_]+(?=(\d|" + r"|".join(numbers) + ")))")
    re_seventy_x = re.compile(r"(seven|seventy[\W_]+(?=(\d|" + r"|".join(numbers) + ")))")
    re_eighty_x = re.compile(r"(eight|eighty[\W_]+(?=(\d|" + r"|".join(numbers) + ")))")
    re_ninety_x = re.compile(r"(nine|ninety[\W_]+(?=(\d|" + r"|".join(numbers) + ")))")

    # re_ten = re.compile(r"(?<=[ilo0-9])ten(?=[ ilo0-9\.\t\(\),\:\-\+\!])")
    re_ten = re.compile(r"(?<=[ilo0-9])ten\b")
    re_one = re.compile(r'(?:(?<=([0-9yneorxt]| ))one|(?:(?<=[ils])[i]((?=[ils])|$)))')
    re_zero = re.compile(r'(?:zero|oh|(?:(?<=[0-9])(o+?))|(?:o(?=[0-9]))|(?:(?<=[o\s])o(?=[o\s])))')

    def prep_replace_numeral_words(self, raw):
        raw = raw.replace("hundred", "00")
        raw = raw.replace("thousand", "000")

        raw = raw.replace("eleven", "11")
        raw = raw.replace("twelve", "12")
        raw = raw.replace("thirteen", "13")
        raw = raw.replace("fourteen", "14")
        raw = raw.replace("fifteen", "15")
        raw = raw.replace("sixteen", "16")
        raw = raw.replace("seventeen", "17")
        raw = raw.replace("eighteen", "18")
        raw = raw.replace("nineteen", "19")

        raw = Cleaner.re_twenty_x.sub("2", raw)
        raw = Cleaner.re_thirty_x.sub("3", raw)
        raw = Cleaner.re_forty_x.sub("4", raw)
        raw = Cleaner.re_fifty_x.sub("5", raw)
        raw = Cleaner.re_sixty_x.sub("6", raw)
        raw = Cleaner.re_seventy_x.sub("7", raw)
        raw = Cleaner.re_eighty_x.sub("8", raw)
        raw = Cleaner.re_ninety_x.sub("9", raw)

        raw = Cleaner.re_ten.sub("10", raw)
        raw = Cleaner.re_one.sub("1", raw)
        raw = Cleaner.re_zero.sub("0", raw)

        raw = raw.replace("twenty", "20")
        raw = raw.replace("thirty", "30")
        raw = raw.replace("forty", "40")
        raw = raw.replace("fifty", "50")
        raw = raw.replace("sixty", "60")
        raw = raw.replace("seventy", "70")
        raw = raw.replace("eighty", "80")
        raw = raw.replace("ninety", "90")
        return raw

    def clean(self, raw):
        raw = self.prep_misspelled_numeral_words(raw)
        raw = self.prep_replace_numeral_words(raw)
        # print raw
        return raw

class Extractor():

    def __init__(self):
        pass

    prefix = r'(?:(?<=[\A\b\sa-zA-Z])|^)'
    # prefix = r'\b'
    # prefix = r'[ ]?'
    postfix = r'(?:(?=[\Z\b\sa-zA-Z])|$)'
    # postfix = r'\b'
    # postfix = r'[ ]?'

    phone_number_format_regex = [
        r'(?:'+prefix+r"\d{10,13}"+postfix+r')',
        r'(?:'+prefix+r"\d{9,10}"+postfix+r')',
        r'(?:'+prefix+r"\d{8}[ ]\d{3,4}"+postfix+r')',
        r'(?:'+prefix+r"\d{7}[ ]\d{3,4}"+postfix+r')',
        r'(?:'+prefix+r"\d{6}[ ]\d{4}"+postfix+r')',
        r'(?:'+prefix+r"\d{5}[ ]\d{6}"+postfix+r')',
        r'(?:'+prefix+r"\d{5}[ ]\d{4}[ ]\d{4}"+postfix+r')',
        r'(?:'+prefix+r"\d{5}[ ]\d{4}"+postfix+r')',
        r'(?:'+prefix+r"\d{5}[ ]\d{4}[ ]\d{2}[ ]\d{2}"+postfix+r')',
        r'(?:'+prefix+r"\d{4}[ ]\d{4}[ ]\d{2}"+postfix+r')',
        r'(?:'+prefix+r"\d{4}[ ]\d{2}[ ]\d{2}[ ]\d{2}[ ]\d{2}"+postfix+r')',
        r'(?:'+prefix+r"\d{4}[ ]\d{3}[ ]\d{3}"+postfix+r')',
        r'(?:'+prefix+r"\d{3}[ ]\d{7,8}"+postfix+r')',
        r'(?:'+prefix+r"\d{3}[ ]\d{4}[ ]\d{4}"+postfix+r')',
        r'(?:'+prefix+r"\d{3}[ ]\d{4}[ ]\d{3}"+postfix+r')',
        r'(?:'+prefix+r"\d{3}[ ]\d{3}[ ]\d{4}"+postfix+r')',
        r'(?:'+prefix+r"\d{3}[ ]\d{3}[ ]\d{3}[ ]\d{1}"+postfix+r')',
        r'(?:'+prefix+r"\d{3}[ ]\d{3}[ ]\d{2}[ ]\d{1}[ ]\d{1}"+postfix+r')',
        r'(?:'+prefix+r"\d{3}[ ]\d{3}[ ]\d{1}[ ]\d{3}"+postfix+r')',
        r'(?:'+prefix+r"\d{3}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{4}"+postfix+r')',
        r'(?:'+prefix+r"\d{2}[ ]\d{4}[ ]\d{4}"+postfix+r')',
        r'(?:'+prefix+r"\d{2}[ ]\d{8}"+postfix+r')',
        r'(?:'+prefix+r"\d{1}[ ]\d{8}[ ]\d{1}"+postfix+r')',    # \d{2}[ ] ...
        r'(?:'+prefix+r"\d{1}[ ]\d{3}[ ]\d{3}[ ]\d{3}"+postfix+r')',
        r'(?:'+prefix+r"\d{2}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}"+postfix+r')',
        r'(?:'+prefix+r"\d{1}[ ]\d{2}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}"+postfix+r')',
        r'(?:'+prefix+r"\d{1}[ ]\d{1}[ ]\d{2}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}"+postfix+r')',
        r'(?:'+prefix+r"\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{2}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}"+postfix+r')',
        r'(?:'+prefix+r"\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{2}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}"+postfix+r')',
        r'(?:'+prefix+r"\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{2}[ ]\d{1}[ ]\d{1}[ ]\d{1}"+postfix+r')',
        r'(?:'+prefix+r"\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{2}[ ]\d{1}[ ]\d{1}"+postfix+r')',
        r'(?:'+prefix+r"\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{2}[ ]\d{1}"+postfix+r')',
        r'(?:'+prefix+r"\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{2}"+postfix+r')',
        r'(?:'+prefix+r"\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}[ ]\d{1}"+postfix+r')'
    ]

    # numbers_regex = r"(?:" + r"|".join(phone_number_format_regex) + r")"
    numbers_regex = r"(?:" + r"|".join(phone_number_format_regex) + r")"
    re_numbers_regex = re.compile(numbers_regex)
    # print numbers_regex
    
    def extract(self, raw):
        raw = Extractor.re_numbers_regex.findall(raw)
        raw = [''.join(_.split()) for _ in raw if len(_.strip()) >= 10]
        return '\t'.join(raw)


class Validator():

    re_zero = re.compile(r'0{3,}')

    def validate_phone_number_with_coutry_code(self, raw, country_code='US'):
        try:
            z = phonenumbers.parse(raw, country_code)
        except NumberParseException, e:
            pass

            """
            if e.error_type == NumberParseException.INVALID_COUNTRY_CODE:
                # Invalid country code specified
                return []
            elif e.error_type == NumberParseException.NOT_A_NUMBER:
                # The string passed in had fewer than 3 digits in it.
                # The number failed to match the regular expression
                return []
            elif e.error_type == NumberParseException.TOO_SHORT_AFTER_IDD:
                # The string started with an international dialing prefix
                # but after this was removed, it had fewer digits than any
                # valid phone number (including country code) could have.
                return []
            elif e.error_type == NumberParseException.TOO_SHORT_NSN:
                # After any country code has been stripped, the string
                # had fewer digits than any valid phone number could have.
                return []

            elif e.error_type == NumberParseException.TOO_LONG:
                # String had more digits than any valid phone number could have
                return []
            """

            # print e.error_type, e._msg
        else:
            if phonenumbers.is_possible_number(z) and phonenumbers.is_valid_number(z):
                return [raw]
            else:
                return []

    def validate_phone_number(self, raw):
        # match all countries if using area_code.get_all_country_iso_two_letter_code()
        # may include too short phone numbers if use 'DE'
        country_code_list = ['US', 'CN', 'IN', 'UA', 'JP', 'RU', 'IT', 'DE', 'CA', 'TR']
        for country_code in country_code_list:
            rtn = self.validate_phone_number_with_coutry_code(raw, country_code=country_code)
            if rtn:
                return rtn

    def is_datetime(self, raw):

        size = len(raw)

        date_format = ''
        if size == 14:
            return is_valid_datetime(raw, '%Y%m%d%H%M%S')
        elif size == 8:
            return is_valid_datetime(raw, '%Y%m%d')
        elif size == 6:
            return is_valid_datetime(raw, '%Y%m%d') or is_valid_datetime(raw, '%H%M%S')
        else:
            return False

    re_num_digits = [
        None,
        re.compile(r"\d{1}"),
        re.compile(r"\d{2}"),
        re.compile(r"\d{3}"),
        re.compile(r"\d{4}"),
        re.compile(r"\d{5}"),
        re.compile(r"\d{6}")
    ]

    def is_all_dup_digits(self, raw):
        for i in range(1, 6):
            rtn = Validator.re_num_digits[i].findall(raw)
            if len(raw) % i != 0:
                continue
            if all(rtn[0] == rest for rest in rtn):
                return True
        return False


    re_start_zero = re.compile(r'^0+')

    def suggest_most_overlap(self, extracted_phone_list):
        def similar(a, b):
            return SequenceMatcher(None, a, b).ratio()
        potential_invalid, potential_valid = [], []
        for pn in extracted_phone_list:
            if len(pn) == 10:
                potential_valid.append(pn)
            else:
                potential_invalid.append(pn)
        ans = list(potential_valid)
        for pi in potential_invalid:
            if not any(similar(pi, pv) > .7 for pv in potential_valid):
                ans.append(pi)
        return ans

    def validate(self, raw):
        ans = []
        for nums in raw.split('\t'):
            nums = nums.strip()
            nums = Validator.re_start_zero.sub('', nums)

            if len(nums) > 16:
                continue

            if len(Validator.re_zero.findall(nums)):
                continue

            if self.is_all_dup_digits(nums):
                continue

            if self.is_datetime(nums):
                continue
            
            valid = self.validate_phone_number(nums)
            if valid:
                ans.extend(valid)

        ans = list(set(ans))
        ans = self.suggest_most_overlap(ans)

        return ' '.join(ans)

class Normalizer():
    # try extracting from this one live escort reviews pnwrapper 754 307 7279 pnwrapper 49 91 3524432077 you won t be disappointedangel

    re_digits = re.compile(r'(?:(?<=[ \s\b\Aa-zA-Z])[\d ]+(?=[ \s\b\Za-zA-Z]))')

    def normalize(self, cleaned_output, uncleaned_output, output_format='list'):
        # print [_.strip() for _ in Normalizer.re_digits.findall(tokenized_content) if _.strip() != '']
        
        if output_format == 'obfuscation':
            output = []
            for co in cleaned_output.split():
                phonenum = {}
                phonenum['telephone'] = co
                if co in uncleaned_output:
                    phonenum['obfuscation'] = 'False'
                else:
                    phonenum['obfuscation'] = 'True'
                output.append(phonenum)
            return output
        else:
            return cleaned_output.split()


class PhoneNumberExtractor():

    PN_OUTPUT_FORMAT_LIST = 'list'
    PN_OUTPUT_FORMAT_OBFUSCATION = 'obfuscation'

    def __init__(self, _output_format='list'):
        self.preprocessor = Preprocessor()
        self.tokenizer = Tokenizer(source_type='text')
        self.extractor = Extractor()
        self.cleaner = Cleaner()
        self.validator = Validator()
        self.normalizer = Normalizer()
        self.set_output_format(_output_format)

    def set_output_format(self, _output_format):
        # 1. list, 2. obfuscation
        if _output_format not in [PhoneNumberExtractor.PN_OUTPUT_FORMAT_LIST, PhoneNumberExtractor.PN_OUTPUT_FORMAT_OBFUSCATION]:
            raise Exception('output_format should be "list" or "obfuscation"')
        self.output_format = _output_format

    def do_process(self, content, source_type='text', do_preprocess=True, do_tokenize=True, do_clean=True, do_extract=True, do_validate=True):
        if do_preprocess:
            content = self.preprocessor.preprocess(content)

        if do_tokenize:
            self.tokenizer.set_source_type(source_type)
            content = self.tokenizer.tokenize(content)

        if do_clean: 
            content = self.cleaner.clean(content)

        if do_extract:
            content = self.extractor.extract(content)

        if do_validate:
            content = self.validator.validate(content)

        return content

        
    def match(self, content, source_type='text'):
        cleaned_ans = self.do_process(content, source_type=source_type)
        uncleaned_ans = self.do_process(content, source_type=source_type, do_clean=False)
        return self.normalizer.normalize(cleaned_ans, uncleaned_ans, output_format=self.output_format)



if __name__ == '__main__':

    # Samples
    
    from phone_number_extractor import PhoneNumberExtractor
    extractor = PhoneNumberExtractor()

    url_string = "http://2134529851.backpage.com/FemaleEscorts/r-u-t-a-_your-blonde-_-o-b-s-e-s-s-i-o-n-_-23-23-23-23/30688875"
    url_phone_numbers = extractor.match(url_string, source_type='url')
    print url_phone_numbers

    text_string = "Sexy new girl in town searching for a great date wiff u Naughty fresh girl here searching 4 a great date wiff you Sweet new girl in town seeking for a good date with u for80 2sixseven one9zerofor 90hr incall or out call"
    text_phone_numbers = extractor.match(text_string, source_type='text')
    print text_phone_numbers


