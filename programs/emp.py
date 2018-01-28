#Base class
class emp :
  # Class variable or Static variable  
  count=0;

  # Base class constructor
  def __init__(self,name,dept):
     self.name=name
     self.dept=dept
     emp.count=emp.count+1
     print("Parent constructor")
  def get_name(self):
     return (self.name);
  def get_dept(self):
     return self.dept
  def display(self):
     print("name=%s, dept=%s"%(self.name,self.dept))

class perm_emp(emp):
  
  #Child constructor
  def __init__(self,name,dept,PF,empid):
      # Parent constructor
      emp.__init__(self,name,dept) 
      print("Child constructor")
      self.empid=empid
      # Data Hiding
      self.__PF=PF
  def get_empid(self):
      return self.empid
  def get_getpf(self):
      return self.__PF
  def display(self) :
      # parent function
     # self.display()
      print("empid %d PF %d"%(self.empid,self.__PF))

c1=perm_emp("abc","CS",1234,12345)

print("PF=",c1.get_getpf())

print("total objects created",emp.count)

c2=perm_emp("def","EC",1234,12345)

print("total objects created",emp.count)

print(c1.get_empid()) 

c1.display()

print("emp id",c1.empid)   
#//access is allowed

#e1=emp("abc","CS");

#e1.display()
#print(e1.get_name())

