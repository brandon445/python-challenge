import os
import csv

csvpath = "election_data.csv"
txtpath = "election_results.txt"

# Method 1: Plain Reading of CSV files
print(csvpath)

# Method 2: Improved Reading using CSV module
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    totalVotesCast = 0

    khanVote = 0
    correyVote = 0
    liVote = 0
    tooleyVote = 0 


    for row in csvreader:
        totalVotesCast = totalVotesCast + 1

    #Calculate how many votes each recieved
        if row[2] == "Khan":
            khanVote = khanVote + 1
        if row[2] == "Correy":
            correyVote = correyVote + 1
        if row[2] == "Li":
            liVote = liVote + 1
        if row[2] == "O'Tooley":
            tooleyVote = tooleyVote + 1

        
    #Calculate percentages of each Candidate
        khanPercentage = khanVote / totalVotesCast
        
        
    #Correy Percentage
        correyPercentage = correyVote / totalVotesCast
        
       
    #Li Percentage
        liPercentage = liVote / totalVotesCast

        
    #O'Tooley Percentage
        tooleyPercentage = tooleyVote / totalVotesCast
        
       
    
        if khanPercentage > correyPercentage:
            winnerRoundA = khanPercentage
            winnerRoundAA = "Khan"
        else:
            winnerRoundA = correyPercentage
            winnerRoundAA = "Correy"
            
        if liPercentage > tooleyPercentage:
            winnerRoundB = liPercentage
            winnerRoundBB = "Li"
        else:
            winnerRoundB = tooleyPercentage
            winnerRoundBB = "O'Tooley"

        if winnerRoundA > winnerRoundB:
            winner = winnerRoundAA
        else:
            winner = winnerRoundBB

khanFinalPercentage = "{:.3%}".format(khanPercentage)

correyFinalPercentage = "{:.3%}".format(correyPercentage)

liFinalPercentage = "{:.3%}".format(liPercentage)

tooleyFinalPercentage = "{:.3%}".format(tooleyPercentage)

print("Election Results")
print("------------------------------------------")
print("Total Votes: " + str(totalVotesCast))
print("------------------------------------------")
print("Khan: " + str(khanFinalPercentage) + " " + "(" + str(khanVote) + ")")
print("Correy: " + str(correyFinalPercentage) + " " + "(" + str(correyVote) + ")")
print("Li: " + str(liFinalPercentage) + " " + "(" + str(liVote) + ")")
print("O'Tooley: " + str(tooleyFinalPercentage) + " " + "(" + str(tooleyVote) + ")")
print("------------------------------------------")
print("Winner: " + str(winner))
print("------------------------------------------")


#Export to text file
f = open("election_results.txt", "w+")

f.write("Election Results" + "\n")
f.write("------------------------------------------ \n")
f.write("Total Votes: " + str(totalVotesCast) + "\n")
f.write("------------------------------------------ \n")
f.write("Khan: " + str(khanFinalPercentage) + " " + "(" + str(khanVote) + ")" + "\n")
f.write("Correy: " + str(correyFinalPercentage) + " " + "(" + str(correyVote) + ")" + "\n")
f.write("Li: " + str(liFinalPercentage) + " " + "(" + str(liVote) + ")" + "\n")
f.write("O'Tooley: " + str(tooleyFinalPercentage) + " " + "(" + str(tooleyVote) + ")" + "\n")
f.write("------------------------------------------ \n")
f.write("Winner: " + str(winner) + "\n")
f.write("------------------------------------------ \n")


