'''
Created on Jul 5, 2012

@author: cacovean
'''

inPath = 'C:\Users\cacovean\Desktop\git_cup_midified_files.txt'
fileIn = open(inPath, 'r')

linesSet = []
for line in fileIn:
    if not line in linesSet:
        linesSet += [line]
 
fileIn.close()

for line in sorted(linesSet):
    print line,