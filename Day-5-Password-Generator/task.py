import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = ""
password_lst = []

# Gets the number of letters specified in a random order
for i in range(1,nr_letters+1):
    password_lst.append(random.choice(letters))

# Gets the number of symbols specified in a random order
for i in range(1,nr_symbols+1):
    password_lst.append(random.choice(symbols))

# Gets the number of numbers specified in a random order
for i in range(1,nr_numbers+1):
    password_lst.append(random.choice(numbers))

# Randomize the password_lst so it is always a different order
random.shuffle(password_lst)

# Create the password string from the list
for i in range(1,len(password_lst)):
    password = password + password_lst[i]

# Print the Password
print(password)