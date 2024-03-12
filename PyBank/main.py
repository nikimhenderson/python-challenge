import os
import csv

# Initialize the file path of the csv file
csvpath = os.path.join('Resources', 'budget_data.csv')
textfile = os.path.join('Analysis', 'budget_data.txt')
# Variables
total_months = 0
net_profit = 0
changes = []
profits = []
greatest_increase = ["", 0]
greatest_decrease = ["", float('inf')]  # Use float('inf') for a high initial value

# Open the file & initialize it to csvreader variable
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)  # Skip the header row

    # Loop through the rows in the CSV file
    for row in csvreader:
        # Count the total months
        total_months += 1

        # Sum the net profit
        net_profit += int(row[1])
# Append the profit to the profits list for calculating changes later
        profits.append(int(row[1]))

# Calculate changes in profits/losses and the average of those changes
for i in range(len(profits) - 1):
    change = profits[i + 1] - profits[i]
    changes.append(change)

 # Check for greatest increase and decrease in profits
    if change > greatest_increase[1]:
        greatest_increase[0] = i + 1  # Store the month index
        greatest_increase[1] = change

    if change < greatest_decrease[1]:
        greatest_decrease[0] = i + 1  # Store the month index
        greatest_decrease[1] = change

average_change = sum(changes) / len(changes)

# Print the results
analysis = (f"Total Months: {total_months}\n"
            f"Total: ${net_profit}\n"
            f"Average Change: ${round(average_change, 2)}\n"
            f"Greatest Increase in Profits: {greatest_increase}\n"
            f"Greatest Decrease in Profits: {greatest_decrease}")


print(analysis)

# Write the results to the txt file
with open (textfile, "w") as text:
    text.write(analysis)
