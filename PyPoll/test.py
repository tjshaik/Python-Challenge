import csv
import os
file = os.path.join ("Resources","election_data.csv")
output = "analysis/election_analysis.txt"
#toal voter count
total_votes = 0 

# candiate options and vote counters
candidate_options = []
candidate_votes = {}
Winner = ""
Wining_count = 0
print(file)
# read csv and convert to dictionary 
with open(file) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)
    print(header)
    for row in reader:
        # total vote count
        total_votes = total_votes + 1
        #print(total_votes)

        # The candidate name from each row
        candidate_name = row[2]
        if candidate_options not in candidate_options:
            # add to list
            candidate_options.append(candidate_name)
            # track candidate voter count
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name]= candidate_votes[candidate_name]+ 1
    print(candidate_votes)
