# import datetime
# def validate(date_text):
#     try:
#         datetime.datetime.strptime(date_text, '%Y%m%d')
#     except ValueError:
#         raise ValueError("Incorrect data format, should be YYYY-MM-DD")
# validate('20031233')
# from dateutil.parser import parse
# try:
#     if parse("20040925101010"):
#         return True
# except ValueError:
#     return False

# cclist = ['BD', 'BF', 'BA', 'BB', 'WF', 'BM', 'BO', 'BI', 'BJ', 'BT', 'JM', 'BV', 'BW', 'BR', 'BS', 'JE', 'BY', 'BZ', '', 'RU', 'RW', 'TL', 'RE', 'TJ', 'RO', 'TK', 'GW', 'GU', 'GT', 'GS', 'GR', 'GQ', 'GP', 'JP', 'GY', 'GG', 'GF', 'GE', 'GD', 'GB', 'GN', 'GL', 'GI', 'GH', 'OM', 'TN', 'JO', 'TA', 'HT', 'HK', 'HN', 'HM', 'VE', 'PR', 'PS', 'PW', 'PT', 'KN', 'PY', 'AI', 'PF', 'PG', 'PK', 'PH', 'PN', 'PL', 'PM', 'ZM', 'EH', 'EG', 'ZA', 'IT', 'VN', 'ET', 'SO', 'KY', 'ES', 'ME', 'MG', 'MA', 'MC', 'UZ', 'MM', 'ML', 'MO', 'MN', 'MH', 'MU', 'MW', 'MQ', 'MP', 'MS', 'IM', 'UG', 'MY', 'MX', 'FR', 'SH', 'FK', 'FO', 'NL', 'NA', 'NC', 'NE', 'NF', 'NZ', 'NR', 'NU', 'CK', 'CI', 'CH', 'CN', 'CM', 'CL', 'CC', 'CA', 'CG', 'CD', 'CZ', 'CX', 'CS', 'KG', 'KE', 'KI', 'KM', 'ST', 'SK', 'SN', 'SM', 'SL', 'SC', 'KZ', 'SG', 'SD', 'DO', 'DM', 'DJ', 'VG', 'YE', 'US', 'YT', 'UM', 'LC', 'LA', 'TV', 'TT', 'TR', 'LK', 'LT', 'TF', 'TD', 'TC', 'LY', 'VA', 'AC', 'VC', 'AD', 'AG', 'AF', 'VI', 'IS', 'IR', 'AO', 'AN', 'AQ', 'AS', 'AR', 'AU', 'IO', 'IN', 'TZ', 'AZ', 'UA', 'QA', 'MZ']


# """ phonenumbers
import phonenumbers
from phonenumbers.phonenumberutil import NumberParseException
# z = phonenumbers.parse("213234345632344567896269876543", 'US')
pn = "22737343"
count = 0
for cc in cclist:
    try:
        z = phonenumbers.parse(pn, cc)
        if phonenumbers.is_possible_number(z) and phonenumbers.is_valid_number(z):
            count += 1
            print cc
    except Exception, e:
        pass        
    
print count


# try:
#     z = phonenumbers.parse(pn, 'BG')
# except NumberParseException, e:
#     if e.error_type == NumberParseException.INVALID_COUNTRY_CODE:
#         # Invalid country code specified
#         pass
#     elif e.error_type == NumberParseException.NOT_A_NUMBER:
#         # The string passed in had fewer than 3 digits in it.
#         # The number failed to match the regular expression
#         pass
#     elif e.error_type == NumberParseException.TOO_SHORT_AFTER_IDD:
#         # The string started with an international dialing prefix
#         # but after this was removed, it had fewer digits than any
#         # valid phone number (including country code) could have.
#         pass
#     elif e.error_type == NumberParseException.TOO_SHORT_NSN:
#         # After any country code has been stripped, the string
#         # had fewer digits than any valid phone number could have.
#         pass

#     elif e.error_type == NumberParseException.TOO_LONG:
#         # String had more digits than any valid phone number could have
#         pass

#     print e.error_type, e._msg
# else:
#     print phonenumbers.is_possible_number(z)
#     print phonenumbers.is_valid_number(z)

# """

