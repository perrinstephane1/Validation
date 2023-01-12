import copy


def monNext(source):
    """
    :param source: de type HanoiConfiguation
    :return: liste de HanoiConfiguration
    """
    res=[]
    n=source.taille()
    for i in range(n):
        if source.conf[i]!=[]:
            for j in range(n):
                if i!=j:
                    if source.conf[j]==[]:
                        res.append(copy.deepcopy(source))
                        config=res[-1]
                        indice=config.conf[i].pop(0)
                        config.conf[j].append(indice)
                    elif source.conf[i][0]<source.conf[j][0]:
                        res.append(copy.deepcopy(source))
                        config = res[-1]
                        config.conf[j].reverse()
                        config.conf[j].append(config.conf[i][0])
                        config.conf[j].reverse()
    return res