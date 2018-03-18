import abc

class Component:
    
    __metaclass__ = abc.ABCMeta

'''    @abc.abstractmethod
    def getPosition(self):
        pass

    @abc.abstractmethod
    def setPosition(self):
        pass
'''
class Vehicle:

    def __init__(self, mediator):
        self._mediator = mediator

class FlyingVehicle(Vehicle):

    def __init__(self, mediator):
        super().__init__(mediator)    