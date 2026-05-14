print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
bill_plus_tip = bill * (1 + tip / 100)
split_bill = bill_plus_tip / people

# : marks the start of the formatting instructions.
# .2 tells Python you want exactly two decimal places.
# f stands for Fixed-point notation (essentially treating it as a float/decimal).
print(f"Each person should pay: $ {split_bill:.2f}")