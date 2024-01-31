import random

stages = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]

total_lives = 6
FinalList = []
word_list = ["ardvark", "baboon", "camel"]
randomletter = random.choice(word_list)
for i in range(len(randomletter)):
    FinalList += "_"
print(FinalList)
end_of_game = False
while end_of_game is False:
    print(f"You have {total_lives} lives left")
    GuessLetter = input("Guess the Value\n").lower()
    for position in range(len(randomletter)):
        letter = randomletter[position]
        if letter == GuessLetter:
            FinalList[position] = letter
    print(FinalList)
    if GuessLetter not in randomletter:
        total_lives -= 1

    if "_" not in FinalList:
        end_of_game = True
        print("you win")
    if total_lives == 0:
        end_of_game = True
        print("you Loose")
    print(stages[total_lives])
