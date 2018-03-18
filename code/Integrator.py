import abc

class Integrator(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def evaluate(self, math_model):
        pass