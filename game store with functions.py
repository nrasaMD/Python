#Nick
#game store program

#initialization
# normally the following variables would be input
TAX_RATE = .085
def main():
    # The following section should be input statements, but we hard-coded the values for efficient testing
    # Once testing is complete, it should be replaced with actual input statements
#Initialization/input
    boardGamesNumSales = int(25)
    boardGamesDollarAmtSale = float(1250.00)


    computerGamesNumSales = int(100)
    computerGamesDollarAmtSale = float(10000.00)


    rpGamesNumSales = int(50)
    rpGamesDollarAmtSale = float(3750.00)

#process: calculate the total number of sales and the total dollar amount received
    totNumSales = boardGamesNumSales + computerGamesNumSales + rpGamesNumSales
    totDollarAmtSale = boardGamesDollarAmtSale + computerGamesDollarAmtSale + rpGamesDollarAmtSale

#output: call function to print all output
    printGameInfo (boardGamesNumSales, boardGamesDollarAmtSale,  "Board Games")
    printGameInfo (computerGamesNumSales, computerGamesDollarAmtSale,  "Computer Games")
    printGameInfo (rpGamesNumSales, rpGamesDollarAmtSale,  "Role Playing Games")
    printGameInfo (totNumSales , totDollarAmtSale,  "Grand Total")

def printGameInfo (numGamesSold, totalAmtReceived, gameType):
    print()
    print(gameType)
    print(format("   Sales:","20"),format (numGamesSold,"10,d"))
    print(format("   Sales Amt:  ","20"),format (totalAmtReceived,"10,.2f"))
    print(format("   Sales Tax:  ","20"),format (getSalesTax(totalAmtReceived),"10,.2f"))
    avgSale = getAvgGameSale(numGamesSold,totalAmtReceived)
    print(format("   Avg Sales:  ","20"), format (avgSale,"10,.2f"))


def getAvgGameSale (numGamesSold, totalAmtReceived ):
    avgSale = float(0.0)
    avgSale = totalAmtReceived/numGamesSold
    return avgSale

def getSalesTax(dollarAmt ):
    salesTax = float(0.0)
    salesTax = dollarAmt * TAX_RATE
    return (salesTax)


main()
