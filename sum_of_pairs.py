A=[1,2,3,4,5,6]
B=[]
sum=int(input("enter sum value"))
for i in range(0,len(A)):
    for j in range(0,len(A)):
        if(A[i]+A[j]==sum):
            B=B+[(A[i],A[j])]
print(B)
