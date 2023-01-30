from seance_4.AConfig import AConfig
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

# à droite
conf=Conf2()
program=SoupProgram(conf)
p=InputSoupSemantics(program)

# à gauche
confg=Conf3()
programg=SoupProgram(confg)
m=SoupSemantics(programg)

# test
ssp=StepSynchronousProduct(m,p)
print(ssp.enabledActions)