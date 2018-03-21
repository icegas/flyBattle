from FlyingVehicles import Aircraft, Rocket
import numpy as np

class Director:

    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder
        
    def getAircraft(self, X, mediator, aThrustCoff, aDm, aMass, rThrustCoff = None, rDm = None, rMass = None, rocket_fuel = None, num_of_rockets = 0, ):
        aircraft = Aircraft(aThrustCoff, aDm, aMass,  X, mediator)

        bins = self.__builder.getBINS(X[: -1])
        aircraft.setBINS(bins)

        gnss = self.__builder.getGNSS(X[: -1])
        aircraft.setGNSS(gnss)

        tmp = X
        #if rocket_coor:
         #   roc_coor =np.reshape(rocket_coor, (num_of_rockets, -1))
        for i in range(num_of_rockets):
            rocket = self.__builder.getRocket(tmp, mediator, rThrustCoff, rDm, rMass, rocket_fuel)
            aircraft.attachRocket(rocket)

        return aircraft
