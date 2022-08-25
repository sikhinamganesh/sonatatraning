def myfile():
    try:
        c = open("ganesh.txt","r")
        print(c.read())
    except(FileNotFoundErrorotfounderror):
        return("not exits")
emp=myfile()
print(emp)