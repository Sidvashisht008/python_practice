def anagram(a,b):
    l=[0]*26
    for i in a:
        l[ord(i)-ord('a')]+=1
    for i in b:
        l[ord(i)-ord('a')]-=1
    print(sum(map(abs,l)))
n=int(input())
for i in range(1,n+1):
    a=input()
    b=input()
    anagram(a,b)
