import copy
from itertools import combinations

from seance_1.parcours_largeur import bfs
from seance_2 import *
from seance_2.Classes import *
from seance_2.Hanoi import *
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
#print(bfs(hanoi_graphe, [0], hanoi_on_entry, None, None))
res=monNext(tours)
for k in range(len(res)):
    print(res[k].conf)

coucou=monNext(res[1])
for k in range(len(coucou)):
    print(coucou[k].conf)