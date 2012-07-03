# -*- coding: utf-8 -*-
'''
Created on Jul 3, 2012

@author: cacovean
'''

import random
import datetime
import math
random.seed(datetime.datetime.now())

def getPoint():
    return (random.random(), random.random())

def inCircle(point):
    y, x = point
    r = .5
    d = math.sqrt(math.pow(.5-y,2) + math.pow(.5-x,2))
    return d <= r

def estimateArea(steps):
    inside = 0
    outside = 0
    while steps:
        point = getPoint()
        if inCircle(point):
            inside += 1
        else:
            outside += 1
        steps -= 1
    return float(inside) / (inside + outside)

def estimatePi(steps):
    area = estimateArea(steps)
    myPi = area / (.5 * .5)
    return myPi

p = getPoint()
print p, inCircle(p)

#print estimateArea(1000)
#print estimateArea(10000)
#print estimateArea(100000)
#print estimateArea(1000000)
print estimatePi(100000)