class Calculator:
    def add(self, *args):
        return sum(args)
    
    def add(self,a,b):
        return a+b
    def add(self,a,b,c):
        return a+b+c

c = Calculator()
print(c.add(2, 3))        # 5
print(c.add(2, 3, 4))     # 9
