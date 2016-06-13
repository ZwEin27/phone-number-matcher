"""
remove digit and word combinations that are definitely not for phone numbers
e.g.
Available 24/7 *** 214 784 2976 *** 
24/7 here should be removed

"""
import faerie
import os
import json
import re

FAERIE_CONF_DIR = os.path.join(os.path.dirname(__file__), 'faerie_conf')

dictionary_ = os.path.expanduser(os.path.join(FAERIE_CONF_DIR, 'numbers_dictionary.json'))
# documents_ = os.path.expanduser(os.path.join(TEST_DATA_DIR, 'numbers_documents.json'))
config_ = os.path.expanduser(os.path.join(FAERIE_CONF_DIR, 'numbers_config.json'))

faerie_config = json.loads(open(config_).read())
faerie_dictionary = faerie.readDict(dictionary_, faerie_config)

class Preprocessor():

    def __init__(self):
        pass

    def replace_notable_numbers(self, raw):
        jsonline = {'number': raw, 'id': 'single'}
        # jsonline = json.dumps(raw)
        jsonline = faerie.processDoc(jsonline, faerie_dictionary, faerie_config)

        for entity in jsonline.entities:
            pass
        return jsonline

    def prep_misspelled_numeral_words(self, raw):
        raw = re.sub(r"th0usand", "thousand", raw, flags=re.I)
        raw = re.sub(r"th1rteen", "thirteen", raw, flags=re.I)
        raw = re.sub(r"f0urteen", "fourteen", raw, flags=re.I)
        raw = re.sub(r"e1ghteen", "eighteen", raw, flags=re.I)
        raw = re.sub(r"n1neteen", "nineteen", raw, flags=re.I)
        raw = re.sub(r"f1fteen", "fifteen", raw, flags=re.I)
        raw = re.sub(r"s1xteen", "sixteen", raw, flags=re.I)
        raw = re.sub(r"th1rty", "thirty", raw, flags=re.I)
        raw = re.sub(r"e1ghty", "eighty", raw, flags=re.I)
        raw = re.sub(r"n1nety", "ninety", raw, flags=re.I)
        raw = re.sub(r"fourty", "forty", raw, flags=re.I)
        raw = re.sub(r"f0urty", "forty", raw, flags=re.I)
        raw = re.sub(r"e1ght", "eight", raw, flags=re.I)
        raw = re.sub(r"f0rty", "forty", raw, flags=re.I)
        raw = re.sub(r"f1fty", "fifty", raw, flags=re.I)
        raw = re.sub(r"s1xty", "sixty", raw, flags=re.I)
        raw = re.sub(r"zer0", "zero", raw, flags=re.I)
        raw = re.sub(r"f0ur", "four", raw, flags=re.I)
        raw = re.sub(r"f1ve", "five", raw, flags=re.I)
        raw = re.sub(r"n1ne", "nine", raw, flags=re.I)
        raw = re.sub(r"0ne", "one", raw, flags=re.I)
        raw = re.sub(r"tw0", "two", raw, flags=re.I)
        raw = re.sub(r"s1x", "six", raw, flags=re.I)
        return raw

    def prep_replace_numeral_words(self, raw):
        raw = re.sub(r"hundred", "00", raw, flags=re.I)
        raw = re.sub(r"thousand", "000", raw, flags=re.I)

        raw = re.sub(r"eleven", "11", raw, flags=re.I)
        raw = re.sub(r"twelve", "12", raw, flags=re.I)
        raw = re.sub(r"thirteen", "13", raw, flags=re.I)
        raw = re.sub(r"fourteen", "14", raw, flags=re.I)
        raw = re.sub(r"fifteen", "15", raw, flags=re.I)
        raw = re.sub(r"sixteen", "16", raw, flags=re.I)
        raw = re.sub(r"seventeen", "17", raw, flags=re.I)
        raw = re.sub(r"eighteen", "18", raw, flags=re.I)
        raw = re.sub(r"nineteen", "19", raw, flags=re.I)
        
        raw = re.sub(r"zero", "0", raw, flags=re.I)
        raw = re.sub(r"one", "1", raw, flags=re.I)
        raw = re.sub(r"two", "2", raw, flags=re.I)
        raw = re.sub(r"three", "3", raw, flags=re.I)
        raw = re.sub(r"four", "4", raw, flags=re.I)
        raw = re.sub(r"five", "5", raw, flags=re.I)
        raw = re.sub(r"six", "6", raw, flags=re.I)
        raw = re.sub(r"seven", "7", raw, flags=re.I)
        raw = re.sub(r"eight", "8", raw, flags=re.I)
        raw = re.sub(r"nine", "9", raw, flags=re.I)
        raw = re.sub(r"ten", "10", raw, flags=re.I)

        raw = re.sub(r"(.*)(twenty[\\W_]{0,3})(\d)(.*)","\g<1>2\g<3>\g<4>", raw)
        raw = re.sub(r"(.*)(thirty[\\W_]{0,3})(\d)(.*)","\g<1>3\g<3>\g<4>", raw)
        raw = re.sub(r"(.*)(forty[\\W_]{0,3})(\d)(.*)","\g<1>4\g<3>\g<4>", raw)
        raw = re.sub(r"(.*)(fifty[\\W_]{0,3})(\d)(.*)","\g<1>5\g<3>\g<4>", raw)
        raw = re.sub(r"(.*)(sixty[\\W_]{0,3})(\d)(.*)","\g<1>6\g<3>\g<4>", raw)
        raw = re.sub(r"(.*)(seventy[\\W_]{0,3})(\d)(.*)","\g<1>7\g<3>\g<4>", raw)
        raw = re.sub(r"(.*)(eighty[\\W_]{0,3})(\d)(.*)","\g<1>8\g<3>\g<4>", raw)
        raw = re.sub(r"(.*)(ninety[\\W_]{0,3})(\d)(.*)","\g<1>9\g<3>\g<4>", raw)

        raw = re.sub(r"twenty", "20", raw, flags=re.I)
        raw = re.sub(r"thirty", "30", raw, flags=re.I)
        raw = re.sub(r"forty", "40", raw, flags=re.I)
        raw = re.sub(r"fifty", "50", raw, flags=re.I)
        raw = re.sub(r"sixty", "60", raw, flags=re.I)
        raw = re.sub(r"seventy", "70", raw, flags=re.I)
        raw = re.sub(r"eighty", "80", raw, flags=re.I)
        raw = re.sub(r"ninety", "90", raw, flags=re.I)

        

        return raw
        
        

    def preprocess(self, raw):
        raw = raw.lower()
        # raw = self.replace_notable_numbers(raw)
        raw = self.prep_misspelled_numeral_words(raw)
        raw = self.prep_replace_numeral_words(raw)
        return raw

