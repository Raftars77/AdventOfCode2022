# A,X => Rock(1)
# B,Y => Paper(2)
# C,Z => Scissors(3)
strategy = open("input","r").read().strip().split('\n')

plays = {
    "A X" : 4,
    "A Y" : 8,
    "A Z" : 3,
    "B X" : 1,
    "B Y" : 5,
    "B Z" : 9,
    "C X" : 7,
    "C Y" : 2,
    "C Z" : 6,
}

score = 0
for i in strategy:
    score+=plays[i]

print("Score obtained following the strategy:",score)
