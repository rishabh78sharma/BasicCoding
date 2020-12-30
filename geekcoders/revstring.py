n=input("enter the name")
def rev():
    global n
    r=n.replace(" ","").lower()
    print(f"{n}")
    print(r)
    if r==r[::-1]:
        return True
    return False
print(rev())
       
        

