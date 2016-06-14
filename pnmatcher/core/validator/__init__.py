
import phonenumbers
from phonenumbers.phonenumberutil import NumberParseException
from dateutil.parser import parse
from pnmatcher.res import area_code
import re

class Validator():

    def __init__(self):
        pass
    

    def validate_long_pn(self, raw):
        size = len(raw)
        ans = []
        if size % 10 == 0:
            for i in range(size/10):
                ans.extend(self.validate_phone_number(raw[(i)*10:(i+1)*10], country_code='US'))
        return ans

    def validate_phone_number_with_coutry_code(self, raw, country_code='US'):
        try:
            z = phonenumbers.parse(raw, country_code)
        except NumberParseException, e:
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
                # return self.validate_long_pn(raw)
                return []

            # print e.error_type, e._msg
        else:
            if phonenumbers.is_possible_number(z) and phonenumbers.is_valid_number(z):
                return [raw]
            else:
                return []

    def validate_phone_number(self, raw):
        # match all countries if use area_code.get_all_country_iso_two_letter_code()
        country_code_list = ['US', 'CN', 'IN', 'UA', 'JP']
        for country_code in country_code_list:
            rtn = self.validate_phone_number_with_coutry_code(raw, country_code=country_code)
            if rtn:
                return rtn

    def is_datetime(self, raw):
        if len(raw) > 12:
            return False
        try:
            if parse(raw):
                return True
        except ValueError:
            return False

    def validate(self, raw):
        ans = []
        for nums in raw.split('\t'):
            nums = nums.strip()
            nums = re.sub(r'^0+', '', nums, flags=re.I)

            # if self.is_datetime(nums):
            #     continue
            valid = self.validate_phone_number(nums)
            if valid:
                ans.extend(valid)
        return ' '.join(ans)



