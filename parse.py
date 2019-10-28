from exp import Val,Add

def parse(s:str):
    pos=s.find('+')
    if pos==-1:
        return Val(int(s))
    else:
        s1=s[0:pos]
        s2=s[pos+1:]
        num=Add(parse(s1),parse(s2))
        return num

e=parse("1+2+3")
print(e,e.eval())
