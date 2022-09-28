import os

import csv

csvpath = os.path.join('Resources','budget_data.csv')

months = []
profit_loss = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    print(csvreader)