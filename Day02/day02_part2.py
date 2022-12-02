# A,X => Rock(1)
# B,Y => Paper(2)
# C,Z => Scissors(3)
strategy = open("input","r").read().strip().split('\n')

#changed plays acording to the new strategy
#X => Loose(0)  Y => Draw(3)  Z => Win(6)
plays = {
    "A X" : 3,
    "A Y" : 4,
    "A Z" : 8,
    "B X" : 1,
    "B Y" : 5,
    "B Z" : 9,
    "C X" : 2,
    "C Y" : 6,
    "C Z" : 7,
}

score = 0
for i in strategy:
    score+=plays[i]

print("Score obtained following the strategy:",score)