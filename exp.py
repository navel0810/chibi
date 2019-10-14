
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
    __slots__=['left','right']
    def __init__(self,a,b):
        self.left=a
        self.right=b
    def eval(self):
        return self.left.eval() * self.right.eval()

class Sub(object):
    __slots__=['left','right']
    def __init__(self,a,b):
        self.left=a
        self.right=b
    def eval(self):
        return self.left.eval() - self.right.eval()

class Div(object):
    __slots__=['left','right']
    def __init__(self,a,b):
        self.left=a
        self.right=b
    def eval(self):
        return self.left.eval() // self.right.eval()

e=Div(Val(7),Val(2))
assert e.eval()==3

print(e)