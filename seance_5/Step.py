class Step(AbstractStep):

    def __init__(self, source, action, target):
        self.source = source
        self.action = action
        self.target = target