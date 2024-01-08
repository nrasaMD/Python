#Nick Rasa
#Dice Roll Minor Program



#Initialize
import random
numRolls = int(0)
firstDiceRoll = [0,0,0,0,0,0,0]
secondDiceRoll = [0,0,0,0,0,0,0]
totalRoll = [0]*13

#input
numRolls = int(input("How many rolls to process? "))


#Process/output
for rollCtr in range(numRolls):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    tot = dice1+ dice2
    firstDiceRoll[dice1]+=1
    secondDiceRoll[dice2]+=1
    totalRoll[tot]+=1

print("Output for", numRolls, "rolls")
print(dice1, "+", dice2, "=", tot)
print("\nNumber of times first individual dice value was rolled:")
print("Roll Value   Times Rolled    %Rolled")
for numValues in range (1, 7):
    print("    ",numValues,"        ", firstDiceRoll[numValues],"       ",format(firstDiceRoll[numValues]/numRolls,"10.1%"))

print("\nNumber of times second individual dice value was rolled:")
print("Roll Value   Times Rolled    %Rolled")
for numValues in range (1, 7):
    print("    ",numValues,"        ", secondDiceRoll[numValues],"       ",format(secondDiceRoll[numValues]/numRolls,"10.1%"))

print("\nNumber of times each total dice value was rolled:")
print("Roll Value   Times Rolled    %Rolled")
for numValues in range (2, 13):
    print('{0: >5}'.format(numValues),"        ", totalRoll[numValues],"       ",format(totalRoll[numValues]/numRolls,"10.1%"))
