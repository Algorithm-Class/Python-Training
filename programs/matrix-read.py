import numpy as np
print ("Enter dimensions of array A:")
n=int(input())
m=int(input())
arr=np.zeros((n,m))
for i in range(n):
   print ("Enter %dth row values:"%(i))
   #for j in range(m):
   arr[i]=[int(x) for x in input().split()]
print ("Array A is :")
print (arr)
print ("Enter dimensions of array B:")
n=int(input())
m=int(input())
arr1=np.zeros((n,m))
print("Enter values")
for i in range(n):
   print ("Enter %dth row values:"%(i))
   #for j in range(m):
   arr1[i]=[int(x) for x in input().split()]
print ("Array B is :")
print (arr1)
print("Addition of two arrays is:")
print (arr+arr1)