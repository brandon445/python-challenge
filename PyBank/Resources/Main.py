import os
import csv

csvpath = "budget_data.csv"
txtpath = "financial_results.txt"

# Method 1: Plain Reading of CSV files
print(csvpath)

# Method 2: Improved Reading using CSV module
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    totalMonths = 0
    total = 0
    #averageChange = 0
    greatestIncreaseInProfits = 0
    greatestDecreaseInProfits = 0
    changeInMonths = 0
    previousMonth = 0
    totalMonthChanges = 0
    
    # Read each row of data after the header
    for row in csvreader:
        totalMonths = totalMonths + 1
        total = total + int(row[1])
        
        if totalMonths > 1:
            changeInMonths = int(row[1]) - previousMonth

        totalMonthChanges = totalMonthChanges + changeInMonths

        previousMonth = int(row[1])

        if changeInMonths > greatestIncreaseInProfits:
            greatestIncreaseInProfits = changeInMonths
            greatestIncreaseInMonths = row[0]

        if changeInMonths < greatestDecreaseInProfits:
            greatestDecreaseInProfits = changeInMonths
            greatestDecreaseInMonths = row[0]

    averageChange = totalMonthChanges / (totalMonths - 1)
    finalAverageChange = "{:.2f}".format(averageChange)
    
    print("Financial Analysis")
    print("--------------------------------------")
    print("Total Months: " + str(totalMonths))
    print("Total: $" + str(total))
    print("Average Change: $" + str(finalAverageChange))
    print("Greatest Increase In Profits: " + str(greatestIncreaseInMonths) + " " + "(" + "$" + str(greatestIncreaseInProfits) + ")")
    print("Greatest Decrease In Profits: " + str(greatestDecreaseInMonths) + " " + "(" + "$" + str(greatestDecreaseInProfits) + ")")

    #Export to text file
    f = open("financial_results.txt", "w+")
    f.write("Financial Analysis" + "\n")
    f.write("--------------------------------------\n")
    f.write("Total Months: " + str(totalMonths) + "\n")
    f.write("Total: $" + str(total) + "\n")
    f.write("Average Change: $" + str(finalAverageChange) + "\n")
    f.write("Greatest Increase In Profits: " + str(greatestIncreaseInMonths) + " " + "(" + "$" + str(greatestIncreaseInProfits) + ")" + "\n")
    f.write("Greatest Decrease In Profits: " + str(greatestDecreaseInMonths) + " " + "(" + "$" + str(greatestDecreaseInProfits) + ")" + "\n")