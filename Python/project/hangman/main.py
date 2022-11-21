import random
import string
from words import words # import words list

# returns a word from given words list
def get_hangman_word(words):
    word = random.choice(words)
    # eliminate the words contain ' ' and '-' for hangman game
    while ' ' in word or '-' in word:
        word = random.choice(words)
    return word.upper()

def hangman():  
    live = 6
    word = get_hangman_word(words)
    word_letter = set(word) # letters in the world
    used_letter = set()  # what the user guessed
    alphabet = set(string.ascii_uppercase)

    while live > 0 and len(word_letter) > 0:
        # print the used letters
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print()
        print(f"You have {live} live left and you have used these letters: ", ' '.join(used_letter))

        # what current word is (ie W _ R D)
        word_list = [letter if letter in used_letter else '_' for letter in word]
        print("Current word: ", " ".join(word_list), "\n")

        guess = input("Guess a letter: ").upper()
        if guess in alphabet - used_letter:
            used_letter.add(guess)
            if guess in word_letter:
                word_letter.remove(guess)
            else:
                print("Letter is not in word")
                live -= 1
        elif guess in used_letter:
            print("You have already used that charachter. Please try again")
        else:
            print("Invalid charachter. Please try again")

    if live > 0:
        print(f"Yay, congrats. You have guessed the word {word} correctly!")
    else:
        print(f"You died. The word was {word}.")

hangman()