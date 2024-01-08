#Nick Rasa
#Favorite Numbers

#initialization
num = int(0)
num = int(input("How many Numbers?"))


myNumbers = [""] * num

for numCtr in range (num):
    myNumbers[numCtr] = input("Enter Number: ")

for numCtr in range (num):
    print("Number",numCtr +1,":", myNumbers[numCtr])
m = myNumbers[0]
for i in myNumbers:
    if i<m:
        m = i
numbers = myNumbers
highest_num = 0
for ma in numbers:
    if ma > highest_num:
        highest_num = ma
print("Smallest Number: ",m)
print("Largest Number: ",ma)





