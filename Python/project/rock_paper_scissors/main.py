import random
def gameTool(c):
    
    if c == "R":
        return "rock"
    elif c == "P":
        return "paper"
    elif c == "S":
        return "scissors"
    else:
        return ""

def is_win(player, opponent):
    return (player == "R" and opponent == "S") or (player == "S" and opponent == "P") or (player == "P" and opponent == "R")

def game():
    user_score = 0
    comp_score = 0

    while user_score != 3 and comp_score != 3:
        user_choose = input("Make your movement rock (R), paper (P), scissors (S): ").upper()
        comp_choose = random.choice(["R", "S", "P"])        

        if is_win(user_choose, comp_choose):
            user_score += 1
        elif is_win(comp_choose, user_choose):
            comp_score += 1

        print(f"{gameTool(user_choose)} vs {gameTool(comp_choose)}")
        print(f"User = {user_score} v Computer = {comp_score}")

    print("Game is over.", end=" ")
    if user_score == 3:
        print("You win!")
    else:
        print("You lose!")

game()