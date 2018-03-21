from facility import GNSS, BINS
from Director import Director
import numpy as np
from FlyingVehicles import Rocket

class Builder:

    def getBINS(self): pass
    def getGNSS(self): pass
    def getRocket(self): pass
    
class AircraftBuilder(Builder):

    def getBINS(self, X):
        bins = BINS(X)
        return bins
    
    def getGNSS(self, X):
        gnss = GNSS(X)
        return gnss

    def getRocket(self, X, mediator, thrustCoff, dm, massAV, rocket_fuel):
        rocket = Rocket(thrustCoff, dm, massAV, X, mediator, rocket_fuel) 
        return rocket
        
