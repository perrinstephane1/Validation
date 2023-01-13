import copy
from itertools import combinations


from seance_2.NBits import NBits
from seance_2.Noeud import Noeud
from seance_2.TransitionRelation import TransitionRelation
from seance_2.HanoiGraph import HanoiGraph
from seance_2.HanoiConfiguration import HanoiConfiguration
from seance_2.test import monNext





#res=monNext(tours)
def test():
    while len(res)>0:
        test=monNext(res[0])
        bonjour=res.pop(0)
        print("->on traite")
        print(bonjour.conf)
        for k in range(len(test)):
            res.append(test[k])
            print(test[k].conf)
        print("----------------------------")
        if hanoi_graphe.hanoi_on_entry(0,bonjour,0):
            print("GAGNE")
            break
tours.conf=[[1, 2], [0], []]
#monNext(tours)
#test()




# monTest=HanoiConfiguration(3,3)
# monTest.conf=[[],[],[0,1,2]]
# print(monTest.conf)
# print(hanoi_on_entry(1, monTest, 0))