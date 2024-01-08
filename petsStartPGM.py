#step 1: initialize/input 
numPets = int(0)

numPets = int(input("How many Pets? "))

petName = [""] * numPets

for petCtr in range(numPets):
    petName[petCtr] = input("Enter pet name: ")


#Step 3 output

for petCtr in range(numPets):
    print("Pet",petCtr + 1, petName[petCtr])

print("PETS BACKWARDS")
for petCtr in range(numPets- 1, -1,  -1):
    print("Pet",petCtr, petName[petCtr])
