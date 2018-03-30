import xml.etree.ElementTree as ET

class Config:

    @staticmethod
    def load():
        root = ET.parse("/root/Desktop/studying/flyBattle/code/data.xml").getroot()
        Config.RocketConfig.load(root)
        Config.AtackAircraftConfig.load(root)
        Config.TargetAircraftConfig.load(root)
        Config.SceneConfig.load(root) 

    class RocketConfig:

        @staticmethod 
        def load(root):
            name = root.find('Rocket')
            Config.RocketConfig.thrustCoff = float(name.find('thrustCoff').text)
            Config.RocketConfig.FuelMassPerSecond = float(name.find('FuelMassPerSecond').text)
            Config.RocketConfig.MassWithoutFuel = float(name.find('MassWithoutFuel').text)
            Config.RocketConfig.x = float(name.find('x').text)
            Config.RocketConfig.y = float(name.find('y').text)
            Config.RocketConfig.z = float(name.find('z').text)
            Config.RocketConfig.vx = float(name.find('vx').text)
            Config.RocketConfig.vy = float(name.find('vy').text)
            Config.RocketConfig.vz = float(name.find('vz').text)
            Config.RocketConfig.FuelMass = float(name.find('FuelMass').text)

    class AtackAircraftConfig:

        @staticmethod 
        def load(root):
            name = root.find('AtackAircraft')
            Config.AtackAircraftConfig.thrustCoff = float(name.find('thrustCoff').text)
            Config.AtackAircraftConfig.FuelMassPerSecond = float(name.find('FuelMassPerSecond').text)
            Config.AtackAircraftConfig.MassWithoutFuel = float(name.find('MassWithoutFuel').text)
            Config.AtackAircraftConfig.x = float(name.find('x').text)
            Config.AtackAircraftConfig.y = float(name.find('y').text)
            Config.AtackAircraftConfig.z = float(name.find('z').text)
            Config.AtackAircraftConfig.vx = float(name.find('vx').text)
            Config.AtackAircraftConfig.vy = float(name.find('vy').text)
            Config.AtackAircraftConfig.vz = float(name.find('vz').text)
            Config.AtackAircraftConfig.FuelMass = float(name.find('FuelMass').text)
            Config.AtackAircraftConfig.rockets = int(name.find('rockets').text)

    class TargetAircraftConfig:

        @staticmethod 
        def load(root):
            name = root.find('TargetAircraft')
            Config.TargetAircraftConfig.thrustCoff = float(name.find('thrustCoff').text)
            Config.TargetAircraftConfig.FuelMassPerSecond = float(name.find('FuelMassPerSecond').text)
            Config.TargetAircraftConfig.MassWithoutFuel = float(name.find('MassWithoutFuel').text)
            Config.TargetAircraftConfig.x = float(name.find('x').text)
            Config.TargetAircraftConfig.y = float(name.find('y').text)
            Config.TargetAircraftConfig.z = float(name.find('z').text)
            Config.TargetAircraftConfig.vx = float(name.find('vx').text)
            Config.TargetAircraftConfig.vy = float(name.find('vy').text)
            Config.TargetAircraftConfig.vz = float(name.find('vz').text)
            Config.TargetAircraftConfig.FuelMass = float(name.find('FuelMass').text)

    class SceneConfig:

        @staticmethod
        def load(root):
            name = root.find('Scene')
            Config.SceneConfig.DeltaTime = float(name.find('DeltaTime').text)
            Config.SceneConfig.BlastRadius = float(name.find('BlastRadius').text)

#root = ET.parse("/root/Desktop/studying/flyBattle/code/data.xml").getroot()
#rocket = root.find('Rocket')
#d = rocket.find('x')
#d = d.text
