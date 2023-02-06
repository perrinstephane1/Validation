import copy
from seance_4.AConfig import AConfig


class AliceBob2(AConfig):

    def __init__(self):
        # alice = 1
        # bob = 2
        self.conf = [[1], [], [], [], [2]]  # chez Alice, waitAlice, jardin, waitBob, chez Bob
        self.flagAlice = False
        self.flagBob = False

    def config(self):
        return self.conf

    def copy(self):
        return copy.deepcopy(self)

    def AB2_on_entry(self, n):
        return len(n.conf[1]) >= 1 and len(n.conf[3]) >= 1

    # modif de on_entry pour avoir 3 paramètres
    def AB2_on_entry2(self, source, n, o):
        print(n)
        return len(list(o[0].enabledActions(n))) == 0  # retourne quand il n'y a plus d'actions possible

    def __hash__(self):
        return 1

    def __eq__(self, other):
        return self.conf == other.conf

    def __repr__(self):
        return str(self.conf)

    def guardeAB2(self, i, j):
        def res(config):
            if i == j:
                return False
            if config.conf[i] == []:  # section vide
                return False
            elif i == 0:  # cas chez alice
                if j != 1:
                    return False
                else:
                    #self.flagAlice = True
                    return True
            elif i == 4:  # cas chez bob
                if j != 3:
                    return False
                else:
                    #self.flagBob = True
                    return True
            elif i == 1:  # cas waitAlice
                if j != 2 or config.flagBob != False:
                    return False
                else:
                    return True
            elif i == 3:  # cas waitBob
                if j != 2 or config.flagAlice != False:
                    return False
                else:
                    return True
            elif i == 2:  # cas jardin
                if config.conf[i][0] == 2 and j == 4:  # cas Bob rentre chez Bob
                    #self.flagBob = False
                    return True
                elif config.conf[i][0] == 1 and j == 0:  # cas Alice rentre chez Alice
                    #self.flagAlice = False
                    return True
                else:
                    return False
            else:
                return True

        return res


    def changeAB2(self, i, j):
        def res(config):
            if i == 0 and j == 1:
                config.flagAlice = True
            if i == 4 and j == 3:
                config.flagBob = True
            #if i == 2 and j == 0:
             #   config.flagAlice = False
            #if i == 2 and j == 4:
             #   config.flagBob = False
            indice = config.conf[i].pop(0)
            config.conf[j].append(indice)
            return config

        return res