""" test re
import re

# raw = '2th0usand'
# print re.findall(r'([a-zA-Z]+)', raw, re.I)
from string import maketrans
text = "rachel5678683300"
# text = re.sub(r'(oh|o)', '0', text)
REG = r'(.*)(\d+[(oils|oh)]+\d+)(.*)'
if re.match(REG, text):
    text = re.sub(REG, '\g<1>\t\g<2>\t\g<3>', text, re.I)
    text = text.split('\t')

    intab = "oils"
    outtab = "0115"
    trantab = maketrans(intab, outtab)
    text[1] = text[1].translate(trantab, 'h')
    text = ''.join(text)

# text = re.sub(r'(\$\d+|24/7|\d+\'\d+)', '', text)
# text = re.sub(r'\$\d+', '', text)
# text = re.sub(r"(.*)(\w)(.*)","\g<1>\g<2>\g<3>", text).split()
# text = re.sub(r'[ _-]+(oh|o)[ _-]+', ' 0 ', text)
# text = re.sub(r"(oh|o)", "0", text, flags=re.I)
# text = re.sub(r"(.*)(twenty[\\W_]{0,3})(\d)(.*)","\g<1>2\g<3>\g<4>", text).split()
# text = re.sub(r"twenty[\\W_]{0,3}\d", "2\d", text, flags=re.I)
# text = re.sub(r"twenty", "20", text, flags=re.I)
print text

"""

"""
{"number": "zero", "id": "0"}
{"number": "one", "id": "1"}
{"number": "two", "id": "2"}
{"number": "three", "id": "3"}
{"number": "four", "id": "4"}
{"number": "five", "id": "5"}
{"number": "six", "id": "6"}
{"number": "seven", "id": "7"}
{"number": "eight", "id": "8"}
{"number": "nine", "id": "9"}
{"number": "ten", "id": "10"}
{"number": "eleven", "id": "11"}
{"number": "twelve", "id": "12"}
{"number": "thirteen", "id": "13"}
{"number": "fourteen", "id": "14"}
{"number": "fifteen", "id": "15"}
{"number": "sixteen", "id": "16"}
{"number": "seventeen", "id": "17"}
{"number": "eighteen", "id": "18"}
{"number": "nineteen", "id": "19"}
{"number": "twenty", "id": "20"}
{"number": "twenty-one", "id": "21"}
{"number": "twenty-two", "id": "22"}
{"number": "twenty-three", "id": "23"}
{"number": "twenty-four", "id": "24"}
{"number": "twenty-five", "id": "25"}
{"number": "twenty-six", "id": "26"}
{"number": "twenty-seven", "id": "27"}
{"number": "twenty-eight", "id": "28"}
{"number": "twenty-nine", "id": "29"}
{"number": "thirty", "id": "30"}
{"number": "thirty-one", "id": "31"}
{"number": "thirty-two", "id": "32"}
{"number": "thirty-three", "id": "33"}
{"number": "thirty-four", "id": "34"}
{"number": "thirty-five", "id": "35"}
{"number": "thirty-six", "id": "36"}
{"number": "thirty-seven", "id": "37"}
{"number": "thirty-eight", "id": "38"}
{"number": "thirty-nine", "id": "39"}
{"number": "forty", "id": "40"}
{"number": "forty-one", "id": "41"}
{"number": "forty-two", "id": "42"}
{"number": "forty-three", "id": "42"}
{"number": "forty-four", "id": "42"}
{"number": "forty-two", "id": "42"}
{"number": "forty-two", "id": "42"}
{"number": "forty-two", "id": "42"}
{"number": "forty-two", "id": "42"}
{"number": "forty-two", "id": "42"}
{"number": "forty-two", "id": "42"}
{"number": "forty-two", "id": "42"}
{"number": "forty-two", "id": "42"}
{"number": "ten", "id": "10"}
{"number": "ten", "id": "10"}
{"number": "ten", "id": "10"}
{"number": "ten", "id": "10"}
{"number": "ten", "id": "10"}
{"number": "ten", "id": "10"}
{"number": "ten", "id": "10"}
{"number": "ten", "id": "10"}
{"number": "ten", "id": "10"}
{"number": "ten", "id": "10"}
{"number": "ten", "id": "10"}
{"number": "ten", "id": "10"}
{"number": "ten", "id": "10"}
{"number": "ten", "id": "10"}
{"number": "ten", "id": "10"}
{"number": "ten", "id": "10"}
"""