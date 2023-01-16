import copy
from seance_4.AConfig import AConfig
from seance_2.TransitionRelation import TransitionRelation


class HanoiConfiguration(AConfig):
    # état du jeu
    def __init__(self, taille, nbre_disque):
        self.conf=[[k for k in range(nbre_disque)]]
        for k in range(nbre_disque-1):
            self.conf.append([])
        self.size=taille
    def config(self):
        return self.conf
    def taille(self):
        return self.size

    def __hash__(self):
        return 1

    # def __eq__(self, other):
    #     if len(self.conf)!=other.conf:
    #         return False
    #     for i in range(len(self.conf)):
    #         if len(self.conf[i]) != other.conf[i]:
    #             return False
    #         for k in range(len(self.conf[i])):
    #             if self.conf[i][k]!=other.conf[i][k]:
    #                 return False
    #     return True

    def __eq__(self, other):
        return self.conf==other.conf

    def copy(self):
        return copy.deepcopy(self)

    def __repr__(self):
        return str(self.conf)