'''
Created on Jul 9, 2012

@author: cacovean
'''
def bits(f):
    bts = (ord(b) for b in f.read())
    print bts
    for b in bts:
        for i in xrange(8):
            yield (b >> i) & 1

filename = 'C:\\Users\\cacovean\\Desktop\\test.zip'
size = 0

for b in bits(open(filename, 'r')):
    print b
    size += 1
print
print size