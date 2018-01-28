class Calc:
   def __init__(self,a,b):
       self.c=a
       self.d=b
   def add(self):
       e=self.c+self.d
       return (e)
   def sub(self):
       f=self.c-self.d
       print(f)

abc=Calc(30,15)
b=abc.add()
print(b)
print(abc.add())
abc.sub()
