from component import FlyingVehicle, Component
from facility import  BINS
from MathClasses import ProtList

class Rocket(FlyingVehicle, Component):

    def __init__(self, X):
        self.bins = BINS(X)
        self.X = ProtList()
        self.X = X

    
class Aircraft(FlyingVehicle, Component):

    def __init__(self, mediator):
        super().__init__(mediator)
        self.bins = None
        self.gnss = None
        self.rockets = list()
        self.X = ProtList()

    def setBINS(self, bins):
        self.bins = bins
    
    def setGNSS(self, gnss):
        self.gnss = gnss
    
    def attachRocket(self, rocket):
        self.rockets.append(rocket)
    
    def Attack(self):
        self.rockets.pop()
    
    
        