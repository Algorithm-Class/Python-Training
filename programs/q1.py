class que:
   def __init__(self,n):
       self.f=-1;
       self.r=-1;
       self.l=[];
       self.size=n;
       self.capacity=0;

   def enqueue(self,x) :
       if(self.capacity==self.size) :
          print("overflow")
          return 
       self.l.append(x)
       if(self.f==-1) :
         self.f=self.f+1
       self.r=self.r+1
       self.capacity=self.capacity+1
   def dequeue(self) :
       if(self.capacity==0) :
         print("undeR flow") 
         return
       print("capacity",self.capacity)
       print("front",self.f)
       self.capacity=self.capacity-1
       x=self.l[self.f];
       print("removed",x)
       del self.l[self.f];
       if( self.f==self.r):
         self.r=-1;
         self.f=-1;
      
       
        

   def display(self):
       print(self.l)
       




q1= que(5);

q1.enqueue(1);
q1.display()

q1.enqueue(2);
q1.display()

q1.enqueue(3);
q1.display()
q1.enqueue(4);
q1.display()
q1.enqueue(5);
q1.display()
q1.enqueue(6);
q1.display()

q1.dequeue();
q1.display()

q1.dequeue();
q1.display()

q1.dequeue();
q1.display()

q1.dequeue();
q1.display()

q1.dequeue();
q1.display()

q1.dequeue();
q1.display()






