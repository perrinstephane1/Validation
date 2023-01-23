from seance_4.SemanticTransitionRelation import SemanticTransitionRelation

class StepSynchronousProduct(SemanticTransitionRelation):

    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def initial(self):
        r = []
        for lc in lhs.initial():
            for rc in rhs.initial():
                r.append((lc, rc))
        return r

    def enabledActions(self, source):
        ls, rs = source
        syncA = []
        lhs_enA = self.lhs.enabledActions(ls)
        numActions = length(lhs_enA)
        # Pas deadlock
        for la in lhs_enA:
            l_targets = self.lhs.execute(la, ls)
            if length(l_targets) == 0:
                numActions -= 1
            for lt in l_targets:
                step = Step(lc, Action(la), lt)
                rhs_enA = self.rhs.enabledActions(step, rs)
                syncA.extend(map(lambda ra : (Step, ra), rhs_enA))

        # Deadlock stutter
        if numActions == 0:
            step = Step(lc, Stutter(), lc)
            rhs_enA = self.rhs.enabledActions(step, rs)
            syncA.extend(map(lambda ra: (step, ra), rhs_enA))

        return syncA

    def execute(self, action, source):
        ls, rs = source
        step, ra = action
        r_T = self.rhs.execute(ra, step, rs)
        return map(lambda rt: (step.target, rt), r_T)