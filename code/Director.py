from FlyingVehicles import Aircraft, Rocket
import numpy as np

class Director:

    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder
        
    def getAircraft(self, X, mediator, rocket_coor = [], num_of_rockets = 0):
        aircraft = Aircraft(mediator, X)

        bins = self.__builder.getBINS(X)
        aircraft.setBINS(bins)

        gnss = self.__builder.getGNSS(X)
        aircraft.setGNSS(gnss)

        if rocket_coor:
            roc_coor =np.reshape(rocket_coor, (num_of_rockets, -1))
        for i in range(num_of_rockets):
            rocket = self.__builder.getRocket(roc_coor[:, i], mediator)
            aircraft.attachRocket(rocket)

        return aircraft
