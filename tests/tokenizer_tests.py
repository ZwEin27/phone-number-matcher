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
        self.tokenizer = Tokenizer(source_type='text')

    def tearDown(self):
        pass

    def test_set_source_type(self):
        self.tokenizer.set_source_type('text')
        assert self.tokenizer.source_type == 'text'
        self.tokenizer.set_source_type('text1')

    def test_tokenize_text(self):
        self.tokenizer.set_source_type('text')
        print self.tokenizer.tokenize("TwO/6/zERo-FouR/0/NiNe-4/eIgHt/1/One")

    

if __name__ == '__main__':
    # unittest.main()

    def run_main_test():
        suite = unittest.TestSuite()
        # suite.addTest(TestTokenizerMethods("test_set_source_type"))
        suite.addTest(TestTokenizerMethods("test_tokenize_text"))
        runner = unittest.TextTestRunner()
        runner.run(suite)

    run_main_test()



