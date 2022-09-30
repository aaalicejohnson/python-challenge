import os

import csv

csvpath = os.path.join('Resources','budget_data.csv')
output_path = os.path.join('Analysis', 'analysis.txt')

profit = []
profit_change = []
date = []

total_months = 0
initial_profit = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    csv_header = next(csvreader)

    for row in csvreader:
        total_months = total_months + 1

        monthly_profit = int(row[1])
        monthly_profit_change = monthly_profit - initial_profit
        
        profit.append(monthly_profit)
        date.append(row[0])
        profit_change.append(monthly_profit_change)

        initial_profit = monthly_profit
    
a = profit_change.pop(0)
b = date.pop(0)

pl_data = zip(date, profit_change)

sum_change = sum(profit_change)

total_profit = sum(profit)

average_change = float(sum_change / len(profit_change))

max_profit = max(profit_change)
min_profit = min(profit_change)

for month, change in pl_data:
    if change == max_profit:
        max_month = month
    if change == min_profit:
        min_month = month 

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(total_months))
print("Total: $" +str(total_profit))
print(f"Average Change: ${average_change:.2f}") 
print(f"Greatest Increase in Profits: {max_month} (${max_profit})")
print(f"Greatest Decrease in Profits: {min_month} (${min_profit})")

with open(output_path, "w") as txtfile:
    txtfile.write("Financial Analysis")
    txtfile.write("\n")
    txtfile.write("----------------------------")
    txtfile.write("\n")
    txtfile.write("Total: $" +str(total_profit))
    txtfile.write("\n")
    txtfile.write(f"Average Change: ${average_change:.2f}") 
    txtfile.write("\n")
    txtfile.write(f"Greatest Increase in Profits: {max_month} (${max_profit})")
    txtfile.write("\n")
    txtfile.write(f"Greatest Decrease in Profits: {min_month} (${min_profit})")










