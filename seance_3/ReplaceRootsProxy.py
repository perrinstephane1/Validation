from IdentityProxy import IdentityProxy

class ReplaceRootsProxy(IdentityProxy):
    def __init__(self, operand, newroots):
        super.__init__(operand)
        self.newroots=newroots

    def roots(self, ):
        return self.newroots