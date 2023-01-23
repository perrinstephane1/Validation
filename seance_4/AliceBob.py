import copy
from seance_4.AConfig import AConfig


class AliceBob(AConfig):

    def __init__(self):
        # alice = 1
        # bob = 2
        self.conf = [[1], [], [2]] # chez Alice, jardin, chez Bob

    def config(self):
        return self.conf

    def copy(self):
        return copy.deepcopy(self)

    def AB_on_entry(self, n):
        return len(n.conf[1])>=2

    def __hash__(self):
        return 1

    def __eq__(self, other):
        return self.conf==other.conf

    def __repr__(self):
        return str(self.conf)


def guardeAB(i, j):
    def res(config):
        if i == j :
            return False
        if config.conf[i] == []: # section vide
            return False
        elif i==0 or i==2:
            if j!=1:
                return False
            else :
                return True
        elif i == 1:
            if config.conf[i][0] == 2 and j != 2:
                return False
            if config.conf[i][0] == 1 and j != 0:
                return False
        else :
            return True
    return res


def changeAB(i, j):
    def res(config):
        indice = config.conf[i].pop(0)
        config.conf[j].append(indice)
        return config

    return res

