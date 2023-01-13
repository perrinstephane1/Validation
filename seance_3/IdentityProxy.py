class IdentityProxy():
    def __init__(self, operand):
        self.operand = operand
        pass

    def __getattr__(self, attr):
        return getattr(self.operand, attr)