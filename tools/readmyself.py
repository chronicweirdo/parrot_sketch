# -*- coding: utf-8 -*-
'''
Created on Jul 31, 2012

@author: cacovean
'''
import sys, os

SIZE = 577

def printBytes(file, start):
    f = open(file, "rb")
    f.seek(start)
    size = 0
    try:
        byte = f.read(1)
        while byte != "":
            # Do stuff with byte.
            print "%x" % ord(byte)
            byte = f.read(1)
            size += 1
    finally:
        f.close()
        
    print 'size: ', size

print sys.argv[0]
statinfo = os.stat(sys.argv[0])
print 'size: ', statinfo.st_size

printBytes(sys.argv[0], SIZE)
"""
this is zip data at the end of the file
"""