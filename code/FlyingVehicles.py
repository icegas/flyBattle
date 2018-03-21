from component import FlyingVehicle, Component
from facility import  BINS, GNSS
import numpy as np
from math import atan2, sqrt
from MathClasses import TransitMatrix 

class Rocket(FlyingVehicle):

    #x, y, z, vx, vy, vz, m ''''' Mass of AV = MASS of fuel + MASS of AV without fuel
    def __init__(self, thrustCoff, dm, massAV, X, mediator, fuel_mass):
        FlyingVehicle.__init__(self, thrustCoff, dm, massAV, X, mediator)
        self._X = np.append(self._X, fuel_mass)
        self.bins = BINS(X[: -1])
    
    def model(self, y, t):
        
        mass = self._massAV + y[6]
        F = self._thrust * self._dm

        body_vec = TransitMatrix.globalToBody(y[3 : 6], atan2(self._mediator.X[9] - y[2], self._mediator.X[7] - y[0]), 
        atan2( sqrt( (self._mediator.X[7] - y[0])**2 + (self._mediator.X[9] - y[2])**2 ), self._mediator.X[8] - y[1]), 0)
        acc = body_vec * F / mass

        res =[ y[3] , y[4] , y[5], \
              acc[0], acc[1], acc[2], -self._dm] 

        return res

class Aircraft(FlyingVehicle):

    def __init__(self, thrustCoff, dm, massAV, X, mediator,  rThrustCoff = None, rDm = None, rMass = None, rocket_fuel = None, num_of_rockets = 0):
        FlyingVehicle.__init__(self, thrustCoff, dm, massAV, X, mediator)
        self.bins = BINS(X)
        self.gnss = GNSS(X) 
        self._rockets = []
        for i in range(num_of_rockets): 
            self.attachRocket(Rocket(rThrustCoff, rDm, rMass, X[:-1], self._mediator, rocket_fuel))

    def setBINS(self, bins):
        self.bins = bins
    
    def setGNSS(self, gnss):
        self.gnss = gnss
    
    def attachRocket(self, rocket):
        self._rockets.append(rocket)
        self._massAV += rocket.getMass() 
        
    def dettachRocket(self):
        rocket = self._rockets.pop()
        self._massAV -= rocket.getMass() 
        return rocket

    def model(self, y, t):
        mass = self._massAV + y[6]
        F = self._thrust * self._dm
        body_vec = TransitMatrix.globalToBody(y[3 : 6], 0, 0, 0)
        acc = body_vec * F / mass
        
        res = [ y[3] , y[4] , y[5], \
              acc[0], acc[1], acc[2], -self._dm] 

        return res
