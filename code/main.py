import numpy as np
from scene import Scene
from mediator import Keeper
from FlyingVehicles import Aircraft, Rocket
from config import Config

def main():
    Config.load()
    keepper = Keeper()
    scene = Scene(Config.SceneConfig.DeltaTime, keepper, Config.SceneConfig.BlastRadius)

    #Primary conditions for rocket
    rX =  np.array([Config.RocketConfig.x, Config.RocketConfig.y, Config.RocketConfig.z, 
    Config.RocketConfig.vx, Config.RocketConfig.vy, Config.RocketConfig.vz, Config.RocketConfig.FuelMass])

    #Primary conditions for  attack Aircraft
    aX =  np.array([Config.AtackAircraftConfig.x, Config.AtackAircraftConfig.y, Config.AtackAircraftConfig.z, 
    Config.AtackAircraftConfig.vx, Config.AtackAircraftConfig.vy, Config.AtackAircraftConfig.vz, Config.AtackAircraftConfig.FuelMass])

    #Primary conditions for target Aircraft    
    tX =  np.array([Config.TargetAircraftConfig.x, Config.TargetAircraftConfig.y, Config.TargetAircraftConfig.z, 
    Config.TargetAircraftConfig.vx, Config.TargetAircraftConfig.vy, Config.TargetAircraftConfig.vz, Config.TargetAircraftConfig.FuelMass])

    #thrustcoff, FuelMassPerSecond, MassWithoutFuel, Vector, mediator 
    atackAircraft = Aircraft(Config.AtackAircraftConfig.thrustCoff, Config.AtackAircraftConfig.FuelMassPerSecond,
    Config.AtackAircraftConfig.MassWithoutFuel, aX, keepper)    

    #:46,47s/AtackAircraft/TargetAircraft/g
    targetAircraft = Aircraft(Config.TargetAircraftConfig.thrustCoff, Config.TargetAircraftConfig.FuelMassPerSecond,
    Config.TargetAircraftConfig.MassWithoutFuel, tX, keepper)
    
    for i in range(Config.AtackAircraftConfig.rockets):
        atackAircraft.add( Rocket(Config.RocketConfig.thrustCoff, Config.RocketConfig.FuelMassPerSecond,
    Config.RocketConfig.MassWithoutFuel, rX, keepper) )
    
    scene.add(atackAircraft) 
    scene.add(targetAircraft)
    scene.add(atackAircraft.dettachRocket())
        
    while not scene.simulate():
        pass

    print("The Target is striked\n")
    print("Last Vector:")
    print("---------------------------------------------------------------------")
    print(scene.res[-1])
    print("---------------------------------------------------------------------")
    print("Target Coordinates:")
    print("---------------------------------------------------------------------")
    print(keepper.X[7:10])  
    print("---------------------------------------------------------------------")
    print("Rocket Coordinates:")
    print("---------------------------------------------------------------------")
    print(keepper.X[14:17])
    print("---------------------------------------------------------------------")
    print("time: {}\n".format(scene.T[-1]))

if __name__ == '__main__':
    main()