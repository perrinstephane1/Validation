import copy

from seance_4.AConfig import AConfig


class Config1(AConfig):
    def __init__(self, x):
        self.x=x
    def copy(self):
        return copy.deepcopy(self)