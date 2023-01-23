# Validation
Cours de Validation (2023)

## Cours du 4 janvier
###Etape 1
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

### Etape 2
Nous devons faire une fonction `graph_include` qui détermine si une `target` est accessible.
Nous nous intéresserons au cas où le graphe aura de manière certaine UN état initial donc on peut se contenter de le faire une seule fois.

### Etape 3
(source, neighbour, 0:accumulateur)
1) bool on_entry(s,n,0) pour arreter la progression dans l'arbre sous une certaine condition
2) bool on_known(s,n,0) -> à ahcaque fois qu'on revient sur un noed connu
3) bool on_exit(n,0)

Ce sont des fonctions à ajouter juste au bon moment, un peu comme les changements d'état découvert/traité/non-découvert. Ces fonctions sont ensuite à implémenter pour pouvoir agir au moment où on parcourt le graphe. 

On a rajouté l'algo `bfs`qui est celui au tableau, la file à double entrée permet de pop à coût constant.

## cours du 9 janvier
On voudrait un truc du genre :
```python
class TransitionRelation:
    @abstractmethod
    def roots(self):
        pass
    @abstractmethod
    def next(self, source):
        pass
```
On va essayer d'implémenter ça.
On voudrait une fonction qui recherche un noeud qui a des conditions particulières.
On crée une fonction next qui donne toutes les modificiations d'un bit : '101' revoie toutes les modifications.
On essaie de générer un graphe.

On a ensuite implémenté le jeu de hanoi, en finissant sur : le bfs s'arrête quand on a gagné (codage de la fonction `hanoi_on_entry` qui indique si on a gagné)
##Séance du 13 janvier
1) traçage : on veut savoir comment on arrive à l'état gagné
2) eDSL : embedded DSL

### solution avec un dictionnaire 
On ne veut pas faire un dictionnaire de parents, on veut plutôt construire l'arbre des parents
pendant l'appel de `roots()` et `next()`.

on définit une classe `identityProxy` avec un seul attribut `operand`, et un `getattr` qui retourne l'operande:
```python
def __getattr__(self, attr):
    return getattr(self.operand, attr)
```
On va faire hériter de cette classe-là en chngeant les méthodes.
```python
class ParentTraceProxy(IdentityProxy):
    def __init__(self, operand, dict):
        self.operand=operand
        self.dict=dict
    def roots(self):
        #doit appeler la fonction roots de l'operande et mettre à jour les parents
        neighboors=self.operand.roots()
        # maj du dico
        pass
    def next(self, source):
        neighboors=self.operand.next(source)
        # maj...
        pass
```

### Séance du 16 janvier
class SemanticsTransitionRelation
méthodes :
- InitialConfigurations():List<C>
- enabledActions(C source): List<A>
- execute(A action, C source): List<C>
 
 fonction `str2tr(a Str): TR` toute seule !

*next* : ce qu'on fait jusqu'à présent
- deepcopy
- identifier les actions possibles
- on les exécute

```python
import copy


class Rule:
    def __init__(self, name, guard, action):
        self.name = name
        self.guard = guard
        self.action = action
    def execute(self, config): return [self.action(config)]


class SoupProgram():
    # possède les trois fonctions plus haut
    def __init__(self, ini):
        self.ini = ini
        self.rules = []

    def add(self, rule):
        self.rules.append(rule)


class SoupSemantics(SemanticTransitionRelation):
    def __init__(self, program):
        self.program = program

    def initialConfiguration(self):
        return [self.program.ini]

    def enabledAction(self, source):
        return filter(labdafct, r.guard(source), program.rules)

    def execute(self, action, source):
        target = copy.deepcopy(source)
        return action.execute(t)

```

# séance du 23 Janvier:
## Implémentation du début d'Alice et Bob
3 premiers versions du TD Vérif
- Alice et Bob qui violent la CS : contre exemple
- deadlock !
- livelock

## au tableau

```python
import copy


class NBitsConfig():
    def __init__(self, n):
        self.value = 0
    # __eq__
    # __hash__


soup = SoupProgram(NBitsConfig)
soup.add('flip 0', lambda x: True, flip)


def execute(self, action, c):
    t = copy.deepcopy(c)
    o=a(t)
    return 
```