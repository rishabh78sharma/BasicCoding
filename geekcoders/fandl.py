val=int(input('enter the no. of value that you want to put into the list'))
l=[]
for i in range(val):
    a=input('enter the value')
    l.append(a)
print(l)
for i in range(val):
    if(i==0 or i==val-1):
        print(l[i])
    