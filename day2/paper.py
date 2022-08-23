p1=int(input('enter a number'))
p2=int(input('enetr a number'))
if(p1==p2):
    print('no result')
elif(p1=='poper' and p2=='rock') or(p1=='scissor' and p2=='paper') or (p1=='rock' and p2=='scissor'):
    print('p1,wins')
else:
    print('p2 wins')