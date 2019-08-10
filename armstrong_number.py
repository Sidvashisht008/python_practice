#two different methods to find armstrong number

n=int(input("enter no."))
m=n
count,sum=0,0
while(n>0):
    count+=1
    n//=10
print(count)

while(m>0):
    a=m%10
    m//=10
    sum=sum+pow(a,count)
print(sum)


#-------------------------------------------------------------------


for i in range(0,1000):
    nsum=0
    abc=i
    while(abc>0):
        d=abc%10
        abc//=10
        nsum=nsum+pow(d,3)
    if(nsum==i):
        print(i)
