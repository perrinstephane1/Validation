from abc import abstractmethod


class TransitionRelation:
    def __init__(self):
        pass
    @abstractmethod
    def roots(self):
        pass

    @abstractmethod
    def next(self, source):
        pass