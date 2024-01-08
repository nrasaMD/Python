#Nick Rasa
#CupCake Program

#Initialize
pans = int(0)
stkButter = int(1)
tspFlavoring = int(1)
cupCreamCheese = int(1)
powderedSugar = int(4)

#Input
pans = int(input("Please enter the number of pans of cupcakes you need to frost: "))

#Process
stkButter = int(stkButter * pans)
tspFlavoring = int(tspFlavoring * pans)
cupCreamCheese = int(cupCreamCheese * pans)
powderedSugar = int(powderedSugar * pans)


#Output
print ("CUPCAKE FROSTING RECIPE CONVERTER")
print (format("Number of pans to frost:","24"), format(pans,"8,d"))
print (format("Sticks of butter:","24"), format(stkButter,"8,d"))
print (format("Cups of cream cheese:","24"), format(cupCreamCheese,"8,d"))
print (format("Teaspoons of flavoring:","24"), format(tspFlavoring,"8,d"))
print (format("Cups of powdered sugar:","24"), format(powderedSugar,"8,d"))
                                                     





