from seance_1.predicate_finder import predicate_finder
from seance_2.HanoiConfiguration import HanoiConfiguration
from seance_4.Config1 import Config1
from seance_4.Rule import Rule
from seance_4.SoupProgram import SoupProgram
from seance_4.SoupSemantics import SoupSemantics
from seance_4.Str2Tr import Str2Tr

def guarde(i, j):
     def res(config):
          if config.conf[i]==[]:
               return False
          indice=config.conf[i][0]
          if config.conf[j]==[]:
               return True
          if config.conf[j][0]>indice:
               return True
          else:
               return False
     return res

def change(i, j):
     def res(config):
          indice=config.conf[i].pop(0)
          config.conf[j]=[indice]+config.conf[j]
          return config
     return res

if __name__ == '__main__':
     hanConf=HanoiConfiguration(3, 3)

     iC = hanConf

     prog = SoupProgram(iC)
     # générer les règles pour hanoi
     for i in range(3):
          for j in range(3):
               if i!=j:
                    prog.add(Rule('{} vers {}'.format(i, j), guarde(i,j), change(i,j)))
     for k in range(len(prog.rules)):
          print(prog.rules[k])

     s = SoupSemantics(prog)
     #tr = Str2Tr(s)
     #predicate_finder(tr, lambda c : c.x == c.y)