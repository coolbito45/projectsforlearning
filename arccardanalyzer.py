import csv
sum=0
with open("acaprdec.csv") as csvfile:

    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        action = row[2]
        description = row[3]
        if action == "Sales" and description != "Purse Missing Tap Fare":
            amount = row[8]
            sum+=float(amount.removeprefix("$"))
    print(sum)