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
    date.append(row[0])    

    profit.append(row[1])
    total_profit = total_profit + int(row[1])

    final_profit = int(row[1]) 
    monthly_changes_profits = final_profit - initial_profit 

    monthly_changes.append(monthly_changes_profits)
    
    average_change_profits = (total_change_profit/count)

    greatest_increase_profits = max(monthly_changes)
    greatest_decrease_profits = min(monthly_changes)

    increase_date = date[monthly_changes.index(greatest_increase_profits)]
    decrease_date = date[monthly_changes.index(greatest_decrease_profits)]

    total_change_profit = total_change_profit + monthly_changes_profits

    initial_profit = final_profit
    
    #watching the lecture videos again really helped with the above section
    
    with open('financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months is: " + str(count) + "\n")
    text.write("    Total Profit is: " + "$" + str(total_profit) +"\n")
    text.write("    Average Change is: " + '$' + str(int(average_change_profits)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
    text.write("----------------------------------------------------------\n")
    
    #https://www.w3schools.com/python/python_file_write.asp
    
    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months is: " + str(count))
    print("Total Profit is: " + "$" + str(total_profit))
    print("Average Change is : " + "$" + str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
    print("----------------------------------------------------------")

