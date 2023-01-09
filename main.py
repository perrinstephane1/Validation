import copy
from itertools import combinations

from seance_1.parcours_largeur import bfs
from seance_2 import *
from seance_2.Classes import *

dict = {1: [2, 3], 2: [5, 6],
          3: [], 4: [4, 6], 5: [4],
          6: [6]}

def f1(s, v, acc):
    acc[0]+=1
    return False
graphe=NBits([3], 4)
#print(graphe.next(graphe.roots()[0]))
print(bfs(NBits([3],4), [0], f1, None, None))

if __name__ == '__main__':
    jeu = HanoiConfiguration(3, 3)
    jeu.next([[3,2,1], [], []])
