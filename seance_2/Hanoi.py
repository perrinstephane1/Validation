import copy

from seance_2.Classes import TransitionRelation


class HanoiConfiguration(TransitionRelation):
    # état du jeu
    def __init__(self, taille, nbre_disque):
        self.conf=[[k for k in range(nbre_disque)]]
        for k in range(nbre_disque-1):
            self.conf.append([])
        self.size=taille
    def config(self):
        return self.conf
    def taille(self):
        return self.size

    def __hash__(self):
        return 1

    def __eq__(self, other):
        if len(self.conf)!=other.conf:
            return False
        for i in range(len(self.conf)):
            if len(self.conf[i]) != other.conf[i]:
                return False
            for k in range(len(self.conf[i])):
                if self.conf[i][k]!=other.conf[i][k]:
                    return False
        return True

class HanoiGraph(TransitionRelation):
    def __init__(self, config):
        self.root=config #HanoiConfiguration

    def roots(self):
        print("COUCOU")
        print(self.root)
        return [self.root]
    def vieuxNext(self, source):
        res=[]
        for i in range(source.taille()):
            print("coucou")
            if source.conf[i]!=[]: # si on peut prendre un disque
                print(source.conf[i])
                indice=source.conf[i][1]
                print("on rentre dans la tour")
                for j in range(source.taille()):
                    if j!=i:
                        if (source.conf[j]==[]) or (source.conf[i][0]<indice):

                            res.append(copy.deepcopy(source))
                            disque=res[-1][i].pop()
                            res[-1].conf[j]=[indice]+res[-1].conf[j]
                            print("on ajoute")
        print("ON A FINI LA RECHERCHE : on ajoute ça :")
        print(res)
        return res

    def next(self, source):
        """
        :param source: de type HanoiConfiguation
        :return: liste de HanoiConfiguration
        """
        res = []
        n = source.taille()
        for i in range(n):
            if source.conf[i] != []:
                for j in range(n):
                    if i != j:
                        if source.conf[j] == []:
                            res.append(copy.deepcopy(source))
                            config = res[-1]
                            indice = config.conf[i].pop(0)
                            config.conf[j].append(indice)
                        elif source.conf[i][0] < source.conf[j][0]:
                            res.append(copy.deepcopy(source))
                            config = res[-1]
                            config.conf[j].reverse()
                            config.conf[j].append(config.conf[i][0])
                            config.conf[j].reverse()
        return res


def hanoi_on_entry(source, n, acc):
    conf=n.conf
    ## doit vérifier si on a fini ou pas le Hanoi
    i=0
    while i<n.taille():
        if conf[i]!=[]:
            return False
    double=copy.deepcopy(conf[-1])
    if double.sort()==conf[-1]:
        return False
    return True