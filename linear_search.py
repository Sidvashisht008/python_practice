n,A=int(input("enter no. of elements in list")),[]
for j in range(n):
    A=A+[int(input())]
a=int(input("enter no. to search"))
k=0
for i in range(0,len(A)):
    if(A[i]==a):
        print("found",A[i],"at position",i,sep=" ")
        k=1
if(k==0):
    print("not found")
