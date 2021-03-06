from component import FlyingVehicle, Component
from facility import  BINS, GNSS
import numpy as np
from math import atan2, sqrt, degrees,radians
from pyquaternion import Quaternion

class Rocket(FlyingVehicle):
    __Max_Vel = 3000
    #x, y, z, vx, vy, vz, m ''''' Mass of AV = MASS of fuel + MASS of AV without fuel
    def __init__(self, thrustCoff, dm, massAV, X, mediator):
        FlyingVehicle.__init__(self, thrustCoff, dm, massAV, X, mediator)
        self.add(BINS(X[: -1], self._mediator))
        
    #def add(self):
     #   pass

    def model(self, y, t):
        
        mass = self._massAV + y[6]
        F = np.array([self._thrust * self._dm, 0, 0])
        q1 = Quaternion(axis = [0, 0, 1], angle = np.arctan2(self._mediator.X[8] - y[1], self._mediator.X[7] - y[0]))
        q2 = Quaternion(axis=q1.rotate([0, 1, 0]), angle = np.arctan2( (self._mediator.X[9] - y[2]), sqrt( (self._mediator.X[7] - y[0])**2 + (self._mediator.X[8] - y[1])**2 ) ) ) 
        q3 = q2.conjugate * q1

        acc = q3.rotate(F) / mass

        FlyingVehicle.model(self, y, t)

        res =[ y[3] , y[4] , y[5], \
              acc[0], acc[1], acc[2], -self._dm] 

        return res

class Aircraft(FlyingVehicle):

    __Max_Vel = 700

    def __init__(self, thrustCoff, dm, massAV, X, mediator):
        FlyingVehicle.__init__(self, thrustCoff, dm, massAV, X, mediator)
        self.add(BINS(X[: -1], self._mediator))
        self.add(GNSS(X[: -1], self._mediator)) 
        self._mediator.subseq = np.append(self._mediator.subseq, len(X))
        self._mediator.X = np.append(self._mediator.X, X)

    def add(self, component):
        if type(component) is Rocket:
            super(Aircraft, self).add(component)
            self._massAV += component.getMass()
        else:
            super().add(component)
            
    def dettachRocket(self):
        rocket = self._components.pop()
        self._mediator.subseq = np.append(self._mediator.subseq, len(rocket.getPosition()))
        self._mediator.X = np.append(self._mediator.X, rocket.getPosition())
        self._massAV -= self.getMass()

        if(len(self._components)):
            return rocket 
        else:
            print("Nothing to remove")

    def model(self, y, t):
        mass = self._massAV + y[6]
        F = np.array([self._thrust * self._dm, 0, 0])
        acc = F / mass
        
        FlyingVehicle.model(self, y, t)

        res = [ y[3] , y[4] , y[5], \
              acc[0], acc[1], acc[2], -self._dm] 

        return res
