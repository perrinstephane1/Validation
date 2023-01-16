from seance_1.predicate_finder import predicate_finder
from seance_4.Config1 import Config1
from seance_4.Rule import Rule
from seance_4.SoupProgram import SoupProgram
from seance_4.SoupSemantics import SoupSemantics
from seance_4.Str2Tr import Str2Tr

if __name__ == '__main__':

     iC = Config1()
     p = SoupProgram(iC)
     p.add(Rule("r1", lambda c : True, a1))
     p.add(Rule("r2", lambda c : True, a2))
     s = SoupSemantics(p)
     tr = Str2Tr(s)
     predicate_finder(tr, lambda c : c.x == c.y)