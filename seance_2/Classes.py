from abc import abstractmethod


class TransitionRelation:
    def __init__(self, dict):
        self.dict=dict

    @abstractmethod
    def roots(self, source):
        pass

    @abstractmethod
    def next(self, source):
        pass

class NBits(TransitionRelation):
    def __init__(self, dict, root):
        super.__init__(dict)
        self.root=root

    def roots(self, source):
        return self.root

    def next(self, source):
        return self.dict[source]