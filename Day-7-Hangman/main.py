import random
import hangman_words
import hangman_art

lives = 6
game_over = False
correct_letters = []
placeholder = ""


# Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)

#   Randomly choose a word to start your game
chosen_word = random.choice(hangman_words.word_list)

#   Add underscores to show player how many letters there are
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)


#   While loop to keep playing until word is guessed or all lives are lost
while not game_over:

    # Take users letter guess
    guess = input("Guess a letter: ").lower()

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in correct_letters:
        print("Already guessed!")

    display = ""

    #   If letter guessed was correct then update display and save letter
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    #   If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #   Subtract a life from player and print newest hangman stage
    if guess not in chosen_word:
        lives -= 1
        print(f"you guessed {guess}, that's not in the word. You lose a life")
        print(hangman_art.stages[lives])
        print(f"****************************<???>/{lives} LIVES LEFT****************************")

        #   Lost all lives set game_over to True
        if lives == 0:
            game_over = True

            # Update the print statement below to give the user the correct word they were trying to guess.
            print(f"***********************YOU LOSE**********************")
            print(f"Correct word was: {chosen_word}")

    #   User guessed all letters correctly and wins
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")
