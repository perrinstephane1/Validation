class SoupSemantics(SemanticTransitionRelation):
    def __init__(self, program):
        self.program = program

    def initialConfigurations(self):
        return [self.program.ini]

    def enabledActions(self, source):
        return filter(lambda r: r.guard(source), program.rules)

    def execute(selfself, action, source):
        t = copy.deepcopy(source)
        return action.execute(t)