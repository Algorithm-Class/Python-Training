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
         print("trd %d sum=%d"%(self.trdid,sum))
         return data



q = queue.Queue(10)
lck=threading.Lock()
max_n=int(input("Enter range"))

trds=int(input("Enter No of threads"))

step1=int(max_n/trds);

start1=1;

end1=step1;

print("step",step1)

i=1;

l=[]; 
# l=[t1,t2,t3...]
ticks1 = time.time()
while(i<=trds):
    print("Thread %d range %d - %d "%(i,start1,end1))
    t1=thread1(i,start1,end1,q);
    t1.start()
    l.append(t1)

    start1=start1+step1
    end1=end1+step1
    i=i+1
n=len(l)
i=0;

while (i<n) :
   print("I amhere")
   t=l[i]
   t.join(10)
   i=i+1


lck=threading.Lock()

sum=0
while not q.empty():
    data = q.get()
    sum=sum+data
print("sum",sum)

ticks2 = time.time()

print("Run time",ticks2-ticks1) 
    








