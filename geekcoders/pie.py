row=int(input("enter tn number"))
for i in range(0,row):
    for j in range(0,row-i):
        print("",end=" ")
    for k in range(0,i):
        print("*",end="")
        
    print()        