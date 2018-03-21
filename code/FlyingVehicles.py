from component import FlyingVehicle, Component
from facility import  BINS
import numpy as np
from math import exp

class Rocket(FlyingVehicle):

    def __init__(self, X, mediator):
        FlyingVehicle.__init__(self, mediator)
        self.bins = BINS(X)
        self.X = X
 
    
    def model(self, y, t):
        
        a=0.012277471; b=1.0-a;    
        D1=((y[0]+a)**2+y[1]**2)**(3.0/2)
        D2=((y[0]-b)**2+y[1]**2)**(3.0/2)
        res = [y[2],\
               y[3],\
               y[0]+2.0*y[3]-b*(y[0]+a)/D1-a*(y[0]-b)/D2, \
               y[1]-2.0*y[2]-b*y[1]/D1-a*y[1]/D2
               ]
    
        return res

class Aircraft(FlyingVehicle):

    def __init__(self, mediator, X):
        FlyingVehicle.__init__(self, mediator)
        self.bins = None
        self.gnss = None
        self.rockets = []
        self.X = X

    def setBINS(self, bins):
        self.bins = bins
    
    def setGNSS(self, gnss):
        self.gnss = gnss
    
    def attachRocket(self, rocket):
        self.rockets.append(rocket)
    
    def attack(self):
        self.rockets.pop()

    def model(self, y, t):
        res = [1 / (1 + exp(1 - y[0] * t)), 1 / (1 + exp(1 - y[1] * t )) ]
        return res
