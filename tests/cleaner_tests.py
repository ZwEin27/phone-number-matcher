import sys
import time
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

# text_ = os.path.expanduser(os.path.join(TEST_DATA_DIR, 'text'))


from pnmatcher.core.cleaner import Cleaner

class TestCleanerMethods(unittest.TestCase):
    def setUp(self):
        self.cleaner = Cleaner()

    def tearDown(self):
        pass

    def test_clean(self):
        raw = None
        self.cleaner.clean(raw)

    

if __name__ == '__main__':
    # unittest.main()

    def run_main_test():
        suite = unittest.TestSuite()
        suite.addTest(TestCleanerMethods("test_clean"))
        runner = unittest.TextTestRunner()
        runner.run(suite)

    run_main_test()



