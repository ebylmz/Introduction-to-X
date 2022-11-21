import csv

# file = open("phonebook.csv", "a")   # open in append mode

# name = input("Name: ")
# number = input("Number: ")

# writer = csv.writer(file)
# writer.writerow([name, number])

# file.close()

# with close the file automaticly
with open("phonebook.csv", "a") as file:
    name = input("Name: ")
    number = input("Number: ")
    writer = csv.writer(file)
    writer.writerow([name, number])