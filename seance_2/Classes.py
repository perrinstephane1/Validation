from abc import abstractmethod
from itertools import combinations
import copy

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
    def __init__(self, dict, root):
        self.dict=dict
        self.root=root

    def roots(self):
        return self.root

    def next(self, source):
        res = []
        n = len(source)
        tools = [k for k in range(n)]
        # print(tools)
        for i in range(n):
            res.append(copy.deepcopy(source))
            res[-1][i] = not (source[i])
        return res