import copy
from itertools import combinations

from seance_1.parcours_largeur import bfs
from seance_2.NBits import NBits
from seance_2.Noeud import Noeud
from seance_2.TransitionRelation import TransitionRelation
from seance_2.HanoiGraph import HanoiGraph
from seance_2.HanoiConfiguration import HanoiConfiguration
from seance_2.test import monNext

#dict = {1: [2, 3], 2: [5, 6],
#          3: [], 4: [4, 6], 5: [4],
#          6: [6]}

def f1(s, v, acc):
    acc[0]+=1
    #if v==10:
    #    return True
    return False
#graphe=NBits([3], 4)
#print(graphe.next(graphe.roots()[0]))
#print(bfs(NBits([3],4), [0], f1, None, None))
tours=HanoiConfiguration(3,3)
#print(tours.next([[1,2,3],[],[]]))
#print(tours.roots())
hanoi_graphe=HanoiGraph(tours)
#print(hanoi_graphe.next(hanoi_graphe.roots()))
#print(hanoi_graphe.next(hanoi_graphe.roots()))
print(bfs(hanoi_graphe, [0], hanoi_graphe.hanoi_on_entry, None, None))
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