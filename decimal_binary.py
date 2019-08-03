a=int(input("enter no.to convert to binary"))
c=''
while a>=1:
    r=a%2
    a=a//2
    c=str(r)+c
print(c)
