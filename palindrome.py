a=int(input("enter number"))
n=a
sum=0
while(n>0):
    c=n%10
    sum=sum*10+c
    n//=10
if(sum==a):
    print("palindrome")
else:
    print("not palindrome")
