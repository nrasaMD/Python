#Nick Rasa
#Price Quote

#1.0 Initialize
COMPANY_NAME = str("Texas Overlay Designs")
customerName = str("")
RATE_ONE = float(7.20)
RATE_TWO = float(5.90)
squareFeet = float(0.0)

#2.0 Input

customerName = str(input("Enter Customer Name: "))
squareFeet = float(input("Enter the square footage for project area: "))


#3.0 Process
a = (squareFeet * RATE_ONE)
b = (squareFeet * RATE_TWO)

if squareFeet >= 2200:
    print()
    print("Thank You: ",customerName, "For choosing",COMPANY_NAME)
    print()
    print("Your Estimated Price is: ", format(b,"30,.2f"))


else:
    print()
    print("Thank You: ",customerName, "For choosing",COMPANY_NAME)
    print()
    print("Your Estimated Price is: ", format(a,"30,.2f"))

















