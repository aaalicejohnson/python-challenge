import os

import csv

csvpath = os.path.join('Resources','election_data.csv')
output_path = os.path.join('Analysis', 'election_results.txt')


candidates = []
stockham = []
degette = []
doane = []

total_votes = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes = total_votes + 1
        candidate = str(row[2])

        if candidate not in candidates: 
            candidates.append(candidate)

        if candidate == "Charles Casper Stockham":
            stockham.append(candidate)

        if candidate == "Diana DeGette": 
            degette.append(candidate)

        if candidate == "Raymon Anthony Doane": 
            doane.append(candidate)

stockham_total = len(stockham)
degette_total = len(degette)
doane_total = len(doane)

stockham_percent = (stockham_total / total_votes)*100 
degette_percent = (degette_total / total_votes)*100
doane_percent = (doane_total / total_votes)*100 

if stockham_total >= doane_total and degette_total:
    winner = "Charles Casper Stockham"

if doane_total >= stockham_total and degette_total:
    winner = "Raymon Anthony Doane"

if degette_total >= stockham_total and doane_total: 
    winner = "Diana DeGette"

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"Charles Casper Stockham: {stockham_percent:.3f}% ({stockham_total})")
print(f"Diana DeGette: {degette_percent:.3f}% ({degette_total})")
print(f"Raymon Anthony Doane: {doane_percent:.3f}% ({doane_total})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

with open(output_path, "w") as txtfile:
    txtfile.write("Election Results")
    txtfile.write("\n")
    txtfile.write("-------------------------")
    txtfile.write("\n")
    txtfile.write(f"Total Votes: {total_votes}")
    txtfile.write("\n")
    txtfile.write("-------------------------")
    txtfile.write("\n")
    txtfile.write(f"Charles Casper Stockham: {stockham_percent:.3f}% ({stockham_total})")
    txtfile.write("\n")
    txtfile.write(f"Diana DeGette: {degette_percent:.3f}% ({degette_total})")
    txtfile.write("\n")
    txtfile.write(f"Raymon Anthony Doane: {doane_percent:.3f}% ({doane_total})")
    txtfile.write("\n")
    txtfile.write("-------------------------")
    txtfile.write("\n")
    txtfile.write(f"Winner: {winner}")
    txtfile.write("\n")
    txtfile.write("-------------------------")
    txtfile.write("\n")



        




