"""Enter size of pattern10
*
***
*****
*******
*********"""


n=int(input("Enter size of pattern"))
for i in range(1,n+1,2):
    for j in range(1,i+1):
        print("*",end="")
    print()
