import numpy as np
from scene import Scene
from Director import Director
from mediator import Keeper
from FlyingVehicles import Aircraft

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
  
def main():
    keepper = Keeper()
    scene = Scene(0, 18, 1000, keepper)

    #Primary conditions for target Aircraft
    tX = [4300.0, 4100.0, 4050.0, 700.0, 650.0, 50.0, 1000.0]

    #Primary conditions for  attack Aircraft
    aX = [4000.0, 4000.0, 4000.0, 700.0, 900.0, 40.0, 1000.0]
    
    #thrustcoff, dm, mass, ax, keeper, rockeThrust, rocket_dm, rocket_mass, rocket_fuel_mass
    atackAircraft = Aircraft(300.0, 0.05, 5000.0, aX, keepper, 800.0, 0.10, 500.0, 100.0,  3)    
    targetAircraft = Aircraft(300.0, 0.05, 7000.0, tX, keepper)
    
    scene.add(atackAircraft) 
    scene.add(targetAircraft)
    scene.simulate() 
    
if __name__ == '__main__':
    main()