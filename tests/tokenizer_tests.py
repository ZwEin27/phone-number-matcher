import sys
import time
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

# text_ = os.path.expanduser(os.path.join(TEST_DATA_DIR, 'text'))

from pnmatcher.core.tokenizer import Tokenizer

class TestTokenizerMethods(unittest.TestCase):
    def setUp(self):
        self.tokenizer = Tokenizer()

    def tearDown(self):
        pass

    def test_set_source_type(self):
        self.tokenizer.set_source_type('text')
        assert self.tokenizer.source_type == 'text'

        self.tokenizer.set_source_type('text1')

    

if __name__ == '__main__':
    # unittest.main()

    def run_main_test():
        suite = unittest.TestSuite()
        suite.addTest(TestTokenizerMethods("test_set_source_type"))
        runner = unittest.TextTestRunner()
        runner.run(suite)

    run_main_test()



