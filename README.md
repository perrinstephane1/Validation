# Validation
Cours de Validation 2023
##Etape 1
on crée un parcours de graphe en largeur
Le graphe est une liste d'adjacente sous la forme d'un dictionnaire

On le teste avec les deux graphes donnés en exemple
```python
graphe = {1: [2, 3], 2: [5, 6],
          3: [], 4: [4, 6], 5: [4],
          6: [6]}

graphe2={0:[3,1], 1:[2], 2:[0], 3:[3, 4], 4:[1, 5], 5:[]}
```
et on obtient les résultats suivant en partant des sommets 1 et 0 :
```bash
{1: 1, 2: 1, 3: 1, 5: 2, 6: 2, 4: 5}
{0: 0, 3: 0, 1: 0, 2: 1, 4: 3, 5: 4}
```
Cela correspond à la liste des parents par lesquels on accède à un noeud. Il suffit ensuite de remonter les noeuds jusqu'à arriver au noeud racine.

En revanche cela dépend du modèe d'implémentation du graphe : on peut par exemple créer des fonctions qu'on implémentera (pex : g.initial ou g.next pour avoir la source/avoir les sommets fils)

## Etape 2
Nous devons faire une fonction `graph_include` qui détermine si une `target` est accessible.
Nous nous intéresserons au cas où le graphe aura de manière certaine UN état initial donc on peut se contenter de le faire une seule fois.

## Etape 3
(source, neighbour, 0:accumulateur)
1) bool on_entry(s,n,0)
2) bool on_known(s,n,0)
3) bool on_exit(n,0)

Ce sont des fonctions à ajouter juste au bon moment, un peu comme les changements d'état découvert/traité/non-découvert. Ces fonctions sont ensuite à implémenter pour pouvoir agir au moment où on parcourt le graphe. 