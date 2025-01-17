from random import random


overallWinCount = 0
maxSimulations = 1000
targetBet = 10000
percentageBet = 0.0001

# 0.1, wins = 372
# 0.2, wins = 241 
# 0.3, wins = 204
# 0.37, wins = 298
# 0.4, wins = 244
# 0.5, wins = 229
# 0.6, wins = 198
# 0.7, wins = 207
# 0.8, wins = 204
# 0.9, wins = 185
# 1.0, wins = 160

#0.01, wins = 416, 446, 462, 466, 467
#0.05, wins = 391

# essentially betting 1 chip at a time
#0.001, wins = 467, 473, 479, 478, 506
#0.0001, wins = 475, 483, 489, 481, 477
#this seems to be the best strategy

winChance = 0.4

for i in range (1, maxSimulations):
    chips = 2000
    currentBet = int(percentageBet * chips)
    totalBet = 0
    counter = 0

    while chips > 1 and totalBet<=targetBet:
        # print (f"round {counter}")
        # print(f"chips remaining {chips}")
        # print(f"total Bet {totalBet}")
        # print("\n")
        counter+=1
        totalBet+=currentBet
        if random()>=winChance:
            chips-=currentBet

        else:
            chips+=currentBet

        currentBet = int(percentageBet * chips)
        if currentBet < 1:
            currentBet = 1

    # print (f"round {counter}")
    # print(f"chips remaining {chips}\n")
    # print(f"total Bet {totalBet}")
    # print(f"wins = {winCount}, losses = {loseCount}")
    # print("\n")

    if totalBet>=targetBet:
        # print ("you won")
        overallWinCount += 1

print(f"you won:{overallWinCount}/{maxSimulations}")