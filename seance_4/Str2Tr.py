from seance_2.TransitionRelation import TransitionRelation

class Str2Tr(TransitionRelation) :
    def __init__(self, roots, next):
        self.roots = roots
        self.next = next
