from seance_3.IdentityProxy import IdentityProxy

class ParentTraceProxy(IdentityProxy):
    def __init__(self, operand, dict):
        self.operand = operand
        self.dict = dict

    def roots(self):
        neighbours = self.operand.roots()
        # A completer

    def next(self, source):
        neighbours = self.operand.next(source)


def getTrace(dict, target):
    # A modifier
    return 0