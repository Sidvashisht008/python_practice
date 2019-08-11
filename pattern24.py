for row in range(7):
    for col in range(7):
        if((row==0 and col not in [0,3,6])or(row in[1,2,3])or((row==4 and col not in[0,6])or(row==5 and col not in(0,1,5,6)or(row==6 and col not in[0,2,1,4,6,5])))):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
             
"""
  * *   * *   
* * * * * * * 
* * * * * * * 
* * * * * * * 
  * * * * *   
    * * *     
      * 
"""
