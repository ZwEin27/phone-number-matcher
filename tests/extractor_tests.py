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
        self.extractor.extract("I  m 5  6  140 lbs  with a nice plump booty   Available 24  7    214 784 2976      INCALL SPECIALS   NO PIMPS   NO TEXTIN")

    

if __name__ == '__main__':
    # unittest.main()

    def run_main_test():
        suite = unittest.TestSuite()
        suite.addTest(TestExtractorMethods("test_extract"))
        runner = unittest.TextTestRunner()
        runner.run(suite)

    run_main_test()



