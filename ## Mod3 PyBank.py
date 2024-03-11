## Module 3 Challenge - Budget_Data

# Import the os module to allow us to create file paths across operating systems
import os

# Import module for reading CSV files
import csv

# Pathway to the csv. file
csvpath = os.path.join("/Users", "tashado", "Desktop", "budget_data.csv")

# Make a counter to count the number of months; total profit/loss; profit/loss change variables for current month change, sum of change, min and max change.
month_count = 0
total = 0
amount = 0
change = 0
total_change = 0
max_pf = 0
min_pf = 0

# Opening the csv. file
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)

    ## First row of data will be treated separately as "change" is only calculated for the other rows onward.
   
    # Read the first row of data
    first_month = next(csvreader)
    # Add to the month count
    month_count=month_count+1
    # Add to the total profit/loss amount
    total = total + int(first_month[1])
    # Reset previous month variable with the profit/loss amount
    prev_month=first_month[1]

    # Read each row of data after the first row
    for row in csvreader:
        
        # Add to month count 
        month_count = month_count + 1

        # Add to the total
        total = total + int(row[1])
        
        # calculate the change of profit/loss from the previous month
        change = int(row[1])-int(prev_month)
        
        # if the current change value is more than the previous saved max profit/loss value, then update the max profit/loss value to be the current change value (or vice versa)
        if change>max_pf:
            max_pf=change
            max_pf_month=(row[0])
        elif change<min_pf:
            min_pf=change
            min_pf_month=(row[0])

        # add the calculated change to the "total change" variable
        total_change=total_change+change

        # Reset previous month variable with the profit/loss amount
        prev_month=row[1]

# Calculate the average change
average_change=total_change/(month_count-1)

# Save the summary as a list
lines=["Financial Analysis", 
       "----------------------------", 
       str(f"Total Months: {month_count}"), 
       str(f"Total: ${total}"), 
       str(f"Average Change: ${round(average_change,2)}"), 
       str(f"Greatest Increase in Profits: {max_pf_month} ({max_pf})"), 
       str(f"Greatest Decrease in Profits: {min_pf_month} ({min_pf})")]

# Print the summary to the terminal
print(*lines,sep="\n")

# Export a txt file with the summary
with open("budget_data_summary.txt","w") as f:
    f.write("\n".join(lines))