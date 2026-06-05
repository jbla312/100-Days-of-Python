import art
import random

NUMBER = random.randint(1, 100)
game_over = False

print(art.logo)
print("Welcome to Number Guessing Game!")
print("Im thinking of a number between 1 & 100")

def check_guess(guess):
    """Compares your number to a random number between 1 and 100 and
    lets you know if its to high or low"""
    reply = ""
    if guess == NUMBER:
        print("You guessed the number! You Win!")
        return True
    elif guess > NUMBER:
        print("Too high!")
    else:
        print("Too low!")
    return False


difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == "easy":
    lives = 10
elif difficulty == "hard":
    lives = 5
else:
    lives = 2
    print("You didnt follow the rules! Now you're down some lives... Good Luck!")

#   Continue the game until the number is guessed or lives run out
while lives > 0 and not game_over:
    print(f"You have {lives} attempts remaining to guess the number!")
    # guess = input("Make a guess: ")
    game_over = check_guess(int(input("Make a guess: ")))
    if not game_over:
        lives -= 1

if lives == 0:
    print("You ran out of lives! You lose!")