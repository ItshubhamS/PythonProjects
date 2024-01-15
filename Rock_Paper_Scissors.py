rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Write your code below this line 👇
import random

choice = int(input("what do you choose  0 for Rock ,1 for Paper ,2 for Scissors? \n"))
myList = [rock, paper, scissors]
p1choice = myList[choice]

print("You Choose\n" + p1choice)

computer_choice = random.randint(0, 2)
c1choice = myList[computer_choice]
print("Computer Chooses\n" + c1choice)


if choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and choice == 2:
    print("You lose")
elif computer_choice > choice:
    print("You lose")
elif choice > computer_choice:
    print("You win!")
elif computer_choice == choice:
    print("It's a draw")
