import threading
import time;
import queue


class thread1(threading.Thread) :
     
     def __init__(self,trdid,start1,end1,q):

         threading.Thread.__init__(self);
         data = threading.local()
         self.start1=start1
         self.trdid=trdid
         self.end1=end1
         self.q = q
         
     def run(self):
        self.add(self.start1,self.end1)
     def add (self,start,end):
         data = threading.local()
         i=start;
         sum=0;
         while(i<=end):
           sum=sum+i;
           i=i+1  
         
         lck.acquire()
         q.put(sum)
         lck.release()  
        # threading.Thread.join(10) 
           
         #  threading.Thread.join(self)
         print("trd %d sum=%d"%(self.trdid,sum))
         return data

q = queue.Queue(10)

t1=thread1(1,1,5,q);
t2=thread1(2,6,10,q);
lck=threading.Lock()

ticks1 = time.time()
t1.start()

t2.start()

t1.join(10) 

t2.join(10)

sum=0
while not q.empty():
    data = q.get()
    sum=sum+data
print("sum",sum)

ticks2 = time.time()

print("Run time",ticks2-ticks1) 
    








