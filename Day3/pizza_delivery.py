print("Welcome to python pizza delivery!")
size = input("What size pizza do you want? S, M, or L: ")
pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

if size == "S" or size == "s":
    bill = 15
    if pepperoni == "y" or pepperoni == "Y":
        bill += 2
    if extra_cheese == "y" or extra_cheese == "Y":
        bill += 1
elif size == "M" or size == "m":
    bill = 20
    if pepperoni == "y" or pepperoni == "Y":
        bill += 3
    if extra_cheese == "y" or extra_cheese == "Y":
        bill += 1
elif size == "L" or size == "l":
    bill = 25
    if pepperoni == "y" or pepperoni == "Y":
        bill += 3
    if extra_cheese == "y" or extra_cheese == "Y":
        bill += 1

print(f"Your final bill is: ${bill}")