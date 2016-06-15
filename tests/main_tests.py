import sys
import time
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

docs_ = os.path.expanduser(os.path.join(TEST_DATA_DIR, 'docs.jsonl'))
docs_extraction_ = os.path.expanduser(os.path.join(TEST_DATA_DIR, 'docs_extraction.jsonl'))
text_ = os.path.expanduser(os.path.join(TEST_DATA_DIR, 'test.txt'))
url_ = os.path.expanduser(os.path.join(TEST_DATA_DIR, 'url.txt'))

import re
import json
from pnmatcher import PhoneNumberMatcher
import yaml
from jsoncompare import jsoncompare

class TestMainMethods(unittest.TestCase):
    def setUp(self):
        self.matcher = PhoneNumberMatcher()
        

    def tearDown(self):
        pass

    def test_extractor(self):
        # {"url": "", "title": "", "body": ""}

        input_fh = open(docs_, 'rb')
        output_fh = open(docs_+'.phm', 'wb')
        cmp_ = open(docs_extraction_, 'rb')

        for content in input_fh:
            json_obj = json.loads(content)

            url = json_obj['url']
            title = json_obj['title']
            body = json_obj['body']

            url_extractions = self.matcher.match(url, source_type='url')
            text_extractions = self.matcher.match(' '.join([title, body]), source_type='text')
            
            test_extraction = {}
            test_extraction["url"] = url_extractions.split()
            test_extraction["text"] = text_extractions.split()

            true_extraction = cmp_.readline()

            true_extraction = yaml.safe_load(true_extraction)
            # print test_extraction
            # print true_extraction

            output_fh.write(json.dumps(test_extraction))
            if not jsoncompare.are_same(test_extraction, true_extraction, True)[0]:
                output_fh.write(' != ' + json.dumps(true_extraction))
            output_fh.write('\n')


        input_fh.close()
        output_fh.close()
        cmp_.close()

    def test_text_extractor_file(self):

        output_fh = open(text_+'.phm', 'wb')
        with open(text_, 'rb') as f:
            for content in f:
                content = self.matcher.match(content, source_type='text')
                if content:
                    output_fh.write(str(content))
                output_fh.write('\n')
                # break
        output_fh.close()

    def test_text_extractor_string(self):
        content = "Looking for a night that you will remember? Then look no further gentleman I strive to ensure you enjoy your time spent with me. No one will leave without a smile on their face ;). Our time spent together will ALWAYS be SLOW & SENSUAL , you will NEVER feel rushed. Text me . 646/389/39Five Zero.Call 646-389-3950 . I offer video/photo also, ask me on my profile before calling..."
        content = self.matcher.match(content, source_type='text')
        print content
                

    def test_url_extractor_file(self):

        output_fh = open(url_+'.phm', 'wb')
        with open(url_, 'rb') as f:
            for content in f:
                content = self.matcher.match(content, source_type='url')
                if content:
                    output_fh.write(str(content))
                output_fh.write('\n')
                # break
        output_fh.close()

    def test_url_extractor_string(self):
        content = "http://pune.backpage.com/FemaleEscorts/pune-escorts-punes-best-female-escorts-service-call-rohan-09921488-433-0888866-5466/18257508"
        content = self.matcher.match(content, source_type='url')
        print content


        # 09921488 433 0888866 5466

    

if __name__ == '__main__':
    # unittest.main()

    def run_main_test():
        suite = unittest.TestSuite()
        # suite.addTest(TestMainMethods("test_text_extractor_file"))
        # suite.addTest(TestMainMethods("test_text_extractor_string"))
        # suite.addTest(TestMainMethods("test_url_extractor_file"))
        # suite.addTest(TestMainMethods("test_url_extractor_string"))
        
        suite.addTest(TestMainMethods("test_extractor"))
        runner = unittest.TextTestRunner()
        runner.run(suite)

    run_main_test()



