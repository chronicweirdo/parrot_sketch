'''
Created on Jul 4, 2012

@author: cacovean
'''

import math
import random

class SimpleNN(object):
    '''
    classdocs
    '''
    learningRate = 0
    momentum = 0
    
    nInput, nHidden, nOutput = 3, 3, 3

    def __init__(self, nInput, nHidden, nOutput):
        '''
        Constructor
        '''
        self.nInput = nInput + 1
        self.nOutput = nOutput + 1
        self.nHidden = nHidden
        
        # initialize layers
        self.input = [0 for i in range(self.nInput-1)] + [-1]
        self.hidden = [0 for i in range(self.nHidden-1)] + [-1]
        self.output = [0 for i in range(self.nOutput)]
        # initialize weights
        self.wInput = [[random.random() for j in range(self.nHidden)] for i in range(self.nInput)]
        self.wHidden = [[random.random() for j in range(self.nOutput)] for i in range(self.nHidden)]
        
    def reset(self):
        pass
    
    def feed(self, inputValues):
        # set inputValues to current value
        self.input = inputValues
        # compute temporary hidden layer
        tHidden = [0 for i in range(self.nHidden)]
        for i in range(self.nHidden):
            tHidden[i] = 0
            for j in range(self.nInput):
                tHidden[i] += self.input[j] * self.wInput[j][i]
        # apply activation function on the temporary hidden layer
        self.hidden = self.activationFunctionLayer(tHidden)
        
        # compute temporary output layer\
        tOut = [0 for i in range(self.nOutput)]
        for i in range(self.nOutput):
            tOut[i] = 0
            for j in range(self.nHidden):
                tOut[i] += self.hidden[j] * self.wHidden[j][i]
        # apply activation function on the temporary output layer
        self.output = self.activationFunctionLayer(tOut)
        
    def backpropagation(self, expectedOutput):
        # update hidden weights
        for i in range(self.nOutput):
            for j in range(self.nHidden):
                targetOutput = expectedOutput[i]
                actualOutput = self.output[i]
                learningRate = .5
                actualWeight = self.wHidden[j][i]
                value = self.hidden[i]
                self.wHidden[j][i] += self.deltaWeight(targetOutput - actualOutput, learningRate, actualWeight, value)
                        
        # obtain hidden output
        expectedHiddenOutput = [0 for i in range(self.nHidden)]
        for i in range(self.nHidden):
            pass
        # update input weights
        for i in range(self.nOutput):
            for j in range(self.nHidden):
                targetOutput = expectedOutput[i]
                actualOutput = self.output[i]
                learningRate = .5
                actualWeight = self.wHidden[j][i]
                value = self.hidden[i]
                self.wHidden[j][i] += self.deltaWeight(targetOutput, actualOutput, learningRate, actualWeight, value)
        

    def deltaWeight(self, error, learningRate, actualWeight, input):
        dw = learningRate * error * self.derivatedActivationFunction(actualWeight * input) * input;
        return dw
        
    def train(self, inputValues, expectedOutput):
        self.feed(inputValues)
        self.backpropagation(expectedOutput)
        
    
    #def train(self, trainingSet, generalizationSet, validationSet):
        #pass
    
    def activationFunctionLayer(self, layer):
        newLayer = []
        for v in layer:
            newLayer += [self.activationFunction(v)]
        return newLayer
    
    def activationFunction(self, value):
        return 1 / (1 + math.exp(-value))
    
    def derivatedActivationFunction(self, value):
        afv = self.activationFunction(value)
        return afv * (1- afv)
    
'''
nn = SimpleNN(3, 4, 2)
print nn.wInput
print nn.wHidden
input = [random.random() for i in range(nn.nInput)]
expectedOutput = [1 for i in range(nn.nInput)]
nn.train(input, expectedOutput)
print nn.input
print nn.hidden
print nn.output
print nn.wHidden
'''