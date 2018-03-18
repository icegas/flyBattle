import abc
from math import sqrt, atan2
from MathClasses import ProtList

class NavigationFacility:
    __metaclass__ = abc.ABCMeta

    #always coordinates or accelerations or velocity
    def __init__(self, X):
        self.X = ProtList()
        self.X = X
    
    #count position in what you need
    @abc.abstractmethod
    def get_position(self):
        pass

class BINS(NavigationFacility):
    
    def __init__(self, X):
       super().__init__(X) 
    
    def get_position(self):
        return self.X

class GNSS(NavigationFacility):
    
    #x, y, z, vx, vy, vz
    def __init__(self, X = []):
        super().__init__(X)
    
    def get_position(self):
        X = self.X
        return [ X[0], X[1], X[2], \
                 sqrt(X[3]**2 + X[5]**2),\
                 atan2(X[5] / X[3]) ] 

