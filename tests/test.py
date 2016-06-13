
import re

# raw = '2th0usand'
# print re.findall(r'([a-zA-Z]+)', raw, re.I)

text = 'rache1567 868 3300'
# text = re.sub(r"(.*)(\w)(.*)","\g<1>\g<2>\g<3>", text).split()
text = re.sub(r'[a-zA-Z]', '', text)
# text = re.sub(r"(oh|o)", "0", text, flags=re.I)
# text = re.sub(r"(.*)(twenty[\\W_]{0,3})(\d)(.*)","\g<1>2\g<3>\g<4>", text).split()
# text = re.sub(r"twenty[\\W_]{0,3}\d", "2\d", text, flags=re.I)
# text = re.sub(r"twenty", "20", text, flags=re.I)
print text

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