# Importing the modules
import os
import csv
# lists 
candidate_counter1 = []
candidate_counter2 = []
#open file
csvpath = os.path.join("election_data.csv")
with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
# next row 
    next(csvreader)
# move candidates in their own list
    for row in csvreader:
        candidate_counter1.append(row[2])
number_votes = len(candidate_counter1)
for row in candidate_counter1:
# names of the candidates into the list
    if row not in candidate_counter2:
        candidate_counter2.append(row)
# count up the votes for each person
Khan_votes = candidate_counter1.count(candidate_counter2[0])
Correy_votes = candidate_counter1.count(candidate_counter2[1])
Li_votes = candidate_counter1.count(candidate_counter2[2])
Otooley_votes = candidate_counter1.count(candidate_counter2[3])
# the percentage of votes 
percent_Khan = format((100 * Khan_votes/ number_votes), '.2f')
percent_Correy = format((100 * Correy_votes / number_votes), '.2f')
percent_Li = format((100 * Li_votes / number_votes), '.2f')
percent_Otooley = format((100 * Otooley_votes / number_votes), '.2f')
#find the winner
winner = max(candidate_counter2, key = candidate_counter1.count)
# Final Print
print(f''' "ELECTION RESULTS"
------------------------------
Total Votes: {number_votes}
------------------------------
{candidate_counter2[0]}: {percent_Khan}% ({Khan_votes})
{candidate_counter2[1]}: {percent_Correy}% ({Correy_votes})
{candidate_counter2[2]}: {percent_Li}% ({Li_votes})
{candidate_counter2[3]}: {percent_Otooley}% ({Otooley_votes})
Winner: {winner}
----------------------------
''') 
# open text file
poll_txt = open("poll_txt.txt", "w")
# save into a text file 
poll_txt.write(f''' ELECTION RESULTS
------------------------------------
Total Votes: {number_votes}
------------------------------------
{candidate_counter2[0]}: {percent_Khan}% ({Khan_votes})
{candidate_counter2[1]}: {percent_Correy}% ({Correy_votes})
{candidate_counter2[2]}: {percent_Li}% ({Li_votes})
{candidate_counter2[3]}: {percent_Otooley}% ({Otooley_votes})
-------------------------------------
Winner: {winner}
-------------------------------------
''')