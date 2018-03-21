from component import Component
from MathModel import MathModel
from Isoda import Isoda
import numpy as np
import matplotlib.pyplot as plt

class Scene(Component):
    
    def __init__(self, t0, t1, steps, mediator):
        self._components = []
        self._t0 = t0
        self._t1 = t1
        self._steps = steps
        self._mediator = mediator 

    
    def add(self, component):
        self._components.append(component)
        self._mediator.add(component) 

        self._mediator.subseq = np.append(self._mediator.subseq, len(component.X))
        self._mediator.X = np.append(self._mediator.X, component.X)

    def remove(self, component):
        self._components.remove(component)

    def model(self, y, t):
        counter = 0
        iterator = 0
        models = np.array([]) 
        for component, iter in zip(self._components, self._mediator.subseq):
            iterator += iter
            models = np.append(models, component.model(y[counter : iterator], t))
            counter += iter
        return models

    def simulate(self):
        MathModel.__init__(self, self._t0, self._t1, self._steps, self._mediator.X)
        solver = Isoda()
        solver.evaluate(self)

        plt.subplot(211)
        plt.plot(self.result[:, 0], self.result[:, 1])
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('My graph')
        plt.grid(True)
        plt.subplot(212) #212
        plt.plot(self.T, self.result[:, 5])
        plt.show()