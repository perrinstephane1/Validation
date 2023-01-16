import copy

from seance_4.SemanticTransitionRelation import SemanticTransitionRelation


class SoupSemantics(SemanticTransitionRelation):
    def __init__(self, program):
        self.program = program

    def initialConfigurations(self):
        return [self.program.ini]

    def enabledActions(self, source):
        return filter(lambda r: r.guard(source), self.program.rules)

    def execute(selfself, action, source):
        t=source.copy()
        return action.execute(t)
