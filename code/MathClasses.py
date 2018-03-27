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
        A = np.matrix([ [ cos(psi) * cos(teta), -cos(gamma) * cos(psi) * sin(teta) + sin(gamma) * sin(psi), sin(gamma) * cos(psi) * sin(teta) + cos(gamma) * sin(psi) ],
                       [ sin(teta), cos(gamma) * cos(teta), -sin(gamma) * cos(teta) ],
                       [ -cos(teta) * sin(psi), cos(gamma) * sin(psi) * sin(teta) + sin(gamma) * cos(psi), -sin(gamma) * sin(psi) * sin(teta) + cos(gamma) * cos(psi) ]  ] )        
        
        return A.dot(vector)