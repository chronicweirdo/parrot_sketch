'''
Created on Jun 25, 2012

@author: cacovean

You are offered the following game. A fair coin will be tossed until the first
time it comes up heads. If this occurs on the j th toss you are paid 2^j
dollars.
You are sure to win at least 2 dollars so you should be willing to pay to play
this game-but how much? Few people would pay as much as 10 dollars to
play this game. See if you can decide, by simulation, a reasonable amount
that you would be willing to pay, per game, if you will be allowed to make
a large number of plays of the game. Does the amount that you would be
willing to pay per game depend upon the number of plays that you will be
allowed?
'''
import random
import datetime
random.seed(datetime.datetime.now())

def tossHeads():
    if (random.random() > .5):
        return True
    return False

def tossesUntilHeads():
    tosses = 0
    while tossHeads():
        tosses += 1
    return tosses

print tossesUntilHeads()

def moneyWon():
    return 2 ** tossesUntilHeads()

print moneyWon()

def simulateRuns(numberOfRuns):
    moneyIn = 2 * numberOfRuns
    moneyOut = 0
    for i in range(numberOfRuns):
        moneyOut += moneyWon()
    return (moneyIn, moneyOut)

print simulateRuns(10)

def averageWinnings(numberOfPlays, numberOfSimulations):
    winnings = 0
    for i in range(numberOfSimulations):
        moneyIn, moneyOut = simulateRuns(numberOfPlays)
        winnings += moneyOut - moneyIn
    return winnings / float(numberOfSimulations)

print averageWinnings(2, 1000)

def runLargeSimulation():
    """average the winnings for a large number of games with different sizes"""
    numberOfPlays = 1
    numberOfSimulations = 1000
    for i in range(5):
        print numberOfPlays, ': ', averageWinnings(numberOfPlays, numberOfSimulations), '$'
        numberOfPlays *= 10

runLargeSimulation()