a,b=map(int,input().split())
if a<b:
    z=a
else:
    z=b
count=0
for i in range(1,z+1):
    if(a%i==b%i==0):
        count+=1
print(count)
