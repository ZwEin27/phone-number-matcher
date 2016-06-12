"""
remove digit and word combinations that are definitely not for phone numbers
e.g.
Available 24/7 *** 214 784 2976 *** 
24/7 here should be removed

"""
import faerie
import os
import json

FAERIE_CONF_DIR = os.path.join(os.path.dirname(__file__), 'faerie_conf')

dictionary_ = os.path.expanduser(os.path.join(FAERIE_CONF_DIR, 'numbers_dictionary.json'))
# documents_ = os.path.expanduser(os.path.join(TEST_DATA_DIR, 'numbers_documents.json'))
config_ = os.path.expanduser(os.path.join(FAERIE_CONF_DIR, 'numbers_config.json'))

faerie_config = json.loads(open(config_).read())
faerie_dictionary = faerie.readDict(dictionary_, faerie_config)

class Preprocessor():

    def __init__(self):
        pass

    def replace_notable_numbers(self, raw):
        jsonline = {'number': raw, 'id': 'single'}
        # jsonline = json.dumps(raw)
        jsonline = faerie.processDoc(jsonline, faerie_dictionary, faerie_config)



        return jsonline

    def clean(self, raw):
        raw = self.replace_notable_numbers(raw)

        return raw

    def preprocess(self, raw):
        raw = self.clean(raw)
        return raw

