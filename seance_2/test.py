import copy


def monNext(source):
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