class SoupProgram:
    def __init__(self, ini):
        self.init = ini
        self.rules = []

    def add(self, rule):
        self.rules.append(rule)