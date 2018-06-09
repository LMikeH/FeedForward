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

    def addNeuron(self):
        # create new neuron and two new connections to replace random connection
        neuron = nr.neuron(nr.neurotype.hidden)
        con = random.choice(self.connection_list)
        con.active = False;
        conInput = nr.connection(con.parent_neuron, neuron)
        conOutput = nr.connection(neuron, con.child_neuron)
        conInput.w = 1
        conOutput.w = con.w
        # update the parent and child connections of the two old neurons and new neuron
        con.parent_neuron.child_connections.append(conInput)
        neuron.parent_connections.append(conInput)
        neuron.child_connections.append(conOutput)
        con.child_neuron.parent_connections.append(conOutput)
        # append new connections and neuron to lists
        self.connection_list.append(conInput)
        self.connection_list.append(conOutput)
        self.hidden.append(neuron)

    def addConnection(self):
        success = False
        canidateset1 = self.inlayer + self.outlayer + self.hidden
        canidateset2 = self.outlayer + self.hidden
        while success == False:
            n1 = random.choice(canidateset1)
            n2 = random.choice(canidateset2)

            connected = False
            for p in n1.parent_connections:
                if n2 == p.parent_neuron:
                    connected == True
            for c in n1.child_connections:
                if n2 == c.child_neuron:
                    connected == True

            if connected == False:
                if n1.checkAncestors(0) > n2.checkAncestors(0):
                    self.connection_list.append(n1.addParent(n2))
                    success = True
                elif n1.checkAncestors(0) < n2.checkAncestors(0):
                    self.connection_list.append(n1.addChild(n2))
                    success = True

    def changeWeight(self):
        conn = random.choice(self.connection_list)
        conn.w = random.random()
            

# ins = 2*np.random.rand(10) - 1
# nn = feedForward(10,10)
# print(nn.activate(ins))
# nn.addNeuron()
# nn.addNeuron()
# nn.addNeuron()
# nn.addNeuron()
# nn.addNeuron()
# nn.addConnection()
# nn.addConnection()
# nn.addConnection()
# nn.addConnection()
# nn.addNeuron()
# nn.addNeuron()
# nn.addNeuron()
# nn.addNeuron()
# nn.addNeuron()
# nn.addConnection()
# nn.addConnection()
# nn.addConnection()
# nn.addConnection()
# nn.addNeuron()
# nn.addNeuron()
# nn.addNeuron()
# nn.addNeuron()
# nn.addNeuron()
# nn.addConnection()
# nn.addConnection()
# nn.addConnection()
# nn.addConnection()
# print(nn.activate(ins))
# nn.changeWeight()
# nn.changeWeight()
# nn.changeWeight()
# nn.changeWeight()
# nn.changeWeight()
# nn.changeWeight()
# nn.changeWeight()
# nn.changeWeight()
# nn.changeWeight()
# nn.changeWeight()
# nn.changeWeight()
# nn.changeWeight()
# nn.changeWeight()
# nn.changeWeight()
# nn.changeWeight()
# print(nn.activate(ins))

