for i in range (7,1,-1):
    for space in range(0,7-i):
       print("  ",end="")
    for j in range(i,2*i-1):
         print("* ",end="")
    for j in range(1,i-1):   
         print("* ",end="")
    print()
