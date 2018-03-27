import abc
from MathModel import MathModel
import numpy as np

class Component(MathModel):

    def __init__(self, mediator, X = None):
        self._mediator = mediator
        self._components = []
        self._X = X

    def getPosition(self):
        return self._X
    
    def model(self, y, t):
        pass

    def add(self, component):
        self._components.append(component)
        self._mediator.add(component) 

    def remove(self, component):
        if(len(self._components)):
            self._components.remove(component)
        else:
            print("nothing to remove")

class Vehicle(Component):

    def __init__(self, mediator, X):
        super().__init__( mediator, X)

    
    def model(self, y, t):
        pass

class FlyingVehicle(Vehicle):

    def __init__(self, thrustCoff, dm, massAV, X, mediator):
        Vehicle.__init__(self, mediator, X)    
        self._thrust = thrustCoff
        self._dm = dm
        self._massAV = massAV

    def getMass(self):
        return self._massAV

    def model(self, y, t):

        if (y[6] < 0):
            y[6] = 0
            self._dm = 0