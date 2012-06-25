# -*- coding: utf-8 -*-
'''
Created on Jun 25, 2012

@author: cacovean

Tversky and his colleagues studied the records of 48 of the Philadelphia
76ers basketball games in the 1980�81 season to see if a player had times
when he was hot and every shot went in, and other times when he was cold
and barely able to hit the backboard. The players estimated that they were
about 25 percent more likely to make a shot after a hit than after a miss.
In fact, the opposite was true�the 76ers were 6 percent more likely to score
after a miss than after a hit. Tversky reports that the number of hot and cold
streaks was about what one would expect by purely random effects. Assuming
that a player has a fifty-fifty chance of making a shot and makes 20 shots a
game, estimate by simulation the proportion of the games in which the player
will have a streak of 5 or more hits.
'''

import random
import datetime
random.seed(datetime.datetime.now())

def successfullShot():
    if (random.random() > .5):
        return True
    return False

#print successfullShot()

def game():
    result = []
    for i in range(20):
        result += [successfullShot()]
    return result

def streak(throws, requiredSize):
    streakSize = 0
    for x in throws:
        if x:
            streakSize += 1
            if streakSize >= requiredSize:
                return True
        else:
            streakSize = 0
    return False

#print streak(game(), 5)

def simulateChildrenHaving(games):
    streaks = 0
    for i in range(games):
        if (streak(game(), 5)):
            streaks += 1
    return streaks / float(games)

print simulateChildrenHaving(100)
print simulateChildrenHaving(1000)
print simulateChildrenHaving(10000)
print simulateChildrenHaving(100000)
print simulateChildrenHaving(1000000)