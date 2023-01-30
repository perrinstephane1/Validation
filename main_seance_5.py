from seance_1.predicate_finder import predicate_finder
from seance_3.ParentTraceProxy import ParentTraceProxy, getTrace
from seance_5.AliceBob import AliceBob, guardeAB, changeAB
from seance_5.AliceBob2 import AliceBob2, changeAB2
from seance_4.Rule import Rule
from seance_4.SoupProgram import SoupProgram
from seance_4.SoupSemantics import SoupSemantics
from seance_4.Str2Tr import Str2Tr
from seance_1.parcours_largeur import bfs

if __name__ == '__main__':
     '''
     ABconf = AliceBob()
     iC = ABconf
     prog = SoupProgram(iC)
     # générer les règles pour AliceBob
     for i in range(3):
          for j in range(3):
               if i != j:
                    prog.add(Rule('{} vers {}'.format(i, j), guardeAB(i, j), changeAB(i, j)))
     # for k in range(len(prog.rules)):
     #     print(prog.rules[k])
   
     s = SoupSemantics(prog)
     translater = Str2Tr(s)
     dict = {}
     ptp = ParentTraceProxy(translater, dict)
     [p, found, count, target], known = predicate_finder(ptp, iC.AB_on_entry)
     print(getTrace(dict, target))
     '''
     # deadlock
     ABconf=AliceBob2()
     iC = ABconf
     prog = SoupProgram(iC)
     # générer les règles pour AliceBob2
     for i in range(5):
          for j in range(5):
               if i!=j:
                    prog.add(Rule('{} vers {}'.format(i, j), ABconf.guardeAB2(i,j), changeAB2(i,j)))

     s = SoupSemantics(prog)
     translater = Str2Tr(s)

     o = [s]
     bfs(translater, o, iC.AB2_on_entry2)

     '''
     dict={}
     ptp=ParentTraceProxy(translater, dict)
     [p, found, count, target], known = predicate_finder(ptp, iC.AB2_on_entry)
     print(getTrace(dict, target))
     '''