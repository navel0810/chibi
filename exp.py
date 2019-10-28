class Expr(object):
    pass

class Val(Expr):
    __slots__=['value']
    def __init__(self,value=0):
        self.value=value
    def __repr__(self):
        return f'Val({self.value})'
    def eval(self):
        return self.value

class Binary(Expr):
    def __init__(self,left,right):
        self.left=left
        self.right=right
    def __repr__(self):
        classname=self.__class__.__name__
        return f'{classname}({self.left},{self.right})'

v=Val(1)
assert v.eval()==1

assert isinstance(v,Expr)
assert isinstance(v,Val)
assert not isinstance(v,int)

def toExpr(a):
    if not isinstance(a,Expr):
        a=Val(a)
    return a

class Add(Binary):
    def __init__(self,a,b):
        self.left=toExpr(a)
        self.right=toExpr(b)
    def eval(self):
        return self.left.eval() + self.right.eval()

class Mul(Binary):
    def __init__(self,a,b):
        self.left=toExpr(a)
        self.right=toExpr(b)
    def eval(self):
        return self.left.eval() * self.right.eval()

class Sub(Binary):
    def __init__(self,a,b):
        self.left=toExpr(a)
        self.right=toExpr(b)
    def eval(self):
        return self.left.eval() - self.right.eval()

class Div(Binary):
    def __init__(self,a,b):
        self.left=toExpr(a)
        self.right=toExpr(b)
    def eval(self):
        return self.left.eval() // self.right.eval()

assert not isinstance(Val(1),Binary)
assert isinstance(Div(Val(7),Val(2)),Binary)
e=Mul(Add(1,2),3)
assert e.eval()==9