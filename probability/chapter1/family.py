# -*- coding: utf-8 -*-
'''
Created on Jun 25, 2012

@author: cacovean

Estimate, by simulation, the average number of children there would be in
a family if all people had children until they had a boy. Do the same if all
people had children until they had at least one boy and at least one girl. How
many more children would you expect to find under the second scheme than
under the first in 100,000 families? (Assume that boys and girls are equally
likely.)
'''

import random
import datetime
random.seed(datetime.datetime.now())

def boy():
    if (random.random() > .5):
        return True
    return False

def haveChildrenUntilBoy():
    hasBoy = False
    children = 0
    while not hasBoy:
        hasBoy = boy()
        children += 1
    return children

#print haveChildrenUntilBoy()

def haveChildrenUntilBoyAndGirl():
    hasBoy = False
    hasGirl = False
    children = 0
    while not (hasBoy and hasGirl):
        currentChildIsBoy = boy()
        if currentChildIsBoy:
            hasBoy = True
        else:
            hasGirl = True
        children += 1
    return children

#print haveChildrenUntilBoyAndGirl()

def simulateChildrenHaving(size, childrenFunction):
    children = 0
    for i in range(size):
        children += childrenFunction()
    return children / float(size)

#print simulateChildrenHaving(100, haveChildrenUntilBoy)

def simulate(size):
    averageChildrenUntilBoy = simulateChildrenHaving(size, haveChildrenUntilBoy)
    averageChildrenUntilBoyAndGirl = simulateChildrenHaving(size, haveChildrenUntilBoyAndGirl)
    return (averageChildrenUntilBoy, averageChildrenUntilBoyAndGirl, averageChildrenUntilBoyAndGirl - averageChildrenUntilBoy)

print simulate(100000)