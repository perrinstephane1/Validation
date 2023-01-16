class Rule:
    def __init__(self, name, guard, effect):
        self.name = name
        self.guard = guard
        self.action = effect

    def execute(self, config):
        return [self.action(config)]

    def __str__(self):
        return self.name