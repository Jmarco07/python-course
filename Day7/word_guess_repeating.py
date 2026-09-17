import random

stage = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(f"The chosen word is: {chosen_word}")

correct_guesses = []
game_over = False
lives = 0
while not game_over:
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
        lives += 1

    if lives == 6:
        game_over = True
        print("You lose!")

    if "_" not in new_guess:
        game_over = True
        print("You won!")

    print(stage[lives])