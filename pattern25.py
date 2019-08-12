for row in range(8):
    for col in range(5):
        if((col==0 and row not in[0,6,7]) or (col==4 and row not in [0,6,7]) or (row==0 and col not in[0,4]) or(row==6 and col not in[0,4])or(row==7 and col==3)or(row==5 and col==1) ):
            print("*",end=" ")
        else:
            print(end="  ")
    print()


"""
  * * *   
*       * 
*       * 
*       * 
*       * 
* *     * 
  * * *   
      *   
"""
