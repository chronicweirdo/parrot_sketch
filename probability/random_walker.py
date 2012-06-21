'''
Created on Jun 21, 2012

@author: cacovean
'''
import random
import datetime
import time

random.seed(datetime.datetime.now())
print random.random()

def randomStep():
    return random.random() - 0.5

def differentSign(num1, num2):
    if num1 < 0 and num2 >= 0: return True
    if num1 >= 0 and num2 < 0: return True
    return False

def randomDirection():
    r = random.random()
    if (r < 0.5): return -1
    return 1

def oneDimension():
    # lastTime walker at 0
    walker = 0
    steps = 10000
    changeTimes = []
    lastTime = datetime.datetime.now()
    while steps > 0:
        # move walker
        newWalker = walker + randomStep()
        if differentSign(walker, newWalker):
            # zero was passed
            now = datetime.datetime.now()
            difference = lastTime - now
            lastTime = now
            changeTimes += [difference]
        walker = newWalker
        print walker
        steps-=1;
        time.sleep(0.001)
    # print result
    #for t in changeTimes:
    print len(changeTimes), changeTimes

def oneDimensionFixedStep():
    # lastTime walker at 0
    walker = 0
    steps = 10000
    returnTimes = []
    lastTime = datetime.datetime.now()
    while steps > 0:
        # move walker
        walker += randomDirection()
        if walker == 0:
            # we returned
            now = datetime.datetime.now()
            difference = lastTime - now
            lastTime = now
            returnTimes += [difference]
        print walker
        steps-=1;
        time.sleep(0.001)
    # print result
    #for t in returnTimes:
    print len(returnTimes), returnTimes
        
oneDimensionFixedStep()
#print differentSign(-1, 1), differentSign(1, -1), differentSign(-1, -1), differentSign(1, 1)