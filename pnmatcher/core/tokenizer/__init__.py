
import string

from pnmatcher.vendor.crf.crf_tokenizer import CrfTokenizer


SOURCE_TYPE_TEXT = 'text'
SOURCE_TYPE_URL = 'url'

class Tokenizer():

    def __init__(self, source_type='text'):
        self.set_source_type(source_type)
        self.source_type = source_type      # text or url

    def set_source_type(self, source_type):
        """ 
        'text' or 'url'

        """
        st = source_type.lower()
        if source_type.lower() not in [SOURCE_TYPE_TEXT, SOURCE_TYPE_URL] :
            raise Exception(source_type + ' is not a source type, which should be "text" or "url"')

        self.source_type = source_type

    def remove_punctuation(self, raw):
        return raw.translate(string.maketrans("",""), string.punctuation)

    def tokenize(self, raw):
        if self.source_type == SOURCE_TYPE_TEXT:
            return self.tokenize_text(raw)
        elif self.source_type == SOURCE_TYPE_URL:
            return self.tokenize_url(raw)

    def tokenize_text(self, raw):
        t = CrfTokenizer()
        t.setRecognizeHtmlEntities(True)
        t.setRecognizeHtmlTags(True)
        t.setSkipHtmlTags(True)
        t.setRecognizePunctuation(True)
        tokens = t.tokenize(raw)
        tokens = ' '.join(tokens)
        tokens = self.remove_punctuation(tokens)
        return tokens

    def tokenize_url(self, raw):
        pass
   




    