class stk:
   def __init__(self,n) :
       self.size=n;
       self.top=-1;
       self.l=[]
   def push(self,x) :
       if(self.top== self.size-1) :
          print("overflow");
          return 
       self.l.append(x);
       self.top=self.top + 1
   def pop(self) :
       if(self.top==-1) :
          print("under flow")
          return;
       x=self.l[self.top]
       print("removed",x)
       del self.l[self.top]
       self.top=self.top-1
       return x
   def display(self) :
      print(self.l)

s1=stk(5)

s1.push(1)
s1.display()

s1.push(2)
s1.display()

s1.push(3)
s1.display()

s1.push(4)
s1.display()

s1.push(5)
s1.display()

s1.push(6)
s1.display()

s1.pop()
s1.display()

s1.pop()
s1.display()
s1.pop()
s1.display()
s1.pop()
s1.display()
s1.pop()
s1.display()
s1.pop()
s1.display()

        