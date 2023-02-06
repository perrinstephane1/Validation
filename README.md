# Validation
Cours de Validation (2023)
avec sur la DBRANCH la crack internationale Delphine FOUQUET

# Explication de nos résultats
Dans cette partie, nous allons expliquer notre travail sur Hanoi et les trois versions d'Alice et Bob

###Hanoi
Une configuration de Hanoi est représentée par un tableau de tableaux : `[[0, 1, 2], [], []]`, où un tableau représente une tour de Hanoi et un chiffre représente un disque. La taille du disque est d'autant plus grande que le chiffre qui le représente est grand. De plus, le haut de la tour est le début du tableau : quand on ajoute un disque, il se met à l'indice 0 du tableau.  
Dans la fonction guarde(), il faut retourner False quand un mouvement ne peut pas être effectué (selon les règles du jeu de Hanoi) et True sinon. 
C'est ensuite dans la fonction change() qu'on définit ce qui se passe lors d'un mouvement : on enlève un disque d'une tour et on le rajoute à une autre tour si les conditions données par la garde sont vérifiées.  
Dans le main (main_seance_4.py), on définit une fonction hanoi_on_entry1() qui va arrêter le parcours de graphe bfs() si elle retourne True. Elle renvoie True quand le jeu est résolue, c'est-à-dire quand tous les disques sont dans l'ordre sur la dernière tour.

###Alice et Bob (AliceBob.py)
Une configuration de Alice et Bob est représentée comme pour Hanoi : `[[1], [], [2]]`, où le tableau de gauche représente chez Alice, le tableau du milieu représente le jardin et le tableau de droite représente chez Bob. Le chiffre 1 représente Alice et le chiffre 2 représente Bob.  
Pour cette première version de Alice et Bob, il n'y a pas d'état Wait. On fait comme pour Hanoi avec les fonctions garde(), change() et on_entry() mais en adaptant au cas Alice et Bob. Dans la fonction on_entry, on vérifie si le jardin contient à la fois Alice et Bob. C'est bien sur le cas, et il faut donc faire une deuxième version pour éviter cela.

###Alice et Bob version 2 (AliceBob2.py)
Dans cette version, on ajoute un état Wait à Alice et à Bob. La configuration est de la forme `[[1], [], [], [], [2]]` avec dans l'ordre de gauche à droite chez Alice, wait Alice, jardin, wait Bob, chez Bob.  
On introduit également un flag Alice et un flag Bob, qu'ils doivent lever (mettre à True) quand ils rentrent en état Wait. De plus, dans la garde, on empêche le mouvement de Wait au jardin quand le flag d'en face est levé.  
Dans la fonction on_entry, on retourne quand il n'y a plus d'actions possibles. On obtient à la fin la configuration `[[], [1], [], [2], []]`, c'est-à-dire que Alice et Bob sont tous les deux dans l'état Wait. C'est un deadlock.  
On fait alors une troisième version pour éviter ce deadlock.

###Alice et Bob version 3 (AliceBob3.py)
Dans cette version finale, si Alice est Bob sont tous les deux dans l'état Wait alors Bob retourne chez lui et baisse son drapeau.  
Dans on_entry, on retourne à nouveau quand il n'y a plus d'actions possibles et on peut avoir soit Bob dans le jardin, soit Alice dans le jardin mais pas les deux en même temps.

