import copy

from seance_4.SemanticTransitionRelation import SemanticTransitionRelation


class SoupSemantics(SemanticTransitionRelation):
    def __init__(self, program):
        self.program = program

    def initial(self):
        return [self.program.init]

    def enabledActions(self, source):
        return list(filter(lambda r: r.guard(source), self.program.rules))

    def execute(self, action, source):
        t=source.copy()
        action.execute(t)
        return [t]
