import os
import csv

# Initialize the file path of the csv file
csvpath = os.path.join('Resources', 'election_data.csv')
textfile = os.path.join('Analysis', 'election_analysis.txt')

total_votes=0
candidate_name = []
candidate_options = []
candidate_votes = {}

# Open the file & initialize it to csvreader variable
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)  # Skip the header row

    # Loop through the rows in the CSV file
    for row in csvreader:
        # Count the total votes
        total_votes += 1
        #Candidate votes in the third column
        candidate_name = row[2]
        #Add unique candidate names to a list and 
        #create a dictionary to count the number of votes per candidate
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

# Print the results
analysis = ("Election Results\n"
    "------------------------------\n"
    f"Total Votes: {total_votes}\n"
    "------------------------------\n"
    f"Charles Casper Stockham: {round(float(((candidate_votes['Charles Casper Stockham'])/total_votes)*100), 3)}%, {candidate_votes['Charles Casper Stockham']}\n"
    f"Diana DeGette: {round(float(((candidate_votes['Diana DeGette'])/total_votes)*100), 3)}%, {candidate_votes['Diana DeGette']}\n"
    f"Raymon Anthony Doane: {round(float(((candidate_votes['Raymon Anthony Doane'])/total_votes)*100), 3)}%, {candidate_votes['Raymon Anthony Doane']}\n"
    "------------------------------\n"
    f"Winner: {max(zip(candidate_votes.values(), candidate_votes.keys()))[1]}\n"
    "------------------------------"
    )


print(analysis)

# Write the results to the txt file
with open (textfile, "w") as text:
    text.write(analysis)
