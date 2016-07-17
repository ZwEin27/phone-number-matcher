# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-15 11:22:42
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-16 09:38:29

import re
import sys
import os

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




if __name__ == '__main__':
    normalizer = Normalizer()
    cleaned_output = ['7543077279', '3524432077']
    uncleaned_output = 'try extracting from this one live escort reviews pnwrapper 754 307 7279 pnwrapper 49 91 3524432077 you won t be disappointedangel'
    normalizer.normalize(cleaned_output, uncleaned_output)



