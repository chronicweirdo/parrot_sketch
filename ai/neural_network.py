'''
Created on Jul 4, 2012

@author: cacovean
'''

import math
import random
import numpy as np
import numpy.linalg

class MNN(object):
    
    def __init__(self, nInput, nHidden, nOutput):
        self.nInput = nInput
        self.nHidden = nHidden
        self.nOutput = nOutput
        
        # initialize layers
        self.layers = [[0 for i in range(self.nInput)] + [-1]]
        self.layers += [[0 for j in range(self.nHidden[i])] + [-1] for i in range(len(nHidden))]
        self.layers += [[0 for i in range(self.nOutput)]]
        
        # initialize weights
        self.weights = []
        for l in range(len(self.layers)-1):
            w, h = len(self.layers[l]), len(self.layers[l+1])
            m = []
            for i in range(h):
                line = []
                for j in range(w):
                    line += [random.random()]
                m += [line]
            self.weights += [m]
    
    def feed(self, input):
        # set input layer value
        self.layers[0][:-1] = input
        
        # run feed forward
        for l in range(len(self.layers)-1):
            lin = np.array(self.layers[l])
            lout = numpy.inner(lin.transpose(), self.weights[l])
            # !!! here the -1 terms should never be updated, i think!!
            self.layers[l+1] = [self.activationFunction(v) for v in lout]

    def activationFunction(self, value):
        return 1 / (1 + math.exp(-value))
    
    def derivatedActivationFunction(self, value):
        afv = self.activationFunction(value)
        return afv * (1- afv)
                
    def backpropagation(self, expectedOutput):
        # compute first delta
        delta = [[self.layers[-1:][0][i] - expectedOutput[i] for i in range(len(expectedOutput))]]
        
        #compute weights
        for l in range(len(self.layers)-2, -1, -1):
            w = np.array(self.weights[l]).transpose()
            print w
            d = np.array(delta[0])
            print d
            gp = 0
            for v in self.layers[l]:
                gp += self.derivatedActivationFunction(v)
            tdelta = numpy.inner(w, d)
            t2delta = [v*gp for v in tdelta]
            delta = [t2delta] + delta

        res1 = self.layers[1:]
        res2 = delta[1:]
        print res1
        print res2
        res3 = [[res1[i][j] - res2[i][j] for j in range(len(res1[i]))] for i in range(len(res1))]
        res4 = [[self.myproduct(self.weights[i][j], res3[i][j]) for j in range(len(res3[i]))] for i in range(len(res3))]
        
        print self.weights
        print res4
        #print self.layers            
        #print delta
        #print res3
        
    def myproduct(self, array, value):
        return [array[i] * value for i in range(len(array))]
    
nn = MNN(3, [4,4,5], 2)
print nn.layers
print nn.weights
nn.feed([1,1,0])
print nn.layers
#print np.inner([1, 2], [[3,4],[5,6]])
nn.backpropagation([1,0])