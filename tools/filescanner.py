'''
Created on Jul 5, 2012

@author: cacovean
'''

import os, glob

#startFolder = 'C:\Users\cacovean\AppData\Roaming\Microsoft\Windows\Start Menu\Programs'
startFolder2 = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs'

'''
os.chdir(startFolder)
fileList = glob.glob("*.*")
print fileList
'''

os.chdir(startFolder2)
fileList = glob.glob("*.*")
print fileList