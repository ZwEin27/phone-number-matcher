
import phonenumbers

class Validator():

    def __init__(self):
        pass
    

    def validate(self, raw):
        ans = []
        for nums in raw.split('\t'):
            nums = nums.strip()
            try:
                print nums
                z = phonenumbers.parse(nums, 'US')
            except Exception as e:
                print e
                continue
            if phonenumbers.is_possible_number(z) and phonenumbers.is_valid_number(z):
                ans.append(nums)
        return ' '.join(ans)


