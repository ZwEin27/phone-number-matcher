
import phonenumbers
from phonenumbers.phonenumberutil import NumberParseException

class Validator():

    def __init__(self):
        pass
    
    def validate_phone_number(self, raw):
        try:
            z = phonenumbers.parse(raw, 'US')
        except NumberParseException, e:
            if e.error_type == NumberParseException.INVALID_COUNTRY_CODE:
                # Invalid country code specified
                pass
            elif e.error_type == NumberParseException.NOT_A_NUMBER:
                # The string passed in had fewer than 3 digits in it.
                # The number failed to match the regular expression
                pass
            elif e.error_type == NumberParseException.TOO_SHORT_AFTER_IDD:
                # The string started with an international dialing prefix
                # but after this was removed, it had fewer digits than any
                # valid phone number (including country code) could have.
                pass
            elif e.error_type == NumberParseException.TOO_SHORT_NSN:
                # After any country code has been stripped, the string
                # had fewer digits than any valid phone number could have.
                pass

            elif e.error_type == NumberParseException.TOO_LONG:
                # String had more digits than any valid phone number could have
                pass

            # print e.error_type, e._msg
        else:
            if phonenumbers.is_possible_number(z) and phonenumbers.is_valid_number(z):
                return [raw]


    def validate(self, raw):
        ans = []
        for nums in raw.split('\t'):
            nums = nums.strip()
            valid = self.validate_phone_number(raw)
            if valid:
                ans.extend(valid)
        return ' '.join(ans)


