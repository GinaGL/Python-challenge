import os 
import csv

election_data = os.path.join("PyRoll","Resources","election_data.csv")

Candidates = []
num_votes = []
percent_votes = []
total_votes = 0 

with open (election_data, "r",newline="") as csvfile: 
     csvreader = csv.reader(csvfile, delimiter = ",")
     csv_header = next(csvreader)

     for row in csvreader:
        total_votes += 1


        if row[2] not in Candidates:
                Candidates.append(row[2])
                index = Candidates.index(row[2])
                num_votes.append(1)
        else:
                index = Candidates.index(row[2])
                num_votes[index] += 1 

        for votes in num_votes:
                percentage = (votes/total_votes) * 100
                percentage = round(percentage,3)
                percentage = "{:.3f}%".format(percentage)
                percent_votes.append(percentage)

winner = max(num_votes)
index = num_votes.index(winner)
winning_candidate = Candidates[index]
     
print ("Election Results")
print ("--------------------------")
print (f"Total Votes: {str(total_votes)}")
print ("--------------------------")

for i in range (len(Candidates)):
   print (f"{Candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
print ("--------------------------")
print (f"Winner: {winning_candidate}")
print ("--------------------------")



output= open("PyRoll/Analysis/Output.txt","w")
line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3,line4))

for candidate, percent_vote, num_vote in zip(Candidates, percent_votes, num_votes):
    line = str(f"{candidate}: {percent_vote} ({num_vote})")
    output.write('{}\n'.format(line))

line5 = "--------------------------"
line6 = str(f"Winner: {winning_candidate}")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))
output.close()






