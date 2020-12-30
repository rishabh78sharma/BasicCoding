a=int(input("enter first no."))
b =int(input("enter second no."))
c=0
for i in range(a,b+1):
    for j in range(2,i):
        if (i%j==0):
            break
    else:
        print(i)        