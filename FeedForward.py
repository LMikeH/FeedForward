import numpy as np
import neuron as nr 
import random

class feedForward():
    def __init__(self,numins,numouts):
        self.numins = numins
        self.numouts = numouts
        self.inlayer = []
        self.outlayer = []
        self.hidden = []
        self.connection_list = []

        for n in range(self.numins):
            self.inlayer.append(nr.neuron(nr.neurotype.inp))

        for n in range(self.numouts):
            self.outlayer.append(nr.neuron(nr.neurotype.output))

        # define connections for feedforward with no hidden layers
        for o in self.outlayer:
            for i in self.inlayer:
                self.connection_list.append(o.addParent(i))

    def activate(self, inputs):
        for inp in range(len(inputs)):
            self.inlayer[inp].input = inputs[inp]

        out = []
        for o in self.outlayer:
            out.append(o.activate())
        return out


ins = 2*np.random.rand(10) - 1
nn = feedForward(10,10)
print(nn.activate(ins))