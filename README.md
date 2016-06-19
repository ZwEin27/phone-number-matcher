# phone-number-matcher

A python tool to extract phone number from url or text 

## About

The phone-number-matcher aims to extract phone numbers from url and text for [DIG](http://usc-isi-i2.github.io/dig/) project. 

The precision is more important than recall, and thus a phone number validator is added at the end of extraction process based on Google's [libphonenumber](https://github.com/googlei18n/libphonenumber).


## Install

    python setup.py install

or

    pip install pnmatcher

## Example Usage

initialize pnmatcher

    from pnmatcher import PhoneNumberMatcher

    matcher = PhoneNumberMatcher()

use pnmatcher for url

    url_string = "http://2134529851.backpage.com/FemaleEscorts/r-u-t-a-_your-blonde-_-o-b-s-e-s-s-i-o-n-_-23-23-23-23/30688875"

    url_phone_numbers = matcher.match(url_string, source_type='url')

    # print url_phone_numbers
    # ['2134529851']

use pnmatcher for text

    text_string = "Sexy new girl in town searching for a great date wiff u Naughty fresh girl here searching 4 a great date wiff you Sweet new girl in town seeking for a good date with u for80 2sixseven one9zerofor 90hr incall or out call"

    text_phone_numbers = matcher.match(content, source_type='text')

    # print text_phone_numbers
    # ['4802671904']

## Spark Usage

1. upload following four files into your spark environment

- spark_workflow.sh
- spark_workflow.py
- spark_dependencies/python_main.zip
- spark_dependencies/python_lib.zip

2. run `spark_workflow.sh` for spark workflow


## Project Layout

- The `pnmatcher` directory holds the python code.
- The `spark_dependencies` directory contains two zip files that are used for spark workflow.
- The `tests` holds test scripts to evaluate the program.

## Credit

### Library
- [python-phonenumbers](https://github.com/daviddrysdale/python-phonenumbers)
- [dig-sparkutil](https://github.com/usc-isi-i2/dig-sparkutil)

### Resource
- [Country List](http://www.andrewpatton.com/countrylist.html)