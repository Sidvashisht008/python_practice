a=int(input())
A=input()
valley=0
s=0
for i in A:
    if i=="D":
        s=s+1
    elif i=="U":
        s=s-1
    if(s==0 and i=="U"):
        valley+=1
print(valley)     
