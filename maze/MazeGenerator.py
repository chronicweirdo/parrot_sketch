# -*- coding: utf-8 -*-
'''
Created on Jul 1, 2012

@author: silviu
'''
import sys
import random
import datetime
import math
import numpy

random.seed(datetime.datetime.now())

def direction():
    if random.random() > 0.5:
        return 1
    return -1

def choose(clist, cprobabilities):
    # remove 0 probability items
    list = []
    probabilities = []
    for i, v in enumerate(cprobabilities):
        if v != 0.0:
            list += [clist[i]]
            probabilities += [v]
    if len(list) == 0:
        return clist[0]
    r = random.random()
    #print "r:", r
    #print "l:", list
    #print "p:", probabilities
    for i in range(len(probabilities)):
        if r < probabilities[i]:
            #print "chose", i
            return list[i]
        r -= probabilities[i]
    return list[-1:][0]



def extractSurroundingMatrix(matrix, y, x):
    sy = 0 if y-1<0 else y-1
    ey = len(matrix) if y+2>len(matrix) else y+2
    sx = 0 if x-1<0 else x-1
    ex = len(matrix[0]) if x+2>len(matrix) else x+2
    minmatrix = matrix[sy:ey]
    for i, line in enumerate(minmatrix):
        minmatrix[i] = line[sx:ex]
    return minmatrix

def computePositionScore(matrix, y, x):
    """checks all adjacent positions and adds their values, a higher score means
    more walls"""
    mm = extractSurroundingMatrix(matrix, y, x)
    center = 0
    if (0 <= y and y < len(matrix) and 0 <= x and x < len(matrix[0])): center = 1 - matrix[y][x]
    centerWeight = 5
    score = float(sum(flatten(mm)) + center * centerWeight)/(len(mm)*len(mm[0]) + centerWeight)
    return score
    
def computeStepProbabilities(matrix, y, x, steps = [(0,1), (0,-1), (1,0), (-1, 0)], previousPositions = []):
    positions = []
    for (dy, dx) in steps:
        positions += [(y + dy, x + dx)]
    scores = [computePositionScore(matrix, cy, cx) for cy, cx in positions]
    #make previous positions zero
    for i, p in enumerate(positions):
        if p in previousPositions:
            scores[i] = 0
    sscores = sum(scores)
    normalizedScores = []
    if sscores == 0:
        normalizedScores = [0 for i in scores]
    else:
        normalizedScores = [i/sscores for i in scores]
    #print "p:", positions
    #print "s:", normalizedScores
    return normalizedScores

def step(matrix, y, x, positions = []):
    steps = [(0,1), (0,-1), (1,0), (-1, 0)]
    stepProbabilities = computeStepProbabilities(matrix, y, x, steps, positions)
    return choose(steps, stepProbabilities)

def move():
    dir = direction()
    if (dir > 0):
        return (direction(), 0)
    else:
        return (0, direction())
    
def printMatrix(matrix):
    # first convert matrix
    cmatrix = []
    for line in matrix:
        s = ''
        for elem in line:
            if elem == 0:
                s += '  '
            else:
                #s += '██'
                ts = u'\u2588\u2588'
                s += ts
                if (len(ts) > 2):
                    sys.stdout.write('!!!' + ts)
        cmatrix += [s]
    for s in cmatrix:
        print s
        
def wallMaze(w, h):
    maze = []
    for i in range(h):
        line = []
        for j in range(w):
            line += [1]
        maze += [line]
    return maze
        
def walk(matrix, y, x, positions = []):
    #print y, x, len(matrix), len(matrix[0])
    if (y >= len(matrix) or x >= len(matrix[0]) or y < 0 or x < 0):
        return
    matrix[y][x] = 0
    positions += [(y, x)]
    #print positions
    #printMatrix(matrix)
    #print
    ny, nx = step(matrix, y, x, positions)
    walk(matrix, ny + y, nx + x, positions)

# normal distribution = (1/(sigma*sqrt(2*pi))*e^((-1/2)*((x-miu)/sigma)^2)
def normalD(sigma, miu, x):
    nd = 1 / (sigma * math.sqrt(2*math.pi))
    ndpow = (-1/2) * math.pow((x - miu) / sigma, 2)
    nd *= math.pow(math.e, ndpow)
    return nd

def getStandardDistributionForList(list):
    """for standard distribution, miu = 0 and sigma^2 = 1 is the standard normal
     distribution"""
    return [normalD(1, 0, i) for i in numpy.linspace(-1, 1, len(list))]

def chooseStartingPosition(matrix):
    h = [i for i in range(len(matrix))]
    w = [i for i in range(len(matrix[0]))]
    sy = choose(h, getStandardDistributionForList(h))
    sx = choose(w, getStandardDistributionForList(w))
    return (sy, sx)

def flatten(matrix):
    return [item for sublist in matrix for item in sublist]


matrix = wallMaze(75, 35)
msum = sum(flatten(matrix))/float(len(matrix)*len(matrix[0]))    
#printMatrix(matrix)
print
while msum > 0.8:
    y, x = chooseStartingPosition(matrix)
    walk(matrix, y, x)
    msum = sum(flatten(matrix))/float(len(matrix)*len(matrix[0]))
printMatrix(matrix)
print msum
'''
y, x = chooseStartingPosition(matrix)
print y, x
print computeStepProbabilities(matrix, y, x)

list = [1, 2, 3, 4]
print list[-1:][0]
'''