import math
a=int(input("enter value of a"))
n=int(input("enter no. of terms"))
A=[(a**i)for i in range(1,n+1)]
B=[math.factorial(i) for i in range(1,n+1)]
C=[]
for i in range(0,len(A)):
    C+=[A[i]/B[i]]
print(sum(C))
