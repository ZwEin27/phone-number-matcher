import re
import sys
import os

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

        suggest_token = en.spelling.correct(token)
        if en.is_number(suggest_token):
            return True
        return False

    def is_units(self, token):
        units = ['lbs', 'kg']   # need to add more here
        if re.search('('+"|".join(units)+')', token):
            return True
        return False

    def extract(self, raw):
        phone_number_list = []
        tokens = raw.split()

        pn_list = None
        for token in tokens:
            if self.is_number(token):
                if pn_list:
                    pn_list.append(token)
                else:
                    pn_list = [token]
            else:
                if pn_list:
                    # if token is units
                    if not self.is_units(token):
                        phone_number_list.append(pn_list)
                    pn_list = None
        if pn_list:
            phone_number_list.append(pn_list)
        return phone_number_list







        