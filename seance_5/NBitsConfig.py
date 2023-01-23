class NBitsConfig():
    def __init__(self, n):
        self.value = 0
    # __eq__
    # __hash__


soup = SoupProgram(NBitsConfig)
soup.add('flip 0', lambda x: True, flip0)
soup.add('flip 1', lambda x: True, flip1)

def execute(self, action, c):
    t = copy.deepcopy(c)
    o=a(t)
    return o # pas trop sûr