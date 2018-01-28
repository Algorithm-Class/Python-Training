#linear Search
l=(1,2,3,4,5,3,4,2,4,2,5)

x=int( input("enter the element"))

i=0;

count=0;

n=len(l)

while(i<n) :
   if(x==l[i]) :
       print("Element is found");
       count=count+1
   i=i+1;

print("Element repeated number",count)


  




