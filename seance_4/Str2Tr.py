from seance_2.TransitionRelation import TransitionRelation

class Str2Tr(TransitionRelation) :
    def __init__(self, str):
        self.str = str

    def roots(self):
        return self.str.initial()

    def next(self, source):
        Actions = self.str.enabledActions(source)
        r = []
        for action in Actions:
            r.extend(self.str.execute(action, source))
        return r