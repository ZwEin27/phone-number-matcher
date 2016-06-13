import re
from urlparse import urlparse

class URLHelper():

    def __init__(self):
        pass

    def clean_url(self, url_string):
        SEPARATOR = ' sep '

        url_obj = urlparse(url_string)
        
        # parse netloc
        netloc = url_obj.netloc.split('.')[:-2]   # get rid of port numbers, ext and domain name

        # parse path
        path = url_obj.path.split('/')
        path = [SEPARATOR.join(re.findall(r'\w+', _, re.I)) for _ in path]

        # parse params
        # url_obj.params
        
        # parse query
        # url_obj.query
        return SEPARATOR.join(netloc + path)

if __name__ == '__main__':
    url_string = 'http://delhi.backpage.com:8080/TranssexualEscorts/mahipalpur-new-delhi-call-girls-phone-numberscall-ratan-91-9643094927-mahipalpur/14898871'
    url_helper = URLHelper()
    url_helper.clean_url(url_string)