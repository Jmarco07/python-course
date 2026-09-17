import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(f"The chosen word is: {chosen_word}")

# chosen_letters = list(chosen_word)

guess = input("Guess a letter: ").lower()
for char in chosen_word:
    if guess == char:
        print("Right")
    else:
        print("Wrong")