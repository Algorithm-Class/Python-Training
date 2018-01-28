import re

s="suresh  java  888887678  suresh@gmail.com"


matchobj=re.match(r'\w+\s+\j+(\w)+\s+(\d+)\s+(\w+@.*)',s,re.I|re.M);

if(matchobj):

  print("found",matchobj.group())
  print("found",matchobj.group(1))
  print("found",matchobj.group(2)) 
  print("found",matchobj.group(3))
  
else:
  print("not found") 