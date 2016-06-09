
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

    def tokenize(self, raw):
        if self.source_type == SOURCE_TYPE_TEXT:
            self.tokenize_text(raw)
        elif self.source_type == SOURCE_TYPE_URL:
            self.tokenize_url(raw)


    def tokenize_text(self, raw):
        pass

    def tokenize_url(self, raw):
        pass
        

    
