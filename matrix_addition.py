r=int(input("Enter rows"))
c=int(input("Enter cols"))
A=[[i for i in range(c)]for j in range(r)]
for i in range(r):
    print(i,"row",sep=" ")
    for j in range(c):
        A[i][j]=int(input())
B=[[i for i in range(c)]for j in range(r)]
for i in range(r):
    print(i,"row",sep=" ")
    for j in range(c):
        B[i][j]=int(input())
for i in range(r):
    for j in range(c):
        print(A[i][j]+B[i][j],end=" ")
    print()
