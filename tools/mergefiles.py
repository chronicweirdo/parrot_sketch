# -*- coding: utf-8 -*-
'''
Created on Aug 28, 2012

@author: cacovean
'''
import sys

def copyFile(fileIn, fileOut):
    byte = fileIn.read(1)
    while byte != "":
        # Do stuff with byte.
        fileOut.write(byte)
        byte = fileIn.read(1)
    
def mergeFiles(path1, path2, patho):
    f1 = open(path1, "rb")
    f2 = open(path2, "rb")
    fo = open(patho, "wb")
    try:
        copyFile(f1, fo)
        copyFile(f2, fo)
    finally:
        f1.close()
        f2.close()
        fo.close()
     
root = "D:\\Workspaces\\eclipse\\parrot_sketch\\tools\\"   
p1 = root + 'readmyself.py'
p2 = root + 'test1.zip'
po = root + 'readmyself2.py'
mergeFiles(p1, p2, po)
        
    