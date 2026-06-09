import game_data
import art
import random
import os

score = 0

def clear_screen():
    """Clears the terminal screen across Windows, Mac, and Linux."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_followers(loc_1, loc_2):
    print(f"{game_data.data[loc_1]["name"]} with {game_data.data[loc_1]["follower_count"]} million has more followers than "
          f"{game_data.data[loc_2]["name"]} with {game_data.data[loc_2]["follower_count"]} million")




def compare():
    global score
    game_over = False
    a = random.randint(0,len(game_data.data)-1)
    while not game_over:
        b = random.randint(0, len(game_data.data) - 1)
        #   If A and B are the same then change B
        while a == b:
            b = random.randint(0, len(game_data.data) - 1)
        clear_screen()
        print(art.logo)
        print(f"Compare A: {game_data.data[a]["name"]}, {game_data.data[a]["description"]}, {game_data.data[a]["country"]}")
        print(art.vs)
        print(f"Against B: {game_data.data[b]["name"]}, {game_data.data[b]["description"]}, {game_data.data[b]["country"]}\n")
        print(f"Current Score: {score}\n")
        choice = input("Who has more followers? Type 'A' or 'B': \n").lower()

        if int(game_data.data[a]["follower_count"]) > int(game_data.data[b]["follower_count"]):
            correct_choice = "a"
            print_followers(a, b)
        else:
            correct_choice = "b"
            print_followers(b, a)
            a=b

        if correct_choice == choice:
            score += 1
        else:
            game_over = True


    return score




total_score = compare()
print(f"Congrats on your final score of {total_score}")
