if __name__ == '__main__':

     iC = P,C
     p = SoupProgram(iC)
     p.add(Rule("r1", lambda c : true, a1))
     p.add(Rule("r2", lambda c : true, a2))
     s = SoupSemantics(p)
     tr = Str2Tr(s)
     predicate_finder(tr, lambda c : c.x == c.y)