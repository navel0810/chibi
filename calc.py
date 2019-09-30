def calc(s):
    nums=map(int,s.split('+'))
    return sum(nums)

print(calc("1"))
print(calc("1+2"))
