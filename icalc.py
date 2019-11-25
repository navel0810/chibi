import pegpy

peg = pegpy.grammar('''
Expression = Product (^{ '+' Product #Add })*
Product = Value (^{ '*' Value #Mul })*
Value = { [0-9]+ #Int }
''')
parser = pegpy.generate(peg)

class Expr(object):
    @classmethod
    def new(cls,v):
        if isinstance(v,Expr):
            return v
        return Val(v)

class Val(Expr):
    __slot__=['value']

    def __init__(self,value):
        self.value=Value

    def __repr__(self):
        return f'Val({self.value})'

    def eval(self,env:dict):
        return self.value

e = Val(0)
assert e.eval({})==0

class Binary(Expr):
    __slot__=['left','right']

    def __init__(self,left,right):
        self.left = Expr.new(left)
        self.right = Expr.new(right)

    def __repr__(self):
        classname = self.__class__.__name__
        return f'{classname}({self.left},{self.right})'

class Add(Binary):
    __slot__ = ['left','right']

    def eval(self,env:dict):
        return self.left.eval(env)+self.right.eval(env)

class Sub(Binary):
    __slot__ = ['left','right']

    def eval(self,env:dict):
        return self.left.eval(env)-self.right.eval(env)

class Mul(Binary):
    __slot__ = ['left','right']

    def eval(self,env:dict):
        return self.left.eval(env)*self.right.eval(env)

class Div(Binary):
    __slot__ = ['left','right']

    def eval(self,env:dict):
        return self.left.eval(env)//self.right.eval(env)



def calc(t):
    if t == 'Int':
        return int(str(t))
    if t == 'Add':
        return calc(t[0])+calc(t[1])
    if t == 'Mul':
        return calc(t[0]) * calc(t[1])
    print(f'TODO{t.tag}')
    return 0

t = parser('1+2*3+4*5')
print(repr(t))
print(calc(t))




def main():
    s = input('>>>')
    t = parser(s)
    print(calc(t))

if __name__ == '__main__':
    main()

