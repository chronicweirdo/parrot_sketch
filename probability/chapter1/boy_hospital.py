'''
Created on Jun 25, 2012

@author: cacovean

The psychologist Tversky and his colleagues say that about four out of five
people will answer (a) to the following question:
A certain town is served by two hospitals. In the larger hospital about 45
babies are born each day, and in the smaller hospital 15 babies are born each
day. Although the overall proportion of boys is about 50 percent, the actual
proportion at either hospital may be more or less than 50 percent on any day.

At the end of a year, which hospital will have the greater number of days on
which more than 60 percent of the babies born were boys?
(a) the large hospital
(b) the small hospital
(c) neither-the number of days will be about the same.
Assume that the probability that a baby is a boy is .5 (actual estimates make
this more like .513). Decide, by simulation, what the right answer is to the
question. Can you suggest why so many people go wrong?
'''
import random
import datetime
random.seed(datetime.datetime.now())

largeHospitalBabiesPerDay = 45
smallHospitalBabiesPerDay = 15
babiesPerDayFluctuation = 3
daysInYear = 356
probabilityBabyIsBoy = .5 # .513

def hospitalMaternityDay(babiesPerDay):
    """simulate the birth of babies in a day at the large hospital"""
    babiesBorn = babiesPerDay + random.randint(-babiesPerDayFluctuation, babiesPerDayFluctuation)
    boysBorn = 0
    for i in range(babiesBorn):
        if (random.random() < probabilityBabyIsBoy):
            boysBorn += 1
    return (babiesBorn, boysBorn, boysBorn / float(babiesBorn))

print hospitalMaternityDay(largeHospitalBabiesPerDay)
print hospitalMaternityDay(smallHospitalBabiesPerDay)

def hospitalMaternityYear():
    largeHospitalOverSixtyDays = 0
    smallHospitalOverSixtyDays = 0
    for i in range(daysInYear):
        born, boys, percent = hospitalMaternityDay(largeHospitalBabiesPerDay)
        if percent > .6:
            largeHospitalOverSixtyDays += 1
        born, boys, percent = hospitalMaternityDay(smallHospitalBabiesPerDay)
        if percent > .6:
            smallHospitalOverSixtyDays += 1
    return (largeHospitalOverSixtyDays, smallHospitalOverSixtyDays)

# because more people are born in the large hospital, the slightly increased
# chance deviation/fluctuation of a boy being born is attenuated.
# in the small hospital, this fluctuation is felt more clearly.
# just like in the coin toss problem, as the number of coin tosses increases,
# the proportion of heads gets closer to .5
print hospitalMaternityYear()