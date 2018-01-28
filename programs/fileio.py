fp1=open("input.txt","r")
fp2=open("output.txt","w")
for line in fp1:
    print("line=",line)
    fp2.write(line)
fp1.close()
fp2.close()