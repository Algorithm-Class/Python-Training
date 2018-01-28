import numpy as np
import sys
import re

# Matrix 1

if (sys.argv !=2) :
   print("Error in usage: python mat_add row=<value> col=<value>")
   exit

for i in sys.argv :
    mobj=re.match(r'col=(\d+)',i,re.I|re.M)
    if(mobj):
       m=int(mobj.group(1))
    mobj=re.match(r'row=(\d+)',i,re.I|re.M)
    if(mobj):
       n=int(mobj.group(1))


       
   
print("Matrix 1 Dimensions");
#m=int(sys.argv[1])
#n=int(sys.argv[2])

arr1=np.zeros((n,m))

print(arr1)

for i in range(m) :
    print("Enter %dth row"%(i))
    arr1[i]=[int(x) for x in input().split()]

print(arr1)

print("Matrix 2 Dimensions");
#m=int(input("enter number of rows"))
#n=int(input("enter number of Cols"))

arr2=np.zeros((n,m))

print(arr1)

for i in range(m) :
    print("Enter %dth row"%(i))
    arr2[i]=[int(x) for x in input().split()]

print(arr2)

print(arr1+arr2)