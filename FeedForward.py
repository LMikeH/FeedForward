import numpy as np
import neuron as nr 

class feedForward():
    def __init__(self,numins,numouts):
        self.numins = numins
        self.numouts = numouts
        self.inlayer = []
        self.outlayer = []
        self.hidden = []
        self.connection_list = []

        for n in range(self.numins):
            self.inlayer.append(nr(nr.neurotype.inp))

        for n in range(self.numouts):
            self.outlayer.append(nr(nr.neurotype.output))

        # define connections for feedforward with no hidden layers
        for o in self.outlayer:
            for i in self.inlayer: