import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


my_choose = int(input("What do you choose? Type 0 for rock, 1 for Paper or 2 for Scissor. "))

if my_choose == 0:
    print(f"Rock {my_choose} {rock}")
elif my_choose == 1:
    print(f"Paper {my_choose} {paper}")
elif my_choose == 2:
    print(f"Scissor {my_choose} {scissor}")
else:
    print("You typed an invalid number. You lose!")

print("Computer Choose")
computer_choose = random.randint(0, 2)

if computer_choose == 0:
    print(f"Rock {computer_choose} {rock}")
elif computer_choose == 1:
    print(f"Paper {computer_choose} {paper}")
else:
    print(f"Scissor {computer_choose} {scissor}")
if my_choose == computer_choose:
    print("It's a tie")
elif (
    (my_choose == 0 and computer_choose == 2) or
    (my_choose == 1 and computer_choose == 0) or
    (my_choose == 2 and computer_choose == 1)
):
    print("You Won!!!")
else:
    print("You lose!!!")