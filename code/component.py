import abc
from MathModel import MathModel
import numpy as np

class Component(MathModel):

    X = np.array([]) 
    
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

    def __init__(self, mediator):
        Vehicle.__init__(self, mediator)    
    
    def model(self, y, t):
        pass