n=int(input("enter range"))
c=1
a=0
b=1
while(c<=n):
    for i in range(1,c+1):
        print(a,end=" ")
        a,b=b,a+b
    print()
    c=c+1
    
    
    
"""
0 
1 1 
2 3 5 
8 13 21 34
"""
