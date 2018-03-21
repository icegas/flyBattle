from component import Component
from MathModel import MathModel
from Isoda import Isoda
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

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

        self._mediator.subseq = np.append(self._mediator.subseq, len(component.getPosition()))
        self._mediator.X = np.append(self._mediator.X, component.getPosition())

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
        
        self._mediator.X = y
        return models

    def simulate(self):
        MathModel.__init__(self, self._t0, self._t1, self._steps, self._mediator.X)
        solver = Isoda()
        solver.evaluate(self)

        rows,cols = 2, 3 #cols - how many plots you want
        text = ['x', 'y', 'z', 'vx', 'vy', 'vz', 'dm']
        s = ['AtackAircraft', 'TargetAircraft']
        gs = gridspec.GridSpec(rows, cols) 
       

#      res = self.result[::, 0:4]
#       plt.plot(self.T, res[:, 0])
#        plt.show()

        for k in range(2):
            plt.figure()

            for i in range(rows):
                for j in range(cols):
                    plt.subplot(gs[i, j])
                    plt.plot(self.T, self.result[:, i * rows + (j + 7)] if i > 0 else self.result[:, i * rows + j ])
                   # plt.xlabel(text[j])
                   # plt.ylabel(self.T)
                   # plt.title(s[i])

        plt.show()