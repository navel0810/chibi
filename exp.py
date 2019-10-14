
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

v=Val(1)
assert v.eval()==1

e=Add(Val(1),Add(Val(2),Val(3)))
assert e.eval()==3

print(e)