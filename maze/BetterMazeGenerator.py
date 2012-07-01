# -*- coding: utf-8 -*-
'''
Created on Jul 1, 2012

@author: silviu
'''
import sys

def printMatrix(matrix):
    for line in matrix:
        for v in line:
            sys.stdout.write(str(v))
        print 
    print

def allPossibilities(matrix, y, x):
    #print y, x
    if (y >= len(matrix) or x >= len(matrix[0])):
        if (matrix[1][1] == 0):
            #printMatrix(matrix)
            print matrix
        return
    for i in range(2):
        matrix[y][x] = i
        ny, nx = y, x+1
        if nx >= len(matrix[0]):
            ny += 1
            nx = 0
        allPossibilities(matrix, ny, nx)
        
h, w = 3, 3
matrix = [[1 for i in range(w)] for i in range(h)]

allPossibilities(matrix, 0, 0)