dict={"ganesh":'08-08-2001',"ravi":'20-06-2000',"sai kiran":'14-06-2001',"tarun":'21-07-1999',"satya":'28-05-2000'}
print(">>>welcome to birthdays dictionary.we know birthdays of :")
for name in dict:
    print(name)
print("who's birthday do want to know ?")
name= input()
if name in dict:
    print(name +'has birthday on' +dict[name])
else:
    print("we don't have " + name + "birthday")