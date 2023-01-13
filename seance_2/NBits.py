from seance_2.TransitionRelation import TransitionRelation


class NBits(TransitionRelation):
    def __init__(self, root, n):
        self.root = root
        self.n = n

    def roots(self):
        return self.root

    def next(self, source):

        res = []
        for i in range(self.n):
            if ((source >> i) & 1) > 0:
                r = source & ~(1 << i)
                # print(r)
                res.append(r)
            else:
                r = source | (1 << i)
                # print(r)
                res.append(r)
        return res
