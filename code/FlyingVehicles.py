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
        self.bins = BINS(X[: -1])
        
    def add(self):
        pass

    def model(self, y, t):
        
        mass = self._massAV + y[6]
        F = np.array([self._thrust * self._dm, 0, 0])
        q1 = Quaternion(axis = [0, 0, 1], angle = np.arctan2(self._mediator.X[8] - y[1], self._mediator.X[7] - y[0]))
        q2 = Quaternion(axis=[0, 1, 0], angle = np.arctan2( -(self._mediator.X[9] - y[2]), sqrt( (self._mediator.X[7] - y[0])**2 + (self._mediator.X[8] - y[1])**2 ) ) ) 
        q3 = q1 * q2
        acc = q3.rotate(F) / mass

        for i in range(3):
            if np.absolute(y[i + 3]) > self.__Max_Vel:
                y[i + 3] = self.__Max_Vel if y[i + 3] > 0 else -self.__Max_Vel

        FlyingVehicle.model(self, y, t)

        res =[ y[3] , y[4] , y[5], \
              acc[0], acc[1], acc[2], -self._dm] 

        return res

class Aircraft(FlyingVehicle):

    __Max_Vel = 700

    def __init__(self, thrustCoff, dm, massAV, X, mediator):
        FlyingVehicle.__init__(self, thrustCoff, dm, massAV, X, mediator)
        self.bins = BINS(X[: -1])
        self.gnss = GNSS(X[: -1]) 
        self._mediator.subseq = np.append(self._mediator.subseq, len(X))
        self._mediator.X = np.append(self._mediator.X, X)

    def setBINS(self, bins):
        self.bins = bins
    
    def setGNSS(self, gnss):
        self.gnss = gnss
    
    def add(self, component):
        if not type(component) is Rocket:
            print("Erorr: Only rocket can be added to aircraft")
        else:
            super(Aircraft, self).add(component)
            self._massAV += component.getMass()
            
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
        
        for i in range(3):
            if np.absolute(y[i + 3]) > self.__Max_Vel:
                y[i + 3] = self.__Max_Vel if y[i + 3] > 0 else -self.__Max_Vel

        FlyingVehicle.model(self, y, t)

        res = [ y[3] , y[4] , y[5], \
              acc[0], acc[1], acc[2], -self._dm] 

        return res
