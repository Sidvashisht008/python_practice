A=[1,212,32123,4321234,543212345,65432123456,7654321234567,876543212345678,98765432123456789]
for i in A:
    print(str(i).center(17))

"""
        1         
       212        
      32123       
     4321234      
    543212345     
   65432123456    
  7654321234567   
 876543212345678  
98765432123456789 
"""

n=int(input("enter series no."))
a=n-1
for i in range(1,n+1):
    print(" "*a,end="")
    for j in range(i,0,-1):
        print(j,end="")
    for j in range(2,i+1):
        print(j,end="")
    print()
    a-=1

"""
        1         
       212        
      32123       
     4321234      
    543212345     
   65432123456    
  7654321234567   
 876543212345678  
98765432123456789 
"""



A=[1,212,32123,4321234,543212345,65432123456,7654321234567,876543212345678,98765432123456789]
for i in A:
    print(str(i).ljust(17))
"""
1                
212              
32123            
4321234          
543212345        
65432123456      
7654321234567    
876543212345678  
98765432123456789
"""
A=[1,212,32123,4321234,543212345,65432123456,7654321234567,876543212345678,98765432123456789]
for i in A:
    print(str(i).rjust(17))
"""
                1
              212
            32123
          4321234
        543212345
      65432123456
    7654321234567
  876543212345678
98765432123456789
"""
