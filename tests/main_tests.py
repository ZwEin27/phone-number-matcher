import sys
import time
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

text_ = os.path.expanduser(os.path.join(TEST_DATA_DIR, 'test.txt'))

from pnmatcher.core.tokenizer import Tokenizer
from pnmatcher.core.extractor import Extractor

class TestMainMethods(unittest.TestCase):
    def setUp(self):
        self.tokenizer = Tokenizer(source_type='text')
        self.extractor = Extractor()

    def tearDown(self):
        pass

    def test(self):
        output_fh = open(text_+'.phm', 'wb')
        with open(text_, 'rb') as f:
            for content in f:
                content = self.tokenizer.tokenize(content)
                content = self.extractor.extract(content)
                if content:
                    output_fh.write(str(content))
                output_fh.write('\n')
        output_fh.close()



    

if __name__ == '__main__':
    # unittest.main()

    def run_main_test():
        suite = unittest.TestSuite()
        suite.addTest(TestMainMethods("test"))
        runner = unittest.TextTestRunner()
        runner.run(suite)

    run_main_test()



