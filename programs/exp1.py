a=int(input("enter number"))
b=int(input("enter number"))
try:
   
   c=a/b;
   print("res=",c)
except TypeError:
   print("TypeError ....")
except ZeroDivisionError:
   print("ZeroDivisionError")
except ValueError:
   print("ValueError")
else: 
    print("no exception")
finally :
   print("I am here")


print("Hello")


