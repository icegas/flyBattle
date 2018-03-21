import numpy as np
from scene import Scene
from Director import Director
from mediator import Keeper
from Builder import AircraftBuilder

class A:

    def __init__(self, x, y):
        self._X = np.array([])
        self.x = x    
'''    @property
    def X(self):
        return self._X
    
    @X.setter
    def X(self, value):
        self._X = value
    
    def __getitem__(self, key):
        return self._X[key]
    
    def __setitem__(self, key, value):
        self._X[key] = value
'''
  
from FlyingVehicles import Rocket
#from Arenstorf import Arenstorf
#from Isoda import Isoda
def main():
    keepper = Keeper()
    scene = Scene(0, 18, 1000, keepper)

    director = Director()
    aircraft_builder = AircraftBuilder()
    director.setBuilder(aircraft_builder) 

    #scene added must be in consequence how objects is created
    aircraft = director.getAircraft([3, 4], keepper)
    model2 = Rocket([0.994, 0.0, 0.0, -2.00151], keepper)

    scene.add(model2)
    scene.add(aircraft)
    scene.simulate() 
    
if __name__ == '__main__':
    main()