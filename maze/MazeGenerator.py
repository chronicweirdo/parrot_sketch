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

sys.setrecursionlimit(10000)
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
    ex = len(matrix[0]) if x+2>len(matrix[0]) else x+2
    #print sy, ey, sx, ex
    minmatrix = matrix[sy:ey]
    finminmatrix = []
    for line in minmatrix:
        finminmatrix += [line[sx:ex]]
    return finminmatrix

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
    # stop when reaching the edges
    if (y >= len(matrix) or x >= len(matrix[0]) or y < 0 or x < 0): return
    # stop when reaching an existing tunnel
    
    matrix[y][x] = 0
    positions += [(y, x)]
    #print positions
    #printMatrix(matrix)
    #print
    ny, nx = step(matrix, y, x, positions)
    walk(matrix, ny + y, nx + x, positions)
    
def simpleWalk(matrix, y, x, previousStep = ()):
    matrix[y][x] = 0
    # stop when reaching the edges
    if (y >= len(matrix)-1 or x >= len(matrix[0])-1 or y <= 0 or x <= 0): return    
    # stop when reaching another tunnel
    if (previousStep != (1,0) and matrix[y-1][x] == 0): return
    if (previousStep != (-1,0) and matrix[y+1][x] == 0): return
    if (previousStep != (0,1) and matrix[y][x-1] == 0): return
    if (previousStep != (0,-1) and matrix[y][x+1] == 0): return
    #choose the next step
    steps = [(0,1),(0,-1),(1,0),(-1,0)]
    if previousStep != ():
        steps.remove(previousStep)
    step = random.choice(steps)
    dy, dx = step
    simpleWalk(matrix, y + dy, x + dx, step)
    
def anotherSimpleWalk(matrix, y, x, path = []):
    endCondition = False
    while not endCondition:
        
        # stop when reaching the edges
        if (y >= len(matrix) or x >= len(matrix[0]) or y < 0 or x < 0):
            endCondition = True
            break
        matrix[y][x] = 0
    
        steps = [(y,x+1),(y,x-1),(y+1,x),(y-1,x)]
        #remove steps already visited
        goodSteps = []
        for step in steps:
            if not step in path:
                goodSteps += [step]
        if goodSteps == []:
            endCondition = True
            step = random.choice(steps)
            y, x = step
            break

        step = chooseRandomWalledStep(matrix, goodSteps)
        y, x = step
        path += [step]
    
# generates spirals
def chooseWalledStep(matrix, steps):
    scores = [(computePositionScore(matrix, cy, cx), (cy, cx)) for cy, cx in steps]
    score, step = sorted(scores)[-1:][0]
    return step
    
def chooseRandomWalledStep(matrix, steps):
    scores = [computePositionScore(matrix, cy, cx) for cy, cx in steps]
    sscores = sum(scores)
    normalizedScores = [v/sscores for v in scores]
    return choose(steps, normalizedScores)
        

# normal distribution = (1/(sigma*sqrt(2*pi))*e^((-1/2)*((x-miu)/sigma)^2)
def normalD(sigma, miu, x):
    nd = 1 / (sigma * math.sqrt(2*math.pi))
    ndpow = (-1/2) * math.pow((x - miu) / sigma, 2)
    nd *= math.pow(math.e, ndpow)
    return nd

def getStandardDistributionForList(list):
    """for standard distribution, miu = 0 and sigma^2 = 1 is the standard normal
     distribution"""
    sd = [normalD(1, 0, i) for i in numpy.linspace(-1, 1, len(list))]
    sm = sum(sd)
    sdf = [v/sm for v in sd]
    return sdf

def chooseStartingPosition(matrix):
    h = [i for i in range(len(matrix))]
    w = [i for i in range(len(matrix[0]))]
    sy = choose(h, getStandardDistributionForList(h))
    sx = choose(w, getStandardDistributionForList(w))
    return (sy, sx)

def flatten(matrix):
    return [item for sublist in matrix for item in sublist]

def postProcessMaze(matrix):
    nmatrix = []
    for y in range(len(matrix)):
        line = []
        for x in range(len(matrix[0])):
            mm = extractSurroundingMatrix(matrix, y, x)
            #print y, x, mm
            s = sum(flatten(mm))
            #print s
            if s == 0:
                line += [1]
            else:
                line += [matrix[y][x]]
        nmatrix += [line]
    return nmatrix

matrix = wallMaze(75, 35)
'''
print extractSurroundingMatrix(matrix, 14, 60)

print extractSurroundingMatrix(matrix, 0, 1)
print extractSurroundingMatrix(matrix, 1, 1)
print extractSurroundingMatrix(matrix, 8, 7)
'''
msum = sum(flatten(matrix))/float(len(matrix)*len(matrix[0]))    
#printMatrix(matrix)
print
'''
while msum > 0.8:
    y, x = chooseStartingPosition(matrix)
    #walk(matrix, y, x)
    simpleWalk(matrix, y, x)    
    msum = sum(flatten(matrix))/float(len(matrix)*len(matrix[0]))
'''
for i in range(10):
    y, x = chooseStartingPosition(matrix)
    #print y, x
    anotherSimpleWalk(matrix, y, x)
#printMatrix(matrix)
print msum
printMatrix(postProcessMaze(matrix))
#printMatrix(matrix)
'''
y, x = chooseStartingPosition(matrix)
print y, x
print computeStepProbabilities(matrix, y, x)

list = [1, 2, 3, 4]
print list[-1:][0]

l = [(0.2, (1, 2)), (0.5, (3, 7)), (0.01, (4, 2))]
print l
score, step = sorted(l)[-1:][0]
print score, step
'''