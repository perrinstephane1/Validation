import copy
from itertools import combinations

from seance_1 import *
from seance_2 import *
from seance_2.Classes import NBits

dict = {1: [2, 3], 2: [5, 6],
          3: [], 4: [4, 6], 5: [4],
          6: [6]}


graphe=NBits(dict, [1])
print(graphe.roots())
print(graphe.next([True, True]))