import numpy as np
import abc

class MathModel(object):

    __metaclass__ = abc.ABCMeta
    def __init__(self, t0, t1, steps, y0):
        self._t = np.linspace(t0, t1, steps)
        self._y = y0
    
    result = []

    @property    
    def T(self):
        return self._t

    @property
    def Y(self):
        return self._y

    @abc.abstractmethod
    def model(self, y, t):
        pass
    
