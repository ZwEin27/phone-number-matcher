import os
hbase_ = os.path.join(os.path.dirname(__file__), 'hbase.bin')
# print hbase_

with open(hbase_, 'rb') as f:
    lines = f.readlines()
    for line in lines:
        print line
        print 's'
        break