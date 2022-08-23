pl1=input()
pl2=input()
def game(pl1,pl2):
    if (pl1 == pl2):
        return('no result')
    elif (pl1 == 'rock' and pl2 == 'scissors') or (pl2 == 'paper' and pl1 == 'scissors') or (
            pl1 == 'paper' and pl2 == 'rock'):
        return('pl1 wins')
    else:
        return('pl2 wins')
x=game('paper','rock')
print(x)

