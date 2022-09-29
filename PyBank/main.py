import os

import csv

csvpath = os.path.join('Resources','budget_data.csv')

profit = []
profit_change = []

total_months = 0
total_profit_change = 0 
monthly_profit_change = 0


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    csv_header = next(csvreader)

    for row in csvreader:
        total_months =+ 1
        total_profit_change =+ int(row[1])

        profit.append(row[1])

            
    print("Months:", total_months)
    print(total_profit_change)
    print(profit)

