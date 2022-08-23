p1=input("enter p1 turn")
p2=input("enter p2 turn")
def rps_game(p1,p2):
    if (p1==p2):
        return "enter the game"
    elif (p1!=p2):
        return "i am exting game"
    elif(p1=="rock" or  p2=="scissor") and  (p1=="paper" or p2=="rock") and (p1=="scissor" and p2=="paper"):
        return "rock wins"
    else:
        return "scissor wins"
x= rps_game("rock","paper")
print(x)