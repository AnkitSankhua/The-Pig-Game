import random

# The DICE for our game......
def dice_roll():
    MINvalue = 1
    MAXvalue = 6
    dice_roll = random.randint(MINvalue , MAXvalue)

    return dice_roll

# Number of Players
while True:
    players = input("Enter The Number Of Players (2-6) : \n")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 6:
            break
        else:
            print(("Number Of Players Must be Between 2 and 6"))
    else:
        print(" Invalid number Of Players !!! \n            Try Again !! ")

print("Number Of Players Confirmed : "+str(players))

# The Total Score For Our Game.
while True:
    maxScore = input("The Max Score For This Game Would Be... : ")
    if maxScore.isdigit():
        maxScore = int(maxScore)
        if 5 <= maxScore <= 150:
            break
        else:
            print("The Minimum Score Should be [5] while the"
                  " Maximum Score Should be [150] !!!"
                  "\nPlease Enter The Score In Between These Numbers !!!")
    else:
        print("Invalid Score value ! \n                     Try Again !")

# The Main Logic Behind Our Game.
playerScore = [0 for x in range(players)]

print("These Are The Current Scores for All the "
      "Players :\n "+str(playerScore))

while max(playerScore) < maxScore:
    for playerNo in range(players):
        print("\nPlayer ", playerNo+1 ,"'s Turn has just Started !")
        print("\nPlease Continue Player Number " , playerNo+1)
        print("Your Total Score Is : ", playerScore[playerNo],"\n")
        currScore = 0

        while True:
            roll = input("Would You Like to ROLL ??\n"
                         "Press < Y / y > to Continue.\n"
                         "Press ANY KEY to End. \n")
            if roll.lower() !=  "y":
                break

            value = dice_roll()
            if value == 1:
                print("You rolled a 1 !! Turn Ended !\n")
                currScore = 0
                break
            else:
                currScore += value
                print("You Rolled A  ",value,"\n" )

            print("Your Score Is : ", currScore, "\n")

        playerScore[playerNo] += currScore
        print("Your Total Score is : ", playerScore[playerNo])

# Winner Declaration !
maxScore = max(playerScore)
winner = playerScore.index(maxScore)
print("\nPlayer NUmber", winner +1,
      "is the Winner With a score of : ",maxScore)

# END
print("******** [ GAME END ] ********")