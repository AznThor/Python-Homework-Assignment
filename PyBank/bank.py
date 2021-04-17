# Import modules
import os
import csv
# declare your variables
Date = []
profitandlosses = []
profitandlosses_change = []
# Opening up the file
csvpath = os.path.join("budget_data.csv")
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Get rid of the header/1st row
    next(csvreader)
    for row in csvreader:
        profitandlosses.append(row[1])
        Date.append(row[0])
        
# sum of the months
datecounter = len(list(Date))

# Conversions
int_profitandlosses = [int(x) for x in profitandlosses]
# sum up the proffits and lossees
sum_profitandlosses = sum(int_profitandlosses)
# month to month profits and losses 
for row in range(1, len(int_profitandlosses)):
    profitandlosses_change.append(int_profitandlosses[row] - int_profitandlosses[row-1])
    # calculating the average change
totalchange = sum(profitandlosses_change)
lenghtchange_profitandlosses = len(profitandlosses_change)
averagechange = round((totalchange/lenghtchange_profitandlosses), 2)
# Define the max and min profit/loss change
max_change = max(profitandlosses_change)
min_change = min(profitandlosses_change)
# find the row that matches with the date 
max_index = profitandlosses_change.index(max_change)
min_index = profitandlosses_change.index(min_change)
max_date = Date[max_index + 1]
min_date = Date[min_index + 1]
# print
print(f'''Financial Analysis
----------------------------
Count of Months: {datecounter}
Total: ${sum_profitandlosses}
Average Change: ${averagechange}
Greatest Increase in Profits: {max_date} (${max_change})
Greatest Decrease in Profits: {min_date} (${min_change})''')
# Open file
bank_txt = open("bank_txt.txt", "w")
# Print results 
bank_txt.write(f'''Financial Analysis
----------------------------
Count of Months: {datecounter}
Total: ${sum_profitandlosses}
Average Change: ${averagechange}
Greatest Increase in Profits: {max_date} ($ {max_change})
Greatest Decrease in Profits: {min_date} ($ {min_change})''')