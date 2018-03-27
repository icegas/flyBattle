import numpy as np

class Mediator:
    def add(self, vehicle):
        pass
    
    def getModelsPos(self):
        pass

class Keeper(Mediator):

    def __init__(self):
        self._colleagues = []
        self.X = np.array([])
        self.subseq = np.array([], dtype=int)

    def add(self, colleague):
        self._colleagues.append(colleague)
    
#    def getModelsPos(self):
#        self.models_pos = []
#        for colleague in self._colleagues:
#            self.models_pos.append(colleague.X)
#        self.models_pos = np.array(self.models_pos)
    
    def UpdateModelPos(self):
        counter = 0
        for colleague in self._colleagues:
            colleague.X = self.X[counter]
            counter += 1