import random
print("Welcome to Rock, Paper, Scissors!")
print("rules are: \nRock beats Scissors\nScissors beats Paper\nPaper beats Rock")
print("To end game press 7")
choices = ["Rock", "Paper", "Scissors"]
while True:
  user_choice = int(input("Enter your choice: 0 for Rock, 1 for Paper, 2 for Scissors, or 7 to quit: "))
  if user_choice == 7:
    print("Game Over")
    break
  if user_choice not in (0, 1, 2):
    print("Invalid choice")
    continue

  computer_choice = random.randint(0, 2)
  if user_choice == computer_choice:
    print("select different kiddo")
  elif (user_choice == 0 and computer_choice == 2) or (user_choice == 2 and computer_choice == 1) or (user_choice == 1 and computer_choice == 0):
    print("You win! You chose", choices[user_choice], "and the computer chose", choices[computer_choice])
  else:
    print("You lose! You chose", choices[user_choice], "and the computer chose", choices[computer_choice])