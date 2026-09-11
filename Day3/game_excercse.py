print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("left or right?")

if choice1 == "left" or  choice1 == "Left":
    choice2 = input("swim or wait?")
    if choice2 == "wait" or choice2 == "Wait":
        choice3 = input("Which door?")
        if choice3 == "red" or choice3 == "Red" or choice3 == "blue" or choice3 == "Blue":
            print("Game Over")
        else:
            print("You Win!")
    else:
        print("game over")
else:
    print("You fell into a hole. Game Over.")