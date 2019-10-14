
class Val(object):
    __slots__=['value']
    def __init__(self,value=0):
        self.value=value
    def __repr__(self):
        return f'Val({self.value})'
    def eval(self):
        return self.value

class Add(object):
    __slots__=['left','right']
    def __init__(self,a,b):
        self.left=a
        self.right=b
    def eval(self):
        return self.left.eval() + self.right.eval()

class Mul(object):
    __slots__=['x1','x2']
    def __init__(self,a,b):
        self.x1=a
        self.x2=b
    def eval(self):
        return self.x1.eval() * self.x2.eval()


e=Mul(Val(1),Val(2))
assert e.eval()==2

print(e)