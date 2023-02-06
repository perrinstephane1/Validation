# Test du SSP avec une version d'Alice et Bob
from seance_1.predicate_finder import predicate_finder
from seance_3.ParentTraceProxy import ParentTraceProxy, getTrace
from seance_4.Rule import Rule
from seance_4.SoupProgram import SoupProgram
from seance_4.SoupSemantics import SoupSemantics
from seance_4.Str2Tr import Str2Tr
from seance_5.AliceBob2 import AliceBob2

## base : Alice et Bob avec Drapeau - Schéma juste avant l'exercice 6
from seance_5.Conf2 import Conf2
from seance_5.InputSoupSemantics import InputSoupSemantics
from seance_5.StepSynchronousProduct import StepSynchronousProduct


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
    p =SoupSemantics(prog)

    ## Automate d'acceptation :
    conf=Conf2()
    guarde=lambda i,c : c.PC==1

    def guarde2(i, c):
        return c.PC == 1 and not (2 in i.source.conf[2]) and not (2 in i.source.conf[2])

    def a2(i, c):
        c.PC=2

    def fct_de_test(n):
        #print(n[0].conf)
        return (2 in n[0].conf[2]) and (1 in n[0].conf[1])
        #return (2 in n[0].conf[2]) and (1 in n[0].conf[2])
        #return True

    programg=SoupProgram(conf)
    programg.add(Rule('ne rien faire', guarde, None))
    programg.add(Rule('avancer', guarde2, a2))
    m=InputSoupSemantics(programg)

    ## SSP
    ssp=StepSynchronousProduct(p, m)
    # l=ssp.initial()
    translater = Str2Tr(ssp)
    dict = {}
    ptp = ParentTraceProxy(translater, dict)
    [p, found, count, target], known = predicate_finder(ptp, fct_de_test)
    if found:
        print(getTrace(dict, target))

test()