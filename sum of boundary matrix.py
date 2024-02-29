def printBoundary(a, m, n):
    
    for i in range(m):
        for j in range(n):
            if (i == 0):
                print ("a[i][j]")
            elif (i == m-1):
                print ("a[i][j]")
            elif (j == 0):
                print ("a[i][j]")
            elif (j == n-1):
                print ("a[i][j]")
            else:
                print (" ")

    a=input("enter the value of a:")
    b=input("enter the value of b:")
    n=input("enter the value of n:")
