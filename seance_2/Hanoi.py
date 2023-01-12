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
        res=[]
        n=source.taille()
        #print(source.conf)
        #print("--------")
        for i in range(n):
            if source.conf[i]!=[]:
                for j in range(n):
                    if i!=j:
                        if source.conf[j]==[]:
                            #print("liste vide")
                            res.append(copy.deepcopy(source))
                            config=res[-1]
                            indice=config.conf[i].pop(0)
                            config.conf[j].append(indice)
                            #print(config.conf)
                        elif source.conf[i][0]<source.conf[j][0]:
                            #print("on rajoute")
                            res.append(copy.deepcopy(source))
                            config = res[-1]
                            config.conf[j].reverse()
                            config.conf[j].append(config.conf[i].pop(0))
                            config.conf[j].reverse()
                            #print(config.conf)
        return res


def hanoi_on_entry(source, n, acc):
    conf=n.conf
    i=0
    while i<n.taille()-1:
        if conf[i]!=[]:
            return False
        i=i+1
    double=copy.deepcopy(conf[-1])
    if double.sort()==conf[-1]:
        return False
    print("GAGNE")
    return True