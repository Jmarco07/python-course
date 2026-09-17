import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

password = ""
for i in range(0, nr_letters):
    password += random.choice(letters)
for i in range(0, nr_letters):
    password += random.choice(numbers)
for i in range(0, nr_letters):
    password += random.choice(symbols)

print(f"Your non randomized password is: {password}")

password_list = list(password)
random.shuffle(password_list)

shuffled_password = ""

for char in password_list:
    shuffled_password += char
print(f"Your randomized password is: {shuffled_password}")