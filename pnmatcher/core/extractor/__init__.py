import re
import sys
import os
import collections

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'vendor'))
import en

class Extractor():

    def __init__(self):
        pass

    def is_number(self, token):
        """
        judge if it is or contain digits, including digit word like 'eight'

        formats:
        2th0usand
        2SIX0--3ONE0--000EIGHT
        5Seven4Three2Two7Zero7Six
        2SIX0--3ONE0--000EIGHT
        """
        
        if re.search(r'\d', token):
            return True

        # suggest_token = en.spelling.correct(token)
        # if en.is_number(suggest_token):
        #     return True
        return False

    def is_units(self, token):
        units = ['lbs', 'kg']   # need to add more here
        if re.search('('+"|".join(units)+')', token):
            return True
        return False

    # numbers_regex = r"(?:(?<=[ ])[\d]+(?=[ ]))"
    numbers_regex = r"(?:(?:[ ]?\d{3}[ ]?\d{7}[ ]?)|[\d ]+)"
    def extract(self, raw):
        raw = re.findall(Extractor.numbers_regex, raw)
        raw = [''.join(_.split()) for _ in raw if len(_.strip()) >= 10]
        
        return '\t'.join(raw)


    """
    def extract(self, raw):
        def add_pn_list(phone_number_list_, pn_list_):
            pn_size_arr_string = ''.join([str(len(_)) for _ in pn_list_])
            results = collections.Counter(pn_size_arr_string)
            print results, pn_list_
            phone_number_list.append(''.join(pn_list))
            
        phone_number_list = []
        tokens = raw.split()

        pn_list = None
        for token in tokens:
            if self.is_number(token):   # and or n or &
                if pn_list:
                    pn_list.append(token)
                else:
                    pn_list = [token]
            else:
                if pn_list:
                    # if token is units
                    if not self.is_units(token):
                        add_pn_list(phone_number_list, pn_list)
                        
                    pn_list = None
        if pn_list:
            add_pn_list(phone_number_list, pn_list)
        return '\t'.join(phone_number_list)
    """







        