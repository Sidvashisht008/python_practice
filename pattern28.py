num=int(input("enter the no. of rows :"))
A=[[0 for x in range(num)]for y in range (num)]
n=1
low=0
high=num-1
count=int((num+1)/2)
for i in range(count):
    for j in range(low,high+1):
        A[i][j]=n
        n+=1
    for j in range(low+1,high+1):
        A[j][high]=n
        n+=1
    for j in range(high-1,low-1,-1):
        A[high][j]=n
        n+=1
    for j in range(high-1,low,-1):
        A[j][low]=n
        n+=1
    low=low+1
    high=high-1
for i in range(num):
    for j in range(num):
        print(A[i][j],end="\t")
    print()

"""
enter the no. of rows :5
 1	 2	 3	 4	5	
16	17	18	19	6	
15	24	25	20	7	
14	23	22	21	8	
13	12	11	10	9
"""
