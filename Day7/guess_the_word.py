import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(f"The chosen word is: {chosen_word}")

word_guess = ""
guess = input("Guess a letter: ").lower()
for char in chosen_word:
    if char == guess:
        word_guess += char
    else:
        word_guess += "_"

    
print(word_guess)