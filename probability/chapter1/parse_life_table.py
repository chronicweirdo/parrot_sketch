'''
Created on Jun 26, 2012

@author: cacovean
'''
import re

postDB = []

def scan(inPath, outPath, matches, process, writeUnprocesses=True, preProcess=None, postProcess=None):
    fileIn = open(inPath, 'r')
    fileOut = open(outPath, 'w')

    if preProcess != None:
        preProcess(fileIn, fileOut)
    for line in fileIn:
        if matches(line):
            fileOut.write(process(line))
        else:
            if writeUnprocesses:
                fileOut.write(line)
    if postProcess != None:
        postProcess(fileIn, fileOut)
    
    fileIn.close()
    fileOut.close()

def matchAll(line):
    return True

def matchStartingWithNumbers(line):
    pattern = '^\s*\d.*'
    if re.match(pattern, line) == None: return False
    return True

def noProcess(line):
    return line

def processTableLine(line):
    global postDB
    numbers = re.findall(r'(\d+)', line)
    print numbers
    if len(numbers) == 8:
        newline1 = ''
        newline2 = ''
        for i, v in enumerate(numbers):
            if i == 4:
                newline1 = newline2 + '\n'
                newline2 = ''
            newline2 += v + ' '
        postDB += [newline2 + '\n']
        return newline1
    return ''

def tablePostProcess(fileIn, fileOut):
    for l in postDB:
        fileOut.write(l)

inPath = '../resources/life table raw.txt'
outPath = '../resources/life_table_1990.txt'

scan(inPath, outPath, matchStartingWithNumbers, processTableLine, False, None, tablePostProcess)