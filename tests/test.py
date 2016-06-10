
import re
units = ['lbs', 'kg']

token ='hellokg'
if re.search('('+"|".join(units)+')', token):
    print 'here'


