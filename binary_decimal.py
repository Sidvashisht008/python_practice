a=input("enter binary number")
sum=0
d=len(a)-1
for i in a:
    sum=sum+int(i)*2**d
    d-=1
print(sum)
