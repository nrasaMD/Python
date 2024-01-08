

def main():
   menuNumber = float(0.0)
   print("converts cups to ounces")
   print("Enter the number next tot he selection,\n and press ENTER")
   print("\t0: QUIT")
   print("\t1: Convert cups to ounces")
   print("\t2: Convert ounces to cups")
   print("\t3: Conver both cups to ounces and ounces to cups")
   menuNumber = float(input("PLease enter a number between 0 and 3:"))



   if menuNumber < 0 or menuNumber > 3:
       menuNumber = float(input("You entered and invalid entry"))
   if menuNumber < 0 or menuNumber > 3:
       print("data input error", menuNumber, "is not valid")
   if menuNumber == 1 or menuNumber == 3:
       processOption1()
   if menuNumber == 2 or menuNumber == 3:

       processOption2()
def processOption1():
    cups = float(0.0)
    ounces = float(0.0)
    cups = float(input("enter how many cups you like to convert"))
    ounces = cups*8
    print(cups,"cups is equal to",ounces,"ounces")

def processOption2():
    cups = float(0.0)
    ounces = float(0.0)
    ounces = float(input("how many ounces would you like to convert"))
    cups = ounces/8
    print(ounces,"equal",cups,"cups")
main()
                      
