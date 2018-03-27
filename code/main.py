import numpy as np
from scene import Scene
from mediator import Keeper
from FlyingVehicles import Aircraft, Rocket

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
    rocket_thrust = 1e+8
    keepper = Keeper()
    scene = Scene(0.001, keepper, 10)

    #Primary conditions for target Aircraft
    tX = [4100.0, 4100.0, 4100.0, 0.0, 0.0, 0.0, 1000.0]

    #Primary conditions for  attack Aircraft
    aX = [4000.0, 4000.0, 4000.0, 0.0, 0.0, 0.0, 1000.0]
    rX = [4000.0, 4000.0, 4000.0, 0.0, 0.0, 0.0, 3000.0] 
    #thrustcoff, dm, mass, ax, keeper, rockeThrust, rocket_dm, rocket_mass, rocket_fuel_mass
    atackAircraft = Aircraft(300.0, 0.05, 5000.0, aX, keepper)    
    targetAircraft = Aircraft(300.0, 0.05, 7000.0, tX, keepper)
    
    atackAircraft.add(Rocket(rocket_thrust, 0.05, 1000.0, rX, keepper))
    atackAircraft.add(Rocket(rocket_thrust, 0.05, 1000.0, rX, keepper))
    
    scene.add(atackAircraft) 
    scene.add(targetAircraft)
    scene.add(atackAircraft.dettachRocket())
        
    while not scene.simulate():
        pass
      #  print(scene.result)
        #print(keepper.X[7:10])
       # print(keepper.X[10:13])
        #print(keepper.X[14:17])
       # print(keepper.X[17:20])
    print("The Target is striked\n")
    print("Last Vector:")
    print("---------------------------------------------------------------")
    print(scene.res[-1])
    print("---------------------------------------------------------------")
    print("time: {}\n".format(scene.T[-1]))

if __name__ == '__main__':
    main()