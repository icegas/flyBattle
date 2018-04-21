import abc
from math import sqrt, atan2
import numpy as np
from component import Component

class NavigationFacility(Component):
    __metaclass__ = abc.ABCMeta

    #always coordinates or accelerations or velocity
    def __init__(self, X, mediator):
        super().__init__(mediator, X)

    #count position in what you need
    @abc.abstractmethod
    def get_position(self):
        pass

    def model(self, y , t):
        pass

class BINS(NavigationFacility):
    
    def __init__(self, X, mediator):
       super().__init__(X, mediator) 
    
    def get_position(self):
        return self._X

class GNSS(NavigationFacility):
    
    #x, y, z, vx, vy, vz
    def __init__(self, X, mediator):
        super().__init__(mediator, X)
    
    def get_position(self):
        X = self._X
        return [ X[0], X[1], X[2], \
                 sqrt(X[3]**2 + X[5]**2),\
                 atan2(X[5] / X[3]) ] 


class PinpointSystem(Component):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        pass

    def model(self, y, t):
        pass
    
    @abc.abstractmethod
    def peleng(self):
        pass

class RLS(PinpointSystem):

    def __init__(self, P1, D, S):
        self.P1 = P1 #power of transmitter
        self.D = D #gain coff
        self.S = S #area of transmitter
    
    def peleng(self, R):
        return self.P1 * self.D * self.S / ( (4 * np.pi)**2 * R**4)
    

