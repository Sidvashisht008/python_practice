n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
pairs=0
for i in a:
    if i not in b:
        b=b+[i]
for i in b:
    c=c+[a.count(i)]
for i in c:
    pairs+=i//2
print(pairs)
