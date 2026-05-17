import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
player1 = [rock, scissors, paper]
computer = [rock, scissors, paper]
computer_choice = random.randint(0, 2)

print("Welcome to the game of Rock, Paper, Scissors")

player_choice = int(input("Choose 0 for rock, 1 for scissors, 2 for paper\n"))

if player_choice == 0:
    if computer_choice == 0:
        print("Tie Game")
    elif computer_choice == 1:
        print("You win!")
    else:
        print("You lose!")
elif player_choice == 1:
    if computer_choice == 0:
        print("You lose!")
    elif computer_choice == 1:
        print("Tie Game")
    else:
        print("You win!")
elif player_choice == 2:
    if computer_choice == 0:
        print("You Win!")
    elif computer_choice == 1:
        print("You lose!")
    else:
        print("Tie Game")
else:
    print("Invalid choice")
print(f"Your choice is {player_choice}")
print(player1[player_choice])
print(f"Computer choice is {computer_choice}")
print(computer[computer_choice])

