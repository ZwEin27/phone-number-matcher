import sys
import time
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

# text_ = os.path.expanduser(os.path.join(TEST_DATA_DIR, 'text'))


from pnmatcher.core.extractor import Extractor

class TestExtractorMethods(unittest.TestCase):
    def setUp(self):
        self.extractor = Extractor()
        

    def tearDown(self):
        pass

    def test_extract(self):
        print self.extractor.extract("TwO  6  zERo  FouR  0  NiNe  4  eIgHt  1  One")

    

if __name__ == '__main__':
    # unittest.main()

    def run_main_test():
        suite = unittest.TestSuite()
        suite.addTest(TestExtractorMethods("test_extract"))
        runner = unittest.TextTestRunner()
        runner.run(suite)

    run_main_test()



