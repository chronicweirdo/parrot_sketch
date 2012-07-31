# -*- coding: utf-8 -*-
'''
Created on Jul 31, 2012

@author: cacovean
'''
import sys

def printBytes(file):
    f = open(file, "rb")
    
    try:
        byte = f.read(1)
        while byte != "":
            # Do stuff with byte.
            print "%x" % ord(byte)
            byte = f.read(1)
    finally:
        f.close()

print sys.argv[0]

printBytes(sys.argv[0])