### Step Synchronous Product (SSP)
(Code dans le fichier `main_seance_7.py`)
Dans cette section, nous allons faire un test pour vérifier que notre implémentation est bien faite.
Nous allons nous attarder sur le cas Alice et Bob, version 2 (ie chacun on un état "wait" avant d'entrer dans la section
critique). Cela reprend la classe `AliceBob2` expliqué plus haut.
Dans la fonction `test` nous créons d'abord un `SoupSemantic` qui contient les règles de l'automate
qui représente Alice et Bob. 
Nous créons ensuite un automate d'acceptation à deux états qui ne contient juste un PC.
1 sera l'état de départ, 2 celui d'arrivée. Il on met une garde si on arrive à "Bob et Alice dans la Section Critique".
Dans la fonction de test (`fct_de_test`, on peut mettre la condition d'arrêt :
- la première ligne (non commentée) nous permet de chercher la configuration où Alice est dans la zone d'attente et où Bob est dans la CS.
- la deuxième ligne permet de s'arrêter quand on arrive dans la section critique ensemble
Enfin, l'appel à `predicate_finder` puis à `getTrace` nous permet d'afficher la suite des opération pour arriver dans cet état.

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
- InitialConfigurations():List\<C\>
- enabledActions(C source): List\<A\>
- execute(A action, C source): List\<C\>
 
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
soup.add('flip 0', lambda x: True, flip0)
soup.add('flip 1', lambda x: True, flip1)

def execute(self, action, c):
    t = copy.deepcopy(c)
    o=a(t)
    return o # pas trop sûr

class PredAutomConfig:
    def __init__(self):
        self.pc=0
    # eq et hash

pSoup=iSoupProgram(PredAutomConfig())
pSoup.add('p', lambda i c:c.pc=i and predicate, action)

class InupuSemTransRelation():
    def __init__(self):
        pass   
    def initial(self):pass
    def actions(self, input, source):
        pass
    def execute(self, action, input, source):
        pass

class InputSoupSemantics():
    def __init__(self):
        pass
    def actions(self, input, source):
        pass
    #filter (lambda c:c.guard(input, source), self.program.rules)
    #execute(self, action, input, source)
```
On rajoute un champ input à toutes nos méthodes
```python
import copy


class InputSemanticTransitionRelation():
    def __init__(self): pass

    def enableActions(self, input, source): pass

    def execute(self, action, input, source): pass


class InputSoupSemantics(InputTransitionRelation):
    def __init__(self, program):
        self.prog = program

    def initial(self): return [self.prog.init]

    def enabledActions(self, input, source):
        return filter(lambda r: r.guard(input, source), self.prog.rules)

    def execute(self, action, input, source):
        target = copy.deepcopy(source)
        n=action(input, target)
        return [target]
```

```python
class MaybeStatter():
    def __init__(self, source, action, target):
        self.source=source
        self.target=target
        self.action=action
class Stutter(MaybeStatter):
class Step():
class Action(MaybeStatter):
class StepSynchronousProduct(SemanticTransitionRelation):
    def __init__(self, lhs, rhs):
        self.lhs=lhs
        self.rhs=rhs
    def initial(self):
        r=[]
        for lc in lhs.initial():
            for rc in rhs.initial():
                r.append((lc, rc))
        return r
    def enabledActions(self, source):
        ls, rc=source
        synchA=[]
        lhs_enA=self.lhs.enabledActions(ls)
        nbreActions=len(lhs_enA)
        for la in lhs_enA:
            targets=self.lhs.execute(lhs.a, ls)
            if len(targets==0):
                nbreActions-=1
            #partie sans deadlock
            for lt in targets:
                rhs_enA=self.rhs.enabledActions(Step(lc, la, lt), rs)
                synchA.append(map(lambda rc:(Step(lc, la, lt)), rhs_enA))
            #on est dans un deadlock
            if nbreActions==0:
                step=Step(lc, Stutter(), lc)
                rhs_enA=self.rhs.enabledActions(step, rs)
                synchA.append(map(lambda ra:(step,ra), rhs_enA))
        return synchA
    def execute(self,action, source):
        step, ra=action
        ls, rs = source
        r_T=self.rhs.execute(ra, step, rs)
        return map(lambda rt:(step.target, rt) , R_T)
```
###Suite des évènements


si vous avez réussi à suivre, pour tout prédicat que vous aviez la dernière fois vous pouvez les encoder avec de automates comme ça.

La suite : détecter les cycles...
Il parait que c'est pas dur

# Séance du 30 Janvier
Compréhension du program de `StepSynchronousProduct`