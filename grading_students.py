"" round off 73 to 75 and all"""

n=int(input())
A=[]
B=[40,45,50,55,60,65,70,75,80,85,90,95,100]
for i in range(n):
    a=int(input())
    A=A+[a]
for i in range(len(A)):
    for j in range(len(B)):
        if(B[j]-A[i]==2):
            A[i]=B[j]
        elif(B[j]-A[i]==1):
            A[i]=B[j]
print(A)
