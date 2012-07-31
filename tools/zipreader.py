# -*- coding: utf-8 -*-
'''
Created on Jul 31, 2012

@author: cacovean
'''

import os

def toInt(string):
    return int(string[::-1].encode('hex'), 16)

def toHex(string):
    return string[::-1].encode('hex')

#def readFileHeader(f):
def readFile(f):
    '''
    Offset    Bytes    Description
     0    4    Local file header signature = 0x04034b50 (read as a little-endian number)
     4    2    Version needed to extract (minimum)
     6    2    General purpose bit flag
     8    2    Compression method
    10    2    File last modification time
    12    2    File last modification date
    14    4    CRC-32
    18    4    Compressed size
    22    4    Uncompressed size
    26    2    File name length (n)
    28    2    Extra field length (m)
    30    n    File name
    30+n    m    Extra field
    '''
    # read entry signature
    localFileHeaderSignature = f.read(4)
    # verify entry signature
    if toHex(localFileHeaderSignature) != '04034b50':
        f.seek(-4, 1)
        return False
    versionNeededToExtract = f.read(2)
    generalPurposeBitFlag = f.read(2)
    print toInt(generalPurposeBitFlag) & 8
    compressionMethod = f.read(2)
    print toHex(compressionMethod)
    fileLastModificationTime = f.read(2)
    fileLastModificationDate = f.read(2)
    crc32 = f.read(4)
    compressedSize = f.read(4)
    print toInt(compressedSize)
    uncompressedSize = f.read(4)
    fileNameLength = f.read(2)
    extraFieldLength = f.read(2)
    
    n_fileNameLength = toInt(fileNameLength)
    fileName = f.read(n_fileNameLength)
    print fileName
        
    n_extraFieldLength = toInt(extraFieldLength)
    extraField = f.read(n_extraFieldLength)
    
    contents = f.read(toInt(compressedSize))
    
    if toInt(compressedSize) > 0:
    #    writeFile(fileName, contents)
        decompress(compressionMethod, contents)
    
    return True

def readCentralDirectory(f):
    '''
    Offset    Bytes    Description[25]
     0    4    Central directory file header signature = 0x02014b50
     4    2    Version made by
     6    2    Version needed to extract (minimum)
     8    2    General purpose bit flag
    10    2    Compression method
    12    2    File last modification time
    14    2    File last modification date
    16    4    CRC-32
    20    4    Compressed size
    24    4    Uncompressed size
    28    2    File name length (n)
    30    2    Extra field length (m)
    32    2    File comment length (k)
    34    2    Disk number where file starts
    36    2    Internal file attributes
    38    4    External file attributes
    42    4    Relative offset of local file header. This is the number of bytes between the start of the first disk on which the file occurs, and the start of the local file header. This allows software reading the central directory to locate the position of the file inside the ZIP file.
    46    n    File name
    46+n    m    Extra field
    46+n+m    k    File comment
    '''
    # read entry signature
    centralDirectorySignature = f.read(4)
    # verify entry signature
    if toHex(centralDirectorySignature) != '02014b50':
        f.seek(-4, 1)
        return False
    print toHex(centralDirectorySignature)
    versionMadeBy = f.read(2)
    versionNeededToExtract = f.read(2)
    generalPorposeBitFlag = f.read(2)
    compressionMethod = f.read(2)
    fileLastModificationTime = f.read(2)
    fileLastModificationDate = f.read(2)
    crc32 = f.read(4)
    compressedSize = f.read(4)
    uncompressedSize = f.read(4)
    fileNameLength = f.read(2)
    extraFieldLength = f.read(2)
    fileCommentLength = f.read(2)
    diskNumberWhereFileStarts = f.read(2)
    internalFileAttributes = f.read(2)
    externalFileAttributes = f.read(4)
    relativeOffsetOfLocalFileHeader = f.read(4)
    
    fileName = f.read(toInt(fileNameLength))
    print fileName
    
    extraField = f.read(toInt(extraFieldLength))
    fileComment = f.read(toInt(fileCommentLength))
    
    return True
    
    
def writeFile(name, bytes):
    if len(os.path.dirname(name)) > 0:
        if not os.path.exists(os.path.dirname(name)):
            os.makedirs(os.path.dirname(name))
    f = open(name, 'wb')
    f.write(bytes)
    f.close()
    
def readCentralDirectoryEnd(f):
    '''
    Offset    Bytes    Description[25]
     0    4    End of central directory signature = 0x06054b50
     4    2    Number of this disk
     6    2    Disk where central directory starts
     8    2    Number of central directory records on this disk
    10    2    Total number of central directory records
    12    4    Size of central directory (bytes)
    16    4    Offset of start of central directory, relative to start of archive
    20    2    Comment length (n)
    22    n    Comment
    '''
    # read entry signature
    endSignature = f.read(4)
    # verify entry signature
    if toHex(endSignature) != '06054b50':
        f.seek(-4, 1)
        return False
    print toHex(endSignature)
    numberOfThisDisk = f.read(2)
    diskWhereCentralDirectoryStarts = f.read(2)
    numberOfCentralDirectoryRecordsOnThisDisk = f.read(2)
    totalNumberOfCentralDirectoryRecords = f.read(2)
    sizeOfCentralDirectory = f.read(4)
    offsetOfStartOfCentralDirectory = f.read(4)
    commentLength = f.read(2)
    coment = f.read(toInt(commentLength))
    
    return True
    
def decompress(compressionMethod, contents):
    pass
    
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
        
#printBytes("test.zip")

f = open("test1.zip", "rb")
readFileEntries = True
while readFile(f):
    pass
print("////////")
while readCentralDirectory(f):
    pass
print("////////")
readCentralDirectoryEnd(f)
f.close()