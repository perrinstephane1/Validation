from seance_1.predicate_finder import predicate_finder
from seance_3.ParentTraceProxy import ParentTraceProxy, getTrace
from seance_5.AliceBob import AliceBob, guardeAB, changeAB
from seance_5.AliceBob2 import AliceBob2
from seance_5.AliceBob3 import AliceBob3, changeAB3
from seance_4.Rule import Rule
from seance_4.SoupProgram import SoupProgram
from seance_4.SoupSemantics import SoupSemantics
from seance_4.Str2Tr import Str2Tr
from seance_1.parcours_largeur import bfs

def mainAliceBob():
    ABconf = AliceBob()
    iC = ABconf
    prog = SoupProgram(iC)
    # générer les règles pour AliceBob
    for i in range(3):
        for j in range(3):
            if i != j:
                prog.add(Rule('{} vers {}'.format(i, j), guardeAB(i, j), changeAB(i, j)))

    s = SoupSemantics(prog)
    translater = Str2Tr(s)
    dict = {}
    ptp = ParentTraceProxy(translater, dict)
    [p, found, count, target], known = predicate_finder(ptp, iC.AB_on_entry)
    print(getTrace(dict, target))


def mainAliceBob2():
    ABconf = AliceBob2()
    iC = ABconf
    prog = SoupProgram(iC)
    # générer les règles pour AliceBob2
    for i in range(5):
        for j in range(5):
            if i != j:
                prog.add(Rule('{} vers {}'.format(i, j), ABconf.guardeAB2(i, j), ABconf.changeAB2(i, j)))

    s = SoupSemantics(prog)
    translater = Str2Tr(s)

    o = [s]
    bfs(translater, o, iC.AB2_on_entry2)


def mainAliceBob3():
    ABconf = AliceBob3()
    iC = ABconf
    prog = SoupProgram(iC)
    # générer les règles pour AliceBob3
    for i in range(5):
        for j in range(5):
            if i != j:
                prog.add(Rule('{} vers {}'.format(i, j), ABconf.guardeAB3(i, j), changeAB3(i, j)))

    s = SoupSemantics(prog)
    translater = Str2Tr(s)

    o = [s]
    bfs(translater, o, iC.AB3_on_entry2)

    #dict = {}
    #ptp = ParentTraceProxy(translater, dict)
    #[p, found, count, target], known = predicate_finder(ptp, iC.AB3_on_entry)
    #print(getTrace(dict, target))


if __name__ == '__main__':
    # mainAliceBob()
    # mainAliceBob2()
    mainAliceBob3()
