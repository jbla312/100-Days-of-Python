import art

print(art.logo)
print("Welcome to Silent Bidding! We will now begin.")

#   Field Values
name_bids = {}
name = ""
more_bidders = ""
bid = 0
highest_bid = 0
winning_name = ""

# Ask the user for input
name = input("What is your name?\n")
bid = int(input("What is your bid?\n"))

# Save data into dictionary {name: bid}
name_bids[name] = bid

# Find out whether new bids need to be added
more_bidders = input("Is there anyone else who would like to bid?\n").lower()

#   Use while loop to add more names and bids until all bidders are finished
while more_bidders != "no":
    if more_bidders == "yes":
        print("\n" * 25)
    else:
        print("Invalid input try again.\n")

    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n"))
    name_bids[name] = bid
    more_bidders = input("Is there anyone else who would like to bid?\n").lower()


print("\n" * 25)

#   Loop to find the highest bid
for key in name_bids:
    if name_bids[key] > highest_bid:
        highest_bid = name_bids[key]
        winning_name = key

#   Print winning bid and name
print(f"The winner is {winning_name} with a bid of ${name_bids[winning_name]}")

