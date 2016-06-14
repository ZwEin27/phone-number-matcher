import sys
import os
import argparse
import re
from pyspark import SparkContext
from digSparkUtil.fileUtil import FileUtil

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from pnmatcher import PhoneNumberMatcher

def load_jsonlines(sc, input, file_format='sequence', data_type='json', separator='\n'):
    fUtil = FileUtil(sc)

    rdd_strings = fUtil.load_file(input, file_format=file_format, data_type=data_type, separator=separator)

    return rdd_strings

def extract_content(raw):
    if not raw:
        return ''
    content = []
    if isinstance(raw, basestring):
        content.append(raw)
    else:
        content = raw
    return ' '.join(content)

def run(sc, input_file, output_dir):

    def map_load_data(data):
        key, json_obj = data

        doc_id = json_obj['doc_id']

        if 'url' in json_obj:
            url = extract_content(json_obj['url'])

        extractions = json_obj['extractions']

        text_data = [] 
        if 'title' in extractions and 'results' in extractions['title']:
            title = extract_content(extractions['title']['results'])
            text_data.append(title)

        if 'text' in extractions and 'results' in extractions['text']:
            text = extract_content(extractions['text']['results'])
            text_data.append(text)

        text_data = ' '.join(text_data)

        # for test only
        phonenumber = None
        if 'phonenumber' in extractions and 'results' in extractions['phonenumber']:
            phonenumber = extract_content(extractions['phonenumber']['results'])

        # in production
        # return (key, [url, text_data])

        # in test
        return (key, [url, text_data, phonenumber])

    def map_extract_phone_number(data):
        # in production
        # key, (url, text) = data

        # in test
        key, (url, text, phonenumber) = data

        matcher = PhoneNumberMatcher()
        url_phone_numbers = matcher.match(url, source_type='url')
        text_phone_numbers = matcher.match(text, source_type='text')

        return (key, [url_phone_numbers.split(), text_phone_numbers.split(), phonenumber])

    rdd = load_jsonlines(sc, input_file)
    rdd = rdd.map(map_load_data).map(map_extract_phone_number)
    rdd.saveAsTextFile(output_dir)

    # for line in rdd.collect()[30:31]:
    #     print line


