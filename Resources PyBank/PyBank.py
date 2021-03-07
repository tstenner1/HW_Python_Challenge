import os 
import csv 
#import the modules 

PyBankcsv = os.path.join("Resources", "budget_data.csv")
#create a path for the CSV file in order for it to find the Pybank 

initial_profit = 0 
total_change_profits = 0 
count = 0 
total_profit = 0 

#these are the variables that are going to be needed to solve the problem for pybank

monthly_changes = []
profit = []
date = []

#we need these in order to have spots and or lists to store the data we are trying to get 

#now to open CVS, below are a few sources that I found useful for this portion 
#https://docs.python.org/3/library/csv.html
#https://www.geeksforgeeks.org/working-csv-files-python/

with open (PyBankcsv, newline="") as csvfile: 
    csvreader = csv.reader(csvfile,delimiter="")
    csv_header = next(csvreader)

    #https://stackoverflow.com/questions/53474110/python-determine-change-in-value-from-one-period-to-the-next

    for row in csvreader: 
        count = count + 1
    #count is needed in order to tally up the amount of months that are in the csv
