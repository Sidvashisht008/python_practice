n=int(input())
A=list(map(int,input().split()))
m=sum(A)
s=max(A)
for i in range(1,max(A)+1):
    if(n*i>sum(A)):
        a=i
        break
print(a)
