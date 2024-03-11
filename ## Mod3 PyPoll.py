## Mod3 PyPoll

# Import the os module to allow us to create file paths across operating systems
import os

# Import module for reading CSV files
import csv

# Get csv. file path
csvpath = os.path.join("/Users", "tashado", "Desktop", "election_data.csv")

# Set initial values for total votes and candidate votes
votes_total=0
Charles=0
Diana=0
Raymon=0

# Open the csv. file
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)

    # Read each row of data after the first row
    for row in csvreader:

        # Add to the total number of votes counter
        votes_total=votes_total+1

        # if function to count how many votes each candidate has
        if row[2]=="Charles Casper Stockham":
            Charles=Charles+1
        elif row[2]=="Diana DeGette":
            Diana=Diana+1
        elif row[2]=="Raymon Anthony Doane":
            Raymon=Raymon+1

# Calculate candidate votes percentages
C_percent=(Charles/votes_total)*100
D_percent=(Diana/votes_total)*100
R_percent=(Raymon/votes_total)*100

# Find the highest candidate percentage
Win_high=max(C_percent, D_percent, R_percent)

# Defining the winner variable based on the previous max() function
if Win_high==C_percent:
    win=str(f"Charles Casper Stockham")
elif Win_high==D_percent:
    win=str(f"Diana DeGette")
elif Win_high==R_percent:
    win=str(f"Raymon Anthony Doane")

# Make a list with the information
lines=["Election Results",
       "----------------------------", 
       str(f"Total Votes: {votes_total}"), 
        "----------------------------", 
        str(f"Charles Casper Stockham: {round(C_percent,3)}% ({Charles})"),
        str(f"Diana DeGette: {round(C_percent,3)}% ({Charles})"),
        str(f"Raymon Anthony Doane: {round(R_percent,3)}% ({Raymon})"),
        "----------------------------", 
        str(f"Winner: {win}"),
        "----------------------------"
        ]

# Print the summary to the terminal
print(*lines,sep="\n")

# Export a txt file with the summary
with open("election_data_summary.txt","w") as f:
    f.write("\n".join(lines))