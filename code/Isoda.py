from Integrator import Integrator
from scipy.integrate.odepack import odeint

class Isoda(Integrator):

    def evaluate(self, math_model):
        math_model.result = odeint(math_model.model, math_model.Y, math_model.T)