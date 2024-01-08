import random
MAX_SPACES = int(20)

def main():
    player1Nm = str("")
    player2Nm = str("")
    player1Space = int(0)
    oldSpace1 = int(0)
    player2Space = int(0)
    oldSpace2 = int(0)
    roundNum = int(0)
    player1Roll = int(0)
    player2Roll = int(0)

    player1Nm = getPlayerName()
    player2Nm = getPlayerName()

    print("Welcome to the game,",player1Nm,"and",player2Nm)
    while player1Space < 20 and player2Space < 20:
        roundNum += 1
        print("\nRound:",roundNum)
        playerRoll = getPlayerRoll()
        oldspace1 = player1Space
        player1Space += playerRoll
        printResult(player1Nm, oldspace1, player1Space, player1Roll)

        player2Roll = getPlayerRoll()
        oldspace2 = player2Space
        player2Space += player2Roll
        printResult(player2Nm, oldspace2, player2Space, player2Roll)
    printFinalResult(player1Nm, player1Space, player2Nm, player2Space)

def getPlayerName():
    name = str(input("Enter PLayer name: "))
    return name

def getPlayerRoll():
    roll = int(random.randint(1, 6))
    return roll


def printResult(playerName,oldSpace, newSpace, roll):
    print(playerName,"is on",oldSpace,"and rolls",roll)
    print(playerName,"moves",roll,"spaces and is now on space", newSpace)
def printFinalResult(player1, player1Space, player2, player2Space):
    print("\nEnd of Game!")
    if player1Space > player2Space:
        print(player1,"is on space", player1Space, "and wins the game!")
        print(player2, "is on space", player2Space)
    elif player1Space < player2Space:
        print(player1,"is on space", player1Space)
        print(player2, "is on space", player1Space,"and wins the game!")
    else:
        print(player1,"and", player2, "are tied!")
        
main()
