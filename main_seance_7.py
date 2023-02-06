# Test du SSP avec une version d'Alice et Bob
from seance_4.Rule import Rule
from seance_4.SoupProgram import SoupProgram
from seance_4.SoupSemantics import SoupSemantics
from seance_5.AliceBob2 import AliceBob2

## base : Alice et Bob avec Drapeau - Schéma juste avant l'exercice 6
from seance_5.Conf2 import Conf2
from seance_5.InputSoupSemantics import InputSoupSemantics


def test():
    ## alice et Bob
    ABconf = AliceBob2()
    iC = ABconf
    prog = SoupProgram(iC)
    # générer les règles pour AliceBob2
    for i in range(5):
        for j in range(5):
            if i != j:
                prog.add(Rule('{} vers {}'.format(i, j), ABconf.guardeAB2(i, j), ABconf.changeAB2(i, j)))

    #s = SoupSemantics(prog)
    p = InputSoupSemantics(prog)

    ## Automate d'acceptation :
    conf=Conf2()
    guarde=lambda i,c : c.PC==1

    def guarde2(i, c):
        return c.PC == 1 and not (2 in i.conf[2]) and not (2 in i.conf[2])

