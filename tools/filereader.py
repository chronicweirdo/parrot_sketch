'''
Created on Jul 5, 2012

@author: cacovean
'''

import shutil
import re
import os

inPath = 'C:\Users\cacovean\Desktop\git_cup_midified_files.txt'


def readLinesSet(fileName):
    fileIn = open(inPath, 'r')
    
    linesSet = []
    for line in fileIn:
        if not line in linesSet:
            linesSet += [line]
     
    fileIn.close()
    
    return linesSet

def commonRoot(string1, string2):
    result = ""
    for i, v in enumerate(string1):
        if i < len(string2) and string2[i] == v:
            result += v
        else:
            break
    return result

#string1 = 'C:\\ucmdbwe10\\newgit\\git-main\\install\\cup_installer\\src\\main\\CUPInstaller\\CUPInstaller.iap_xml'
#string2 = 'C:\\ucmdbwe10\\newgit\\git-main\\install\\cup_installer\\src\\main\\CUPInstaller\\CUPInstallerlocales\\ProjectLocalizationInfo.txt'
#print commonRoot(string1, string2)

def findCommonRoot(linesSet):
    cRoot = linesSet[0]
    for line in linesSet:
        cRoot = commonRoot(line, cRoot)
    return cRoot

def extractRelativeRoot(linesSet, cRoot):
    result = []
    for v in linesSet:
        rel = v[len(cRoot):]
        result += [(v, rel.split('\\'))]
    return result

def preparePath(rootPath, path):
    newPath = rootPath
    for i in range(len(path)-1):
        newPath += '\\' + path[i]
        if not os.path.exists(newPath):
            os.makedirs(newPath)
    newPath += '\\' + path[len(path)-1]
    return newPath

def replaceAll(list, replaceFrom, replaceTo):
    newList = []
    for v in list:
        newList += [v.replace(replaceFrom, replaceTo).replace('\n', '')]
    return newList

#for line in sorted(readLinesSet(inPath)):
#    print line,

def createPatchFolder(folderPath, files):
    for originalFile, relativeFile in files:
        newPath = preparePath(folderPath, relativeFile)
        shutil.copyfile(originalFile, newPath)
        
def backupBeforePatch(backupPath, oldProjectPath, files):
    for originalFile, relativeFile in files:
        newPath = preparePath(backupPath, relativeFile)
        oldPath = preparePath(oldProjectPath, relativeFile)
        if os.path.exists(oldPath):
            shutil.copyfile(oldPath, newPath)

linesSet = readLinesSet(inPath)
linesSet = replaceAll(linesSet, 'C:\\ucmdbwe10\\newgit\\', 'D:\\Workspaces\\ucmdb.10.git\\')
print linesSet
cRoot = findCommonRoot(linesSet)
print cRoot
relRoot = extractRelativeRoot(linesSet, cRoot)
print relRoot
backupBeforePatch('C:\\Users\\cacovean\\Desktop\\cup_installer_patch_backup', 'D:\\Workspaces\\ucmdb.10\\install', relRoot)
#createPatchFolder('C:\\Users\\cacovean\\Desktop\\cup_installer_patch', relRoot)