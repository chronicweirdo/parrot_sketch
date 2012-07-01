# -*- coding: utf-8 -*-
'''
Created on Jun 21, 2012

@author: cacovean

Mathematicians have been known to get some of the best ideas while sitting in
a cafe, riding on a bus, or strolling in the park. In the early 1900s the famous
mathematician George P�olya lived in a hotel near the woods in Zurich. He
liked to walk in the woods and think about mathematics. P�olya describes the
following incident:

    At the hotel there lived also some students with whom I usually
    took my meals and had friendly relations. On a certain day one
    of them expected the visit of his fianc�ee, what (sic) I knew, but
    I did not foresee that he and his fianc�ee would also set out for a
    stroll in the woods, and then suddenly I met them there. And then
    I met them the same morning repeatedly, I don�t remember how
    many times, but certainly much too often and I felt embarrassed:
    It looked as if I was snooping around which was, I assure you, not
    the case.
    
This set him to thinking about whether random walkers were destined to
meet.
P�olya considered random walkers in one, two, and three dimensions. In one
dimension, he envisioned the walker on a very long street. At each intersection
the walker flips a fair coin to decide which direction to walk next (see
Figure 1.6a). In two dimensions, the walker is walking on a grid of streets, and
at each intersection he chooses one of the four possible directions with equal
probability (see Figure 1.6b). In three dimensions (we might better speak of
a random climber), the walker moves on a three-dimensional grid, and at each
intersection there are now six different directions that the walker may choose,
each with equal probability (see Figure 1.6c).
The reader is referred to Section 12.1, where this and related problems are
discussed.

(a) Write a program to simulate a random walk in one dimension starting
at 0. Have your program print out the lengths of the times between
returns to the starting point (returns to 0). See if you can guess from
this simulation the answer to the following question: Will the walker
always return to his starting point eventually or might he drift away
forever?

(b) The paths of two walkers in two dimensions who meet after n steps can
be considered to be a single path that starts at (0, 0) and returns to (0, 0)
after 2n steps. This means that the probability that two random walkers
in two dimensions meet is the same as the probability that a single walker
in two dimensions ever returns to the starting point. Thus the question
of whether two walkers are sure to meet is the same as the question of
whether a single walker is sure to return to the starting point.
Write a program to simulate a random walk in two dimensions and see
if you think that the walker is sure to return to (0, 0). If so, P�olya would
be sure to keep meeting his friends in the park. Perhaps by now you
have conjectured the answer to the question: Is a random walker in one
or two dimensions sure to return to the starting point? P�olya answered
this question for dimensions one, two, and three. He established the
remarkable result that the answer is yes in one and two dimensions and
no in three dimensions.

(c) Write a program to simulate a random walk in three dimensions and see
whether, from this simulation and the results of (a) and (b), you could
have guessed P�olya�s result.
'''
import random
import datetime
#import time
random.seed(datetime.datetime.now())

'''
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
'''

def direction():
    if random.random() > 0.5:
        return 1
    return -1

'''
def oneDimensionWalk(steps):
    time = 0
    position = 0
    timesAtZero = []
    for i in range(steps):
        time += 1
        position += direction()
        if position == 0:
            timesAtZero += [time]
    differencesBetweenZero = [(timesAtZero[i] - timesAtZero[i-1])
                              for i in range(1, len(timesAtZero))]
    return (len(differencesBetweenZero), differencesBetweenZero)

#print oneDimensionWalk(1000)

def twoDimensionWalk(steps):
    time = 0
    positionX = 0
    positionY = 0
    timesAtZero = []
    for i in range(steps):
        time += 1
        positionX += direction()
        positionY += direction()
        if positionX == 0 and positionY == 0:
            timesAtZero += [time]
    differencesBetweenZero = [(timesAtZero[i] - timesAtZero[i-1])
                              for i in range(1, len(timesAtZero))]
    return (len(differencesBetweenZero), differencesBetweenZero)
'''

#print twoDimensionWalk(1000)

def atOrigin(position):
    for v in position:
        if v != 0:
            return False
    return True

def nDimensionWalk(dimension, steps):
    time = 0
    position = [0 for i in range(dimension)]
    timesAtZero = []
    for i in range(steps):
        time += 1
        for i, v in enumerate(position):
            position[i] = v + direction();
        if atOrigin(position):
            print 'at origin at time', time
            timesAtZero += [time]
    differencesBetweenZero = [(timesAtZero[i] - timesAtZero[i-1])
                              for i in range(1, len(timesAtZero))]
    if len(timesAtZero) > 0: 
        differencesBetweenZero[0:0] = [timesAtZero[0]]
    return (len(differencesBetweenZero), differencesBetweenZero)

print nDimensionWalk(3, 10000000)
#print nDimensionWalk(3, 10)