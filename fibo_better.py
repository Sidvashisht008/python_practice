n=int(input("enter no. of terms"))
a,b,c=0,1,0
while(c<n):
    print(a,end=" ")
    a,b=b,a+b
    c=c+1
