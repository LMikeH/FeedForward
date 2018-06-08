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
        neuron1 = random.choice()
        neuron2 = ramdom.choice()
        newcon = nr.connection(neuron1, neuron2)
        neuron1.child_connections.append(newcon)
        neuron2.parent_connections.append(newcon)
        self.connection_list.append(newcon)

ins = 2*np.random.rand(10) - 1
nn = feedForward(10,10)
print(ins)
print(nn.activate(ins))

print(len(nn.hidden))
print(len(nn.connection_list))
nn.addNeuron()
print(len(nn.hidden))
print(len(nn.connection_list))

neuron1 = nn.inlayer[0]
neuron2 = nn.hidden[0]
nn.addConnection()
print(len(nn.connection_list))
neuron3 = nn.hidden[0]
neuron4 = nn.outlayer[3]
nn.addConnection()
print(len(nn.connection_list))
print(nn.activate(ins))

nn.addNeuron()
