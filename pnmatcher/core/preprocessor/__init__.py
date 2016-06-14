"""
preprocess digits that must not belong to phone number

"""
import os
import json
import re



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

    # datetime_regex = r""    # pass and left for validator
    
    # isolate_digits_regex = r"(?:[a-z][\s_-][0-9]{,10}[\s_-][a-z])"

    others_regexes = [r"24/7", r"\d+\'\d+", r"\d+\%"]
    other_regex = r"(?:" + "|".join(others_regexes) + ")"

    all_regexes = [money_regex, unit_regex, other_regex]
    all_regex = r"(" + r"|".join(all_regexes) + ")"
    print "|".join(all_regexes)

    def preprocess(self, raw):
        raw = raw.lower()
        # raw = re.sub(r'(\$\d+|24/7|\d+\'\d+)', '', raw, flags=re.I)
        raw = re.sub(Preprocessor.all_regex, '', raw, flags=re.I)
        return raw


if __name__ == '__main__':
    samples = ['$200tel3365551212', 
                '$276 3235551212',]

    preprocessor = Preprocessor()
    for sample in samples:
        print preprocessor.preprocess(sample)