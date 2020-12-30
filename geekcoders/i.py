global c

def nota(l):
    rev=[]
    for i in range(len(string)):
        p=string[::-1]
    print(p)
    c=0
    for j in p:
        
        c+=1
        print(c)
        rev.append(j[::-1])
        
    return rev
        
string=["sun","mun","dun"]
print(nota(string))        