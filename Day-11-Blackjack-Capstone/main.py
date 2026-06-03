import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play_again = "y"

def calculate_score(list):
    """Calculates the score of players hand. Will substitute a 1 for 11 if over 21"""
    if sum(list) == 21:
        return 0
    elif sum(list) > 21:
        if 11 in list:
            list.remove(11)
            list.append(1)
            print("Over 21 but Ace was Found and 10 switched to 1")
    score = sum(list)
    return score


def deal_card():
    """Adds a random card to the user or computer's list"""
    return random.choice(cards)

def continue_game():
    """Allows the user to keep playing until they choose to stop drawing cards"""
    #   Add up the user's and the computer's scores
    user_score = calculate_score(user_cards)
    print(f"Your cards are: {user_cards}, score is: {user_score}")
    print(f"Computers first card is: {computer_cards[0]}\n")
    if user_score == 0:
        return 21
    elif user_score > 21:
        return user_score
    else:
        draw_card = input("Do you want to draw another card? (y/n): ").lower()
        if draw_card == 'y':
            user_cards.append(deal_card())
            return continue_game()
        else:
            return user_score

def compare_scores(score1, score2):
    """Takes two scores and returns the highest score."""
    if score1 == score2:
        return "Its a Draw!"
    elif score2 == 0:
        return "Sorry you Lose"
    elif score1 == 0:
        return "Congrats you Win!"
    elif score1 > 21:
        return "Sorry you Lose"
    elif score2 > 21:
        return "Congrats you Win!"
    elif score1 > score2:
        return "Congrats you Win!"
    else:
        return "Sorry you Lose"

while play_again == "y":
    #   Print logo and initialize values
    print(art.logo)
    user_cards = []
    computer_cards = []
    user_score = 0
    computer_score = 0

    #   User and Computer should each get 2 random cards to start
    for count in range(0, 2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    #   Calls to start the game and returns the score
    user_score = continue_game()

    computer_score = calculate_score(computer_cards)

    #   Computer keeps drawing until at least 17
    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    #   Change Blackjack to a 21 for the final score
    if computer_score == 0:
        computer_score = 21

    print(f"Your cards are: {user_cards}, Final score is: {user_score}")
    print(f"Computer's cards are:{computer_cards}, Final score is: {computer_score}")
    print(compare_scores(user_score, computer_score))
    play_again = input("Do you want to play again? (y/n): ").lower()
    print("\n" * 25)
