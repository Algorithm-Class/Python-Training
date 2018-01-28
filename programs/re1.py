import re

s="suresh      88878877678  java  suresh@gmail.com"
  

matchObj=re.match(r'\w+\s+j(\w+)\s+(\d+)\s+',s,re.I|re.M);

if(matchObj) :

   print("found",matchObj.group())
   print("found",matchObj.group(1))
   print("found",matchObj.group(2))
else:
   print("not found")
   

