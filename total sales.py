#Nick Rasa
#Calories Per Day

#Initialize
start = int(1)
stop = int(7)
cal = int(0)
total = int(0)
calNum = int(0)
totalCal = str("")
averageCal = int(0)

#process

for calNum in range (start, stop +1,):
    cal = int(input("Enter number of calories for day " + str(calNum) + ": "))
    total = total + cal
    totalCal = totalCal + "Calories " + str(calNum) + ":  " + str(calNum) + "\n"
averageCal = total / 7
print (totalCal)
print("\n", "Total Calories Consumed during the week: ", total, "\n")
print("Average calories consumed per day: ", averageCal,)



    
