from main_seance_4 import hanoi_on_entry1
from seance_1.predicate_finder import predicate_finder
from seance_3.ParentTraceProxy import ParentTraceProxy, getTrace
from seance_4.AConfig import AConfig
from seance_4.Rule import Rule
from seance_4.SoupProgram import SoupProgram
from seance_4.SoupSemantics import SoupSemantics
from seance_4.Str2Tr import Str2Tr
from seance_5.Conf2 import Conf2, Conf3
from seance_5.InputSoupSemantics import InputSoupSemantics
from seance_5.StepSynchronousProduct import StepSynchronousProduct
from seance_5.Stutter import Stutter

g1=lambda i,c : c.PC==1
def a1(i, c):
    c.PC=1

g2=lambda i,c: c.PC==1 and i.action is Stutter()
def a2(i, c):
    c.PC=2

g3=lambda c : c.PC=='a'
def a3(c):
    c.PC='b'

def fct_de_test(n):
    print(n)
    return True
# à droite
conf=Conf2()
program=SoupProgram(conf)
program.add(Rule('règle 1', g1, a1))
program.add(Rule('règle 2', g2, a2))
p=InputSoupSemantics(program)

# à gauche
confg=Conf3()
programg=SoupProgram(confg)
programg.add(Rule('R1', g3, a3))
m=SoupSemantics(programg)
ssp=StepSynchronousProduct(m,p)

def test():

    l=ssp.initial()

    step, rule=ssp.enabledActions(l[0])[0][0]

    #action=?
    source=(ssp.lhs, ssp.rhs)
    res=ssp.execute((step, rule), source)
    print(res)

def test2():
    translater = Str2Tr(ssp)
    dict = {}
    ptp = ParentTraceProxy(translater, dict)
    [p, found, count, target], known = predicate_finder(ptp, fct_de_test)
    print(getTrace(dict, target))

test2()