# binary search

n,A=int(input("enter total no. of elements in array")),[]
for j in range(n):
    A+=[int(input())]
A=sorted(A)   #for binary search list should be in sorted order
f=int(input("enter no. you want to search"))
beg=0
end=len(A)-1
k=0
while(beg<=end):
    mid=(beg+end)/2
    mid=int(mid)
    if(A[(mid)]==f):
        print("found",A[mid],"at position",mid+1,sep=" ")
        k=1
        break
    elif(A[(mid)]>f):
        end=mid-1
    else:
        beg=mid+1
    
if(k==0):
    print("not found")
