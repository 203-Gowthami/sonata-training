pl1=input()
pl2=input
if(pl1==pl2):
    print("no result")
elif(pl1=="rock" and pl2=="scissors") or(pl2=="paper" and pl1=="scissors")or(pl1=="paper" and pl2=="rock"):
    print("pl1 wins")
else:
    print("pl2 wins")