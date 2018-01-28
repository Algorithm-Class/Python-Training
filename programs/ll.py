class node:

   def __init__(self,data):
       self.data=data;
       self.next=None;
   def get_data(self):
       return self.data;
   def get_next(self):
       return self.next
   def set_left(self,node1):
       self.next=node1

class ll :
   def __init__(self):
      self.head=None;
   def insert_front(self,data):
       new_node=node(data)
       new_node.next=self.head;
       self.head=new_node
   def display(self):
       p=self.head
       while (p) :
          print(p.get_data(), end=' ')
          p=p.get_next();


   

l1=ll();
l1.insert_front(1);
l1.insert_front(2);
l1.insert_front(3);

l1.display()
node1=node(1)
