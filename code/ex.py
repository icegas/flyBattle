from Isoda import Isoda
from Arenstorf import Arenstorf
import numpy as np

class A:

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

def main():
    a = A()
    a = np.array([0, 1, 2])
    a[0] = 10
    print(a)
    
    
    
    
    
if __name__ == '__main__':
    main()