print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island \nYour mission is to find the treasure.")
user_direction_choice = str(input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n')).lower()
if user_direction_choice != "left":
    print("You fall into a hole and thus your adventure ends!")
    exit()
user_lake_choice = str(input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n')).lower()
if user_lake_choice != "wait":
    print("You are eaten by a trout (but not a gru)!")
    exit()
user_door_choice = str(input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n")).lower()
if user_door_choice == "red":
    print("You are burned by fire!")
    exit()
elif user_door_choice == "blue":
    print("You are eaten by beasts who are most definitely not made of treasure!")
    exit()
elif user_door_choice == "yellow":
    print("You win! The treasure is full of cookies! Good job!")
    exit()
else:
    print("You walk into a wall, fall down, and bump your head!")
    exit()

# original code from the lesson had three layers of nested if statements and was harder to read then it needed to be. The structure (above) is cleaner, at least in my opinion.

#choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
#if choice1 == "left":
#  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
#  if choice2 == "wait":
#    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
#    if choice3 == "red":
#      print("It's a room full of fire. Game Over.")
#    elif choice3 == "yellow":
#      print("You found the treasure! You Win!")
#    elif choice3 == "blue":
#      print("You enter a room of beasts. Game Over.")
#    else:
#      print("You chose a door that doesn't exist. Game Over.")
#  else:
#    print("You get attacked by an angry trout. Game Over.")
#else:
#  print("You fell into a hole. Game Over.")