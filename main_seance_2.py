import copy
from seance_1.parcours_largeur import bfs
from seance_2.NBits import NBits
from seance_2.Noeud import Noeud
from seance_2.TransitionRelation import TransitionRelation
from seance_2.HanoiGraph import HanoiGraph
from seance_2.HanoiConfiguration import HanoiConfiguration
from seance_2.test import monNext


def f1(s, v, acc):
    acc[0]+=1
    #if v==10:
    #    return True
    return False

def testNBits():
    graphe=NBits([3], 4)
    #print(graphe.next(graphe.roots()[0]))
    print(bfs(NBits([3],4), [0], f1, None, None))

def testHanoi():
    tours=HanoiConfiguration(3,3)
    #print(tours.next([[1,2,3],[],[]]))
    #print(tours.roots())
    hanoi_graphe=HanoiGraph(tours)
    #print(hanoi_graphe.next(hanoi_graphe.roots()))
    #print(hanoi_graphe.next(hanoi_graphe.roots()))
    print(bfs(hanoi_graphe, [0], hanoi_graphe.hanoi_on_entry, None, None))

if __name__=="__main__":
    testHanoi()