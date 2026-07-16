name = input("Enter username: ")

if(len(name)>13):
    print("Usearname is too long.")
elif(name.find(" ")>-1):
    print("Username can't contain spaces.")
elif(name.isalpha()==False):
    print("Username does't contain digit.")
else:
    print("Username is ok")