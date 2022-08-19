import csv

filename = input("What is the name of the file?\n") + ".csv"

option = "y"

while option == "y":
    front = input("What is on the front of the card?\n")
    back = input("What is on the back of the card?\n")
    rows = str(front), str(back)
    with open(filename, 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(rows)
    option = input("Would you like to make another card? (y/n)\n")