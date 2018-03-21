import numpy as np
from math import cos, sin

class ProtList:
    
    def __init__(self):
        self._X = np.array([])
    
    @property
    def X(self):
        return self._X
    
    @X.setter
    def X(self, value):
        self._X = value
    
    def __getitem__(self, key):
        return self._X[key]
    
    def __setitem__(self, key, value):
        self._X[key] = value

class TransitMatrix:

    @staticmethod
    def globalToBody(vector, psi, gamma, teta):
        
        A = np.array([ [ cos(teta) * cos(psi) , sin(teta) , -cos(teta) * sin(psi) ],
                       [ -cos(gamma) * sin(teta) * cos(psi) + sin(gamma) * sin(psi) , cos(gamma) * cos(teta), cos(gamma) * sin(teta) * sin(psi) + sin(gamma) * cos(psi) ],
                       [ sin(gamma) * sin(teta) * cos(psi) + cos(gamma) * sin(psi) , -sin(gamma) * cos(teta) , -sin(psi) * sin(teta) * sin(gamma) + cos(psi) * cos(gamma) ] ])
        
        return A.dot(vector)