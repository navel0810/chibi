import math

class Q(object):
    def __init__(self,a,b=1):
        gcd=math.gcd(a,b)
        self.a=a//gcd
        self.b=b//gcd

    def __repr__(self):
        if self.b==1:
            return str(self.a)

        return f'{self.a}/{self.b}'

    def __add__(self,q):
        a=self.a
        b=self.b
        c=q.a
        d=q.b
        return Q(a*d+b*c,b*d)

    def __sub__(self,q):
        a=self.a
        b=self.b
        c=q.a
        d=q.b
        return Q(a*d-b*c,b*d)

    def __mul__(self,q):
        a=self.a
        b=self.b
        c=q.a
        d=q.b
        return Q(a*c,b*d)

    def __truediv__(self,q):
        a=self.a
        b=self.b
        c=q.a
        d=q.b
        return Q(a*d,b*c)


q1=Q(1,2)
q2=Q(1,3)
print(q1/q2)