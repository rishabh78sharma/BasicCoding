n=list(range(1,11))
def squarelist(l):
    global n
    for i in l:
        n.append(i**2)
    return n
print(squarelist(n))
print(n)    