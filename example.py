from pnmatcher import PhoneNumberMatcher
matcher = PhoneNumberMatcher()

url_string = "YOU_URL_DATA"
url_phone_numbers = matcher.match(url_string, source_type='url')
# []

text_string = "YOU_TEXT_DATA"
text_phone_numbers = matcher.match(text_string, source_type='text')
# []





