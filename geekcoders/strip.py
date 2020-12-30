name,char=input("enter name and char").split(",")
print(len(name.replace(" ","").strip()))
print(name.strip().lower().count(char.strip().lower()))