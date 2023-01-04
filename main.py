from parcours_largeur import *

graphe = {1: [2, 3], 2: [5, 6],
          3: [], 4: [4, 6], 5: [4],
          6: [6]}
res=parcours_largeur(graphe, 1)
print(res)

graphe2={0:[3,1], 1:[2], 2:[0], 3:[3, 4], 4:[1, 5], 5:[]}
print(parcours_largeur(graphe2, 0))