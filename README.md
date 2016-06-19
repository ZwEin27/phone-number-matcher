# phone-number-matcher

A python tool to extract phone number from url or text 

## About

The phone-number-matcher aims to extract phone numbers from url and text for [DIG](http://usc-isi-i2.github.io/dig/) project. The precision is more important than recall, and thus a phone number validator is added at the end of extraction process based on Google's [libphonenumber](https://github.com/googlei18n/libphonenumber).

## Credit

### Library
- [python-phonenumbers](https://github.com/daviddrysdale/python-phonenumbers)
- [dig-sparkutil](https://github.com/usc-isi-i2/dig-sparkutil)

### Resource
- [Country List](http://www.andrewpatton.com/countrylist.html)