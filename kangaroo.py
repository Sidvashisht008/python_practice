x1,v1,x2,v2=list(map(int,input().split()))
flag=0
for i in range(1,10001):
        if(x1==x2):
            print("YES")
            flag=1
            break
        x1+=v1
        x2+=v2
if(flag==0):
    print("NO")
