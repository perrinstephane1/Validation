from seance_4.AConfig import AConfig


class Conf2(AConfig):
    def __init__(self):
        self.PC=1
    def __str__(self):
        return str(self.PC)

class Conf3(AConfig):
    def __init__(self):
        self.PC='a'
    def __str__(self):
        return str(self.PC)