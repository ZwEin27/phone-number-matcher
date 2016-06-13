import re
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'vendor'))
import en
import re
class Cleaner():

    def __init__(self):
        pass

    def clean_digits(self, raw):
        raw = re.sub(r"(oh|o)", "0", raw, flags=re.I)
        raw = re.sub(r"(i|l)", "1", raw, flags=re.I)
        return raw

    # def clean_non_phone_number(self, raw):
    #     for nums in raw.split('\t'):
    #         if len(nums) <

    def clean(self, raw):

        raw = self.clean_digits(raw)

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

    

        




        