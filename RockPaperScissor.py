import random
options = ["Rock", "Paper", "Scissors"]
player = input("Choose Rock, Paper, or Scissors: ")
computer = random. choice(options)
print("You chose: ", player)
print("Computer chose: ", computer)
if player == computer:
  print("It's a tie!")

