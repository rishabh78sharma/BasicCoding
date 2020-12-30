global t
n=input("enter the number till the loop is work ")
t=int(n)
user=list(range(1,t))
def squalist(l):
    square=[]
    for i in l:
      user =square.append(i**2)
    return square
print(user)   
print(squalist(user))