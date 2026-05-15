print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#Only way to win is Left, Wait, Yellow

choice = input('You\'re at a cross road. Where do you want to go?\nType "left" or "right":\n').lower()
if choice == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    choice = input('Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if choice == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        choice = input("One red, one yellow, and one blue. Which door do you choose?\n").lower()
        if choice == "red":
            print("Game over! You were hit with a giant fireball.")
        elif choice == "yellow":
            print("Congratulations! You are a survivor. You won the treasure.")
        else:
            print("Game over! You were dropped into the ocean and eaten by sharks")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Game Over! You fell into a hole")