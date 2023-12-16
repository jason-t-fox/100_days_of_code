import random

#very modern graphics!
#initialize variables
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
Rock!
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
Paper!
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
Scissors!
'''

ascii_images = [rock, paper, scissors]
computer_choice = random.randint(0,2)

#user input
user_choice = input("What do you choose?\nType 0 for Rock, 1 for Paper, or 2 for Scissors:\n")
#adding some basic input verification, I did not do this for treasure island.
try:
  int(user_choice)
except:
   print("Please choose a valid number.")
   exit()
user_choice = int(user_choice)
if user_choice > 2 or user_choice < 0:
  print("Please choose a valid number.")
  exit()
#possible to wrap the user input section into a function and rerun it on an invalid input.  If this class doesn't cover this sort of thing later, I will try to add it in.

#begin the game!
print("The computer chooses:\n" + ascii_images[computer_choice])
print("You choose:\n" + ascii_images[user_choice])

if user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")
