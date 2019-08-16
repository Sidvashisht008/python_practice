n=int(input("enter range"))
for i in range(1,n):
    sum=0
    for j in range(2,i+1):
        if(i%j==0):
            sum=sum+j
    if(sum==i):
        print(i,end=" ")
