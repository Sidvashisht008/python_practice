for row in range(7):
    for col in range(7):
        if(col==0 or col==6)or((col==row) and (col in [1,2,3,4,5] and row in [1,2,3,4,5] )):
            print("*",end="")
        else:
            print(end=" ")
    print()
    
"""
*     *
**    *
* *   *
*  *  *
*   * *
*    **
*     *
"""
