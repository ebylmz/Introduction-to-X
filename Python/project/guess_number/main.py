import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess > random_number:
            print("Guess again. Too high")
        elif guess < random_number:
            print("Guess again. Too low")
    print(f"Yay, congrats. You have guessed the number {random_number} correctly!")

def computer_guess(x):
    guess = 0
    feedback = ""
    low = 1
    high = x

    while feedback != "c":
        guess = random.randint(low, high)

        # randint throws  exp, if low and high are same
        if low != high:
            feedback = input(f"Is {guess} too high (H), too low (L) or correct (C) ? ").lower()
        else:
            guess = high # could also be low, since they are same

        if feedback in ["l", "low", "lower"]:
            high = guess - 1
        elif feedback in ["h", "high", "higher"]:
            low = guess + 1
    print(f"Yay I have guessed the number {guess} correctly!")

computer_guess(10)