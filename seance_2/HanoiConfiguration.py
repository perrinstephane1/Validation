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

def guarde(i, j):
    def res(config):
        if config.conf[i] == []:
            return False
        indice = config.conf[i][0]
        if config.conf[j] == []:
            return True
        if config.conf[j][0] > indice:
            return True
        else:
            return False

    return res

def change(i, j):
    def res(config):
        indice = config.conf[i].pop(0)
        config.conf[j] = [indice] + config.conf[j]
        return config

    return res