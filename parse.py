from exp import Val,Add,Mul

def parse(s:str):
    if s.find('+')>0:
        pos=s.find('+')
        s1=s[0:pos]
        s2=s[pos+1:]
        num=Add(parse(s1),parse(s2))
        return num
    if s.find('*')>0:
        pos=s.find('*')
        s1=s[0:pos]
        s2=s[pos+1:]
        num=Mul(parse(s1),parse(s2))
        return num
    return Val(int(s))

e=parse("1*2+3")
print(e,e.eval())
