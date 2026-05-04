for i in range(1,6,2):
    for j in range(1,6):
        if j<=i+1:
            print(" ",end="")
        if j==i:
             print("*", end="")
    print("\n")