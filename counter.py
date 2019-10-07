class Counter(object):
    def __init__(self): #コンストラクタ
        self.cnt=0
    
    def count(self):
        self.cnt+=1

    def doublecount(self):
        self.cnt+=2

    def reset(self):
        self.cnt=0

    def show(self):
        print(self.cnt)

    def __repr__(self): #文字列を返すと表示される
        return str(self.cnt)

c=Counter()
c.show()
c.count()
c.show()
c.doublecount()
c.show()