import re
import sys
import os
from string import maketrans

# sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'vendor'))
# import en
import re
class Cleaner():

    def __init__(self):
        pass

    def clean_digits(self, raw):
        REG = r'(.*)(\d+[(oils|oh)]+\d+)(.*)'
        if re.match(REG, raw):
            raw = re.sub(REG, '\g<1>\t\g<2>\t\g<3>', raw, re.I)
            raw = raw.split('\t')

            intab = "oils"
            outtab = "0115"
            trantab = maketrans(intab, outtab)
            raw[1] = raw[1].translate(trantab, 'h')
            raw = ''.join(raw)
        return raw

    # def clean_non_phone_number(self, raw):
    #     for nums in raw.split('\t'):
    #         if len(nums) <

    def clean(self, raw):
        raw = raw.split('\t')
        for i in range(len(raw)):
            raw[i] = self.clean_digits(raw[i])
        raw = '\t'.join(raw)
        
        # remove alphbets
        raw = re.sub(r'[a-zA-Z]', ' ', raw)

        # if raw:
        #     print re.findall(r'\b[a-z]+\b', raw, re.I)
        # self.clean_non_phone_number(raw)
        return raw.strip()

    # def clean_numbers_list(self, nums_list):
    #     for nums in nums_list:
    #         for i in range(len(nums)):
    #             nums[i] = self.clean(nums[i])
    #     return nums_list

    

        



# raw = re.sub(r"(oh|o)", "0", raw, flags=re.I)
# raw = re.sub(r"(i|l)", "1", raw, flags=re.I)
# raw = re.sub(r"(s)", "5", raw, flags=re.I)
        