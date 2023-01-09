from abc import abstractmethod
from itertools import combinations
import copy

import numpy as np


class TransitionRelation:
    def __init__(self):
        pass
    @abstractmethod
    def roots(self, source):
        pass

    @abstractmethod
    def next(self, source):
        pass

class NBits(TransitionRelation):
    def __init__(self, root, n):
        self.root=root
        self.n=n

    def roots(self):
        return self.root


    def next(self, source):

        res=[]
        for i in range(self.n):
            if ((source>>i)&1)>0:
                r=source & ~(1<<i)
                #print(r)
                res.append(r)
            else:
                r=source|(1<<i)
                #print(r)
                res.append(r)
        return res

class Noeud():
    def __init__(self, list):
        self.list=list

    def __hash__(self):
        return 1

    def __eq__(self, other):
        i=0
        if len(self.list)!=len(other.list):
            return False
        while self.list[i]==other.list[i] and i<len(self.list)-1:
            i=i+1
        if i==len(self.list):
            return True
        else:
            return False

class HanoiConfiguration(TransitionRelation):
    def __init__(self, nb_piles, nb_disque):
        self.nb_piles = nb_piles
        self.nb_disque = nb_disque
        self.initial = self.roots()

    def roots(self):  # Etat initial du jeu (tableau de tableau)
        res = []
        n = self.nb_piles
        m = self.nb_disque
        for i in range(n):
            res.append([])
        for j in range(m):
            res[0].append(m-j)
        print(res)
        return res

    def next(self, source):
        liste_res = []
        res = copy.deepcopy(source)
        for i in range(self.nb_disque):
            for j in range(self.nb_disque):
                if source[i] != [] and (source[j] == [] or (source[i][-1] >= source[j][-1])):
                    res[i].append(res[j][-1])
                    res[j] = res[j][:-1]
                    liste_res.append(res)
        print(liste_res)
        return liste_res


    def on_entry(self):
        pass
