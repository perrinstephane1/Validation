from seance_4.SemanticTransitionRelation import SemanticTransitionRelation
from seance_5.Action import Action
from seance_5.Step import Step
from seance_5.Stutter import Stutter


class StepSynchronousProduct(SemanticTransitionRelation):

    def __init__(self, lhs, rhs):
        self.lhs = lhs # modèle SoupSemantic
        self.rhs = rhs # propriété InputSoupSemantic

    def initial(self):
        r = []
        for lc in self.lhs.initial():
            for rc in self.rhs.initial():
                r.append((lc, rc))
        return r

    def enabledActions(self, source):
        ls, rs = source
        syncA = []
        lhs_enA = self.lhs.enabledActions(ls)
        numActions = len(lhs_enA)
        # Pas deadlock
        for la in lhs_enA:
            l_targets = self.lhs.execute(la, ls)
            if len(l_targets) == 0:
                numActions -= 1
            for lt in l_targets:
                step = Step(ls, Action(la), lt)
                rhs_enA = self.rhs.enabledActions(step, rs)
                syncA.append(map(lambda ra : (step, ra), rhs_enA))
                #syncA.append(map(lambda ra: (la, ra), rhs_enA))

        # Deadlock stutter
        if numActions == 0:
            step = Step(ls, Stutter(), ls)
            rhs_enA = self.rhs.enabledActions(step, rs)
            syncA.append(map(lambda ra: (step, ra), rhs_enA))
            #syncA.append(map(lambda ra: (None, ra), rhs_enA))

        return syncA

    def execute(self, action, source):
        ls, rs = source
        step, ra = action
        r_T = self.rhs.execute(ra, step, rs)
        return map(lambda rt: (step.target, rt), r_T)