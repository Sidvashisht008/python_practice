"""Enter size of pattern5
*
**
***
****
*****"""

n=int(input("Enter size of pattern"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print(end="\n")
