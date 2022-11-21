import csv

houses = {
    "Gryffindor": 0,
    "Hufflepuff": 0,
    "Ravenclaw": 0,
    "Slytherin": 0
}

with open("hogwarts.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)    # skip first line
    for row in reader:  # reader reads row by row and returns each row as list
        house = row[1]
        houses[house] += 1
    
for house in houses:
    print(f"{house}: {houses[house]} ")