"""
remove digit and word combinations that are definitely not for phone numbers
e.g.
Available 24/7 *** 214 784 2976 *** 
24/7 here should be removed

"""
import faerie
import os

TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'faerie_conf')

dictionary_ = os.path.expanduser(os.path.join(TEST_DATA_DIR, 'numbers_dictionary.json'))
documents_ = os.path.expanduser(os.path.join(TEST_DATA_DIR, 'numbers_documents.json'))
config_ = os.path.expanduser(os.path.join(TEST_DATA_DIR, 'numbers_config.json'))


class Preprocessor():

    def __init__(self):
        pass

    def clean(self, raw):
        raw = faerie.run(dictionary_,documents_,config_)

        return raw

    def preprocess(self, raw):
        raw = self.clean(raw)


