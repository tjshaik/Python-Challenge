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
Winning_count = 0

# read csv and convert to dictionary 
with open(file) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)

    for row in reader:
        # total vote count
        total_votes = total_votes + 1
        #print(total_votes)

        # The candidate name from each row
        candidate_name = row[2]
        #print (candidate_name)
        # IF diffrent candidate 
        if candidate_name not in candidate_options:
            # add to list
            candidate_options.append(candidate_name)
            # track candidate voter count
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name]= candidate_votes[candidate_name]+ 1
with open(output, 'w') as txt_file:
    #Print
    election_results = (
        f"\n\nElection Results\n"
        f"---------------------\n"
        f"Total Votes: {total_votes}\n"
    )
    print(election_results)
    # save text file 
    txt_file.write(election_results)

    #Find winning vote count and candidate
    for candidate in candidate_votes:

        # get vote count and percentage
        votes = candidate_votes.get(candidate)
        votes_percentage = float(votes)/ float(total_votes) * 100
        # Determine winning count and cand 
        if (votes > Winning_count):
            Winning_count = votes
            Winner = candidate

        #print each candiate's infor
        voter_output = f" {candidate}: {votes_percentage:.2f}% {votes})\n"
        print(voter_output)

    #print winning candidate
    Winner_summary = (
        f"--------------------\n"
        f"Winner: {Winner}\n"
        f"--------------------\n"
    )
    print(Winner_summary)
    txt_file.write(Winner_summary)



