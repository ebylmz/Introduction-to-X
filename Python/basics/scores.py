scores = [] # list of scores

while True:
    val = float(input("Score: "))
    if 0 <= val and val <= 100: 
        scores.append(val)
    else:
        print("Score must be in closed range 0 to 100")
    
    exit = input("Do you want to continue? ")
    if exit.lower() in ["n", "no"]:
        break

print("Scores : " + str(scores))
print("Average: " + str(sum(scores) / len(scores)))