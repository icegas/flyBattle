from component import Component
from MathModel import MathModel
from Isoda import Isoda
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

class Scene(Component):

    def __init__(self, dt, mediator, R):
        super().__init__(mediator)
        self._mediator = mediator
        self._R = R
        self.res = np.array([])
        self._t0 = 0.0
        self._dt = dt
        self._solver = Isoda()

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

    def _checkOnHit(self, rX, tX):
        if( (rX[0] - tX[0]) ** 2 + (rX[1] - tX[1]) ** 2 + (rX[2] - tX[2]) ** 2 < self._R ** 2 ):
            return True
        else:
            return False

    def simulate(self):

        if not len(self.res):
            self.res = np.array(self._mediator.X)

        MathModel.__init__(self, self._t0, self._t0 + self._dt, 2, self._mediator.X)
        self._solver.evaluate(self)
        self._t0 = self._t0 + self._dt
        self.res = np.vstack((self.res, self.result[1]))

        return self._checkOnHit(self._mediator.X[14 : 17], self._mediator.X[7 : 10])

