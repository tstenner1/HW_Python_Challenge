#import modules
import os 
import csv 

#setting the path to the csv file for the pypoll
PyPollcsv = os.path.join("Resources","election_data.csv")

#lists for data to be stored in

vote_percent = []
unique_candidate = []
candidatelist = []
count = 0
vote_count = []

#the following contains opening the csv using the path above.  What ensues is 
#conducting the ask
#we must count the total number of votes
#append candidate names to list, 
#create set from said list for distinctive names
#total votes per candidate
#in turn % totals per candidate
#this order makes the most sense chronologically 

with open (Pypollcsv, newline= "") as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   csv_header = next(csvreader)
   
   
   for row in csvreader: 
     count = count + 1
     
     candidatelist.append(row[2])
     
   for x in set(candidatelist): 
     unique_candidate.append(x)
     
     y = candidatelist.count(x)
     vote_count.append(y)
#y is for the total amount of voters for the candidate being plugged into the equation 

     z = (y/count)*100 
     vote_percent.append 
  
  
#need max vote count as well 
  votecount = votecount["percentage"].sortvalues()
 
  winning_vote_count = max(vote_count)
  winner = unique_candidate[vote_count.index(winning_vote_count)]

print("Election Results")
print("-------------------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------------------")
for key, value in candidates.items():
    print(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ")")
print("-------------------------------------")
print("Winner: " + winner)
print("-------------------------------------")

new_file = open("pollresults.txt", "w")

new_file.write("Election Results \n")
new_file.write("------------------------------------- \n")
new_file.write("Total Votes: " + str(total_votes) + "\n")
new_file.write("------------------------------------- \n")
for key, value in candidates.items():
    new_file.write(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ") \n")
new_file.write("------------------------------------- \n")
new_file.write("Winner: " + winner + "\n")
new_file.write("------------------------------------- \n")

#to write a new file containing the info of the data that we are striving to get 
#https://www.w3schools.com/python/python_file_write.asp
