n=int(input())
for i in range(1,n):
    for a in range(1,n-i+1):
        print(" ",end="")
    for b in range(1,i+1):
        print("#",end=" ")
    print()
for i in range(n,-1,-1):
    for a in range(1,n-i+1):
        print(" ",end="")
    for b in range(1,i+1):
        print("#",end=" ")
    print()


"""
    # 
   # # 
  # # # 
 # # # # 
# # # # # 
 # # # # 
  # # # 
   # # 
    # 
"""
