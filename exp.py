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



v=Val(1)
print(v)
assert v.eval()==1

assert isinstance(v,Expr)
assert isinstance(v,Val)
assert isinstance(v,int)

class Add(Expr):
    __slots__=['left','right']
    def __init__(self,a,b):
        self.left=a
        self.right=b
    def eval(self):
        return self.left.eval() + self.right.eval()

class Mul(Expr):
    __slots__=['left','right']
    def __init__(self,a,b):
        self.left=a
        self.right=b
    def eval(self):
        return self.left.eval() * self.right.eval()

class Sub(Expr):
    __slots__=['left','right']
    def __init__(self,a,b):
        self.left=a
        self.right=b
    def eval(self):
        return self.left.eval() - self.right.eval()

class Div(Expr):
    __slots__=['left','right']
    def __init__(self,a,b):
        self.left=a
        self.right=b
    def eval(self):
        return self.left.eval() // self.right.eval()

assert isinstance(Val(1),Expr)
assert isinstance(Div(Val(7),Val(2)),Expr)