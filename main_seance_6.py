from seance_4.AConfig import AConfig
from seance_4.Rule import Rule
from seance_4.SoupProgram import SoupProgram
from seance_4.SoupSemantics import SoupSemantics
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

# test
ssp=StepSynchronousProduct(m,p)
l=ssp.initial()

step, rule=ssp.enabledActions(l[0])[0][0]

#action=?
source=(ssp.lhs, ssp.rhs)
res=ssp.execute((step, rule), source)
print(res)