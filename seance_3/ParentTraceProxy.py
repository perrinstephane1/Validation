from seance_3.IdentityProxy import IdentityProxy

class ParentTraceProxy(IdentityProxy):
    def __init__(self, operand, dict):
        super.__init__(operand)# l'opérande c'est le graphe qu'on va explorer
        self.dict = dict

    def roots(self):
        neighbours = self.operand.roots()
        for n in neighbours:
            self.dict[n]=n
        return neighbours  # retourne le root du graphe

    def next(self, source):
        neighbours = self.operand.next(source)
        for n in neighbours:
            self.dict[n]=source
        return neighbours  # retourne le next du graphe

def getTrace(dict, target):
    res=[target]
    courant=None
    while courant!=res[-1]:
        courant=dict[courant]
    return res.reverse()