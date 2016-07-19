
import sys
import time
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

docs_ = os.path.expanduser(os.path.join(TEST_DATA_DIR, 'docs.json'))
text_ = os.path.expanduser(os.path.join(TEST_DATA_DIR, 'test.txt'))
url_ = os.path.expanduser(os.path.join(TEST_DATA_DIR, 'url.txt'))

import re
import json
from pnmatcher import PhoneNumberMatcher

class TestMainMethods(unittest.TestCase):
    def setUp(self):
        self.matcher = PhoneNumberMatcher()
        
    def tearDown(self):
        pass

    def test_extractor(self):
        # {"url": "", "title": "", "body": "", "url_ext_gt": [], "text_ext_gt": []}

        input_fh = open(docs_, 'rb')
        lines = input_fh.readlines()
        
        json_obj = json.loads(''.join(lines))
        jsonlines = json_obj['jsonlines']

        total = 0           # total number of tests
        correct = 0         # total corrent number of tests
        missing = 0         # total number of tests that missing some extractions (no missing means that program get all extraction shown in groundtruth)
        error = 0           # total number of tests that get extra error extractions (no error means that there are no any extra extractions that shown in groundtruth)
        
        for jsonline in jsonlines:
            # json_obj = json.loads(jsonline)
            json_obj = jsonline
            
            is_correct = True
            is_error = False
            is_missing = False
            # error_ext = []
            # missing_ext = []

            url = json_obj['url']
            title = json_obj['title']
            body = json_obj['body']
            url_ext_groudtruth = json_obj['url_ext_gt']
            text_ext_groudtruth = json_obj['text_ext_gt']

            url_ext_expect = self.matcher.match(url, source_type='url')
            text_ext_expect = self.matcher.match(' '.join([title, body]), source_type='text')


            if len(url_ext_expect) < len(url_ext_groudtruth) or len(text_ext_expect) < len(text_ext_groudtruth) or len(url_ext_expect) > len(url_ext_groudtruth) or len(text_ext_expect) > len(text_ext_groudtruth):
                is_correct = False

            json_obj.setdefault('url_error', [])
            json_obj.setdefault('url_missing', [])
            json_obj.setdefault('text_error', [])
            json_obj.setdefault('text_missing', [])

            ## url
            # check if error
            for tee in url_ext_expect:
                if tee not in url_ext_groudtruth:
                    json_obj['url_error'].append(tee)
                    is_correct = False
                    is_error = True
            # check if missing
            for ueg in url_ext_groudtruth:
                if ueg not in url_ext_expect:
                    json_obj['url_missing'].append(ueg)
                    is_correct = False
                    is_missing = True

            ## text
            # check if error
            for tee in text_ext_expect:
                if tee not in text_ext_groudtruth:
                    json_obj['text_error'].append(tee)
                    is_correct = False
                    is_error = True
            # check if missing
            for ueg in text_ext_groudtruth:
                if ueg not in text_ext_expect:
                    json_obj['text_missing'].append(ueg)
                    is_correct = False
                    is_missing = True

            if is_error:
                error += 1
            if is_missing:
                missing += 1
            if is_correct:
                correct += 1
            else:
                json_obj['url_ext_ep'] = url_ext_expect
                json_obj['text_ext_ep'] = text_ext_expect

                print json.dumps(json_obj, sort_keys=True, indent=4, separators=(',', ': '))

            total += 1
        
        print 60*'-'
        print 'pass', correct, 'out of', total, 'tests', missing, 'missing,', error, 'error'

        input_fh.close()

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
        # content = "Sweet new chick in town searching 4 a good date wiff uNaughty new chick in town searching for a good date with usix02 two28 4192 80hr in call or outcallDuo dream come true available 145hr 2night.Call 10000-40000"
        # content = '07807 254599  asd 07807-254599 ad 10000-40000 '
        # content = 'Try exxtracting from this one: Live Escort Reviews - 754-307-7279 - 49.99 3524432077 You WON\'T be DISAPPOINTEDANGEL!! - 30'
        # content = 'How about Ad: Live Escort Reviews - 780-442-3705 - ????Naughty Maria*Maria so sweet so Nice????3hrs/$500 or 8hrs/1000 - 587.712.8963 - 28'
        # content = '??? 4? First Time in HI?COMING 22, 25, ????808-462-8138 ????100% Real Pics ???'
        # content = 'Pune Escorts - Pune\'s Best Female Escorts Service, CAll ROHAN? 09921488 433/ 0888866 5466 - Pune escorts - backpage.com'
        # content = 'Try extracting from this one: Live Escort Reviews - 754-3two7-7279 - 49.91 3524432077 You WON\'T be DISAPPOINTEDANGEL!! - 30'
        # content = 'Here is an example of an international number: Student Escort In Dubai | +971501948716, Hey handsome,'
        content = 'Please call me at +9715562644120 fast reservation)'
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
        # content = "http://liveescortreviews.com/ad/philadelphia/602-228-4192/1/310054"
        content = 'http://honolulu.backpage.com/BodyRubs/4-first-time-in-hicoming-22-25-28-808-462-8138-100-real-pics-emerald/5079439'
        content = self.matcher.match(content, source_type='url')
        print content
    

if __name__ == '__main__':
    # unittest.main()

    def run_main_test():
        suite = unittest.TestSuite()
        # suite.addTest(TestMainMethods("test_text_extractor_file"))
        suite.addTest(TestMainMethods("test_text_extractor_string"))
        # suite.addTest(TestMainMethods("test_url_extractor_file"))
        # suite.addTest(TestMainMethods("test_url_extractor_string"))
        
        # suite.addTest(TestMainMethods("test_extractor"))

        runner = unittest.TextTestRunner()
        runner.run(suite)

    run_main_test()

