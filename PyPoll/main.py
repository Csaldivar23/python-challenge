# adding modules
import os
import csv

# setting vote counters
total_votes = 0
candidate_votes = {}

# creating path to election data csv file
csvpath = os.path.join("..", "Resources", "election_data.csv")

with open(csvpath) as csvfile:

    # reading csv file and setting header
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    print(f"CSV Header: {csv_header}")

    # counting up the total votes and candidate votes
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 0
        candidate_votes[candidate] += 1

# calculating the percentage of votes
candidate_percentages = {}
for candidate, votes in candidate_votes.items():
    candidate_percentages[candidate] = (votes / total_votes) * 100

# calculate winner
winner = max(candidate_votes, key=candidate_votes.get)

# print election results
print("Election Results")
print(f"Total Votes: {total_votes}")
for candidate in candidate_votes:
    print(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({candidate_votes[candidate]})")
print(f"Winner: {winner}")

# export the results to a text file
output_path = os.path.join("..", "Analysis", "Election_Results.txt")
with open(output_path, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    for candidate in candidate_votes:
        txtfile.write(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({candidate_votes[candidate]})\n")
    txtfile.write(f"Winner: {winner}\n")