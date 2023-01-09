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