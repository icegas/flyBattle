import abc
from MathModel import MathModel
import numpy as np

class Component(MathModel):

    _X = np.array([]) 

    def getPosition(self):
        return self._X
    
    def model(self, y, t):
        pass

'''    @abc.abstractmethod
    def getPosition(self):
        pass

    @abc.abstractmethod
    def setPosition(self):
        pass
'''
class Vehicle(Component):

    def __init__(self, mediator):
        self._mediator = mediator

    
    def model(self, y, t):
        pass

class FlyingVehicle(Vehicle):

    def __init__(self, thrustCoff, dm, massAV, X, mediator):
        Vehicle.__init__(self, mediator)    
        self._X = X
        self._thrust = thrustCoff
        self._dm = dm
        self._massAV = massAV
    
    
    def getMass(self):
        return self._massAV

    def model(self, y, t):
        pass