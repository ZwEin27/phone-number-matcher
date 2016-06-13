import sys
import time
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

# text_ = os.path.expanduser(os.path.join(TEST_DATA_DIR, 'test.txt'))
url_ = os.path.expanduser(os.path.join(TEST_DATA_DIR, 'url.txt'))

from pnmatcher.core.common.url import URLHelper
from pnmatcher.core.preprocessor import Preprocessor
from pnmatcher.core.tokenizer import Tokenizer
from pnmatcher.core.extractor import Extractor
from pnmatcher.core.cleaner import Cleaner
from pnmatcher.core.validator import Validator

class TestMainMethods(unittest.TestCase):
    def setUp(self):
        self.url_helper = URLHelper()
        self.preprocessor = Preprocessor()
        self.tokenizer = Tokenizer(source_type='text')
        self.extractor = Extractor()
        self.cleaner = Cleaner()
        self.validator = Validator()

    def tearDown(self):
        pass

    def test(self):
        import re
        output_fh = open(url_+'.phm', 'wb')
        with open(url_, 'rb') as f:
            for content in f:
                # content = re.sub(r" ", "", content)
                content = self.url_helper.clean_url(content)
                content = self.preprocessor.preprocess(content)
                content = self.tokenizer.tokenize(content)
                content = self.extractor.extract(content)
                content = self.cleaner.clean(content)
                # content = self.validator.validate(content)
                if content:
                    output_fh.write(str(content))
                output_fh.write('\n')
                # break
        output_fh.close()
    

if __name__ == '__main__':
    # unittest.main()

    def run_main_test():
        suite = unittest.TestSuite()
        suite.addTest(TestMainMethods("test"))
        runner = unittest.TextTestRunner()
        runner.run(suite)

    run_main_test()



