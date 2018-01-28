import threading
import time;


class thread1(threading.Thread) :
     
     def __init__(self,trdid,start,end):
         threading.Thread.__init__(self)
         self.tread_id=trdid;
         self.start=start
         self.end=end
     def run(self):
         add(self.start,self.end)



def add (start,end):

   i=self.start;
   sum=0;
   while(i<=self.end):
            sum=sum+i;
            i=i+1         
        # lck.release()  
        # threading.Thread.join(10) 
            print("sum=",sum)
       # return sum

t1=thread1(1,1,50);
#t2=thread1(2,51,100);
#lck=threading.Lock()

t1.start()
#t2.start()

t1.join(10) 

#t2.join(10)

#print("sum by trd 1", s1);
#print("sum by trd 2", s2);

#print("sum=",s1+s2)







