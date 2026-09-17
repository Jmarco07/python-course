import random
from hangman_art import stage, logo
from hangman_words import word_list

print(logo)
chosen_word = random.choice(word_list)
# print(f"The chosen word is: {chosen_word}")

correct_guesses = []
game_over = False
lives = 6
while not game_over:
    print(f"******************************YOU HAVE {lives} LIVES LEFT!!!******************************")
    guess = input("Guess a letter: ").lower()
    new_guess = ""
    for char in chosen_word:
        if char == guess:
            new_guess += char
            correct_guesses.append(char)
        elif char in correct_guesses:
            new_guess += char
        else:
            new_guess += "_"
    print(new_guess)

    if guess not in chosen_word or not guess.isalpha():
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

    if lives == 0:
        game_over = True
        print(f"******************************IT WAS {chosen_word} You lose!******************************")

    if "_" not in new_guess:
        game_over = True
        print("******************************You won!******************************")

    print(stage[lives])