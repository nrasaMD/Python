#Drink Cost program
#Nick Rasa

#0. Initialization
DRINK_COST = float(8.10)
numDrinksPurchased = int(0)
totalCostOfDrinks = float(0.0)

#1. Input
numDrinksPurchased = int(input("Enter Number of Drinks Purchased This Week: "))

#2. Process
totalCostOfDrinks = DRINK_COST * numDrinksPurchased

#3. Output
print ("Weekly Soft Drink Cost")
print ("Drink Price:",DRINK_COST)
print ("Number of Drinks Purchased:",numDrinksPurchased)
print ("Total Weekly Cost:",totalCostOfDrinks)
