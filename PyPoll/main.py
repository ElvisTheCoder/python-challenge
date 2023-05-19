import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_data.csv")

# Open the file.
with open(file_to_load, 'r') as election_data:

    # Read the file object.
    csvreader = csv.reader(election_data, delimiter=',')

    # Print the header row. 
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Declare variables
    percentages = []
    votes = []
    candidates = []
    total_votes = 0

    # Loop through each row in the CSV file and find the total number of votes and the candidates.
    for row in csvreader:
        total_votes += 1
        if (row[2] not in candidates):
            candidates.append(row[2])
            votes.append(1)
        # What is the purpose of line 41?

        else:
            votes[candidates.index(row[2])] += 1

# Calculate the percentages of votes for each candidate.
for i in range(len(candidates)):
    percentages.append(round(votes[i] / total_votes * 100, 3))

# Find the winner of the election.
winner = candidates[votes.index(max(votes))]

# Export the election results to a text file.
file_to_output = os.path.join("analysis", "election_analysis.txt")
with open(file_to_output, "w") as txt_file:
    # Write the Election Results into the file election_analysis.txt and put it in the analysis folder
    txt_file.write(f"Election Results\n")
    txt_file.write(f"-------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write(f"-------------------------\n")
    
    # Put the candidates, percentages, and votes into the file.
    for i in range(len(candidates)):
        txt_file.write(f"{candidates[i]}: {percentages[i]}% ({votes[i]})\n")
    
    txt_file.write(f"-------------------------\n")
    txt_file.write(f"Winner: {winner}\n")
    txt_file.write(f"-------------------------\n")
    




