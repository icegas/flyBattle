from component import Component
from integrator.MathModel import MathModel

class Scene(Component, MathModel):
    
    def __init__(self, t0, t1, steps, X):
        MathModel.__init__(t0, t1, steps, X)
        self._components = []
    
    def add(self, component):
        self._components.append(component)

    def remove(self, component):
        self._components.remove(component)

    def model(self, y, t):
        y[0] = y[3] #dx = vx
        y[1] = y[4] #dy = vy
        y[2] = y[5] #dz = vz
        