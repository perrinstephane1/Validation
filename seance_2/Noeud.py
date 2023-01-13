class Noeud():
    def __init__(self, list):
        self.list=list

    def __hash__(self):
        return 1
    def __eq__(self, other):
        i=0
        if len(self.list)!=len(other.list):
            return False
        while self.list[i]==other.list[i] and i<len(self.list)-1:
            i=i+1
        if i==len(self.list):
            return True
        else:
            return False