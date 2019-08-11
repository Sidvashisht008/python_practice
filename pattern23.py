for row in range(7):
    for col in range(7):
        if((row==0 and col not in [0,3,6])or(col==3 and row ==1)or((row==2 or row==3 or row==1) and col not in[1,2,3,4,5])or(row==4 and col not in[0,2,3,4,6])or(row==5 and col not in[1,0,3,6,5])or(row==6 and col==3)):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
             
"""
  * *   * *   
*     *     * 
*           * 
*           * 
  *       *   
    *   *     
      *   
"""
