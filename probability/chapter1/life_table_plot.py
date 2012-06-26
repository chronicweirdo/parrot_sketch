# -*- coding: utf-8 -*-
'''
Created on Jun 26, 2012

@author: cacovean

A life table is a table that lists for a given number of births the estimated
number of people who will live to a given age. In Appendix C we give a life
table based upon 100,000 births for ages from 0 to 85, both for women and for
men. Show how from this table you can estimate the probability m(x) that a
person born in 1981 would live to age x. Write a program to plot m(x) both
for men and for women, and comment on the differences that you see in the
two cases.

install required scientific libraries: http://www.scipy.org/Download
http://matplotlib.sourceforge.net/users/installing.html
'''
import numpy
import pylab
import matplotlib.pyplot as plt
import re

def tutorialPlot():
    t = numpy.arange(0.0, 1.0+0.01, 0.01)
    print t
    s = numpy.cos(2*2*numpy.pi*t)
    print s
    pylab.plot(t, s)
    
    pylab.xlabel('time (s)')
    pylab.ylabel('voltage (mV)')
    pylab.title('About as simple as it gets, folks')
    pylab.grid(True)
    pylab.savefig('simple_plot')
    
    pylab.show()
    
def testPlot():
    plt.plot([1,2,3,4])
    plt.ylabel('some numbers')
    plt.show()
    
def lifeTablePlot():
    fileIn = open('../resources/life_table_1990.txt', 'r')
    ages = []
    alive = []
    male = []
    female = []
    for line in fileIn:
        numbers = re.findall(r'(\d+)', line)
        for i, v in enumerate(numbers):
            numbers[i] = int(v)
        #print numbers
        ages += [numbers[0]]
        alive += [numbers[1]]
        male += [numbers[2]]
        female += [numbers[3]]
    fileIn.close()
    
    #print ages
    #print alive
    
    p1, = plt.plot(alive, label='alive')
    p2, = plt.plot(male)
    p3, = plt.plot(female)
    plt.legend([p1, p2, p3], ['alive', 'male', 'female'])
    plt.show()
    
lifeTablePlot()