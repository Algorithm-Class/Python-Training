import numpy as np

a=[1,2,3,4]

print(a)
print(a+a)

arr=np.array(a,int)

print(arr)

print(arr+arr)

print(arr.shape)
print(arr.size)
print(type(arr))

a=[1,2,3,4]
b=[4,5,6,7]

arr2=np.array([[1,2,3,4],[5,6,7,8]])

print(arr2)


print(arr2+arr2)

print(arr[0])
print(arr[-1])
print(arr[1:3])

#ACcess one dimensional

print(arr)

for i in arr:
   print(i)

#ACcess two dimensional

print(arr2)

for i in arr2:
   for j in i:
       print(j)

# Read from terminal
a=4
arr=np.zeros(4)
print(arr)

#for i in range(a):
arr= [int(x)  for x in input().split()]
print(arr)

n=2
m=2
for i in range(n):
   print("%dth row with %d elements"%(i,m))
   arr[i]= [int(x)  for x in input().split()]
print(arr)




