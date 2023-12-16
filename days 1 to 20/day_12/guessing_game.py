#imports
import random

#initial variables
logo = '''
                                   .__                                               
   ____  __ __   ____   ______ _____|__| ____    ____      _________    _____   ____  
  / ___\|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\    / ___\__  \  /     \_/ __ \ 
 / /_/  >  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  >  / /_/  > __ \|  Y Y  \  ___/ 
 \___  /|____/  \___  >____  >____  >__|___|  /\___  /   \___  (____  /__|_|  /\___  >
/_____/             \/     \/     \/        \//_____/   /_____/     \/      \/     \/ 
 '''

def difficulty_choice(): # have player choose the game mode
    player_difficulty = input("Please type 'hard' for hard mode or 'easy' for easy mode: ").lower()
    if player_difficulty == 'easy':
        game_difficulty = 10
        print(f"You have {game_difficulty} guesses.")
        difficulty_chosen = True
    elif player_difficulty == 'hard':
        game_difficulty = 5
        print(f"You have {game_difficulty} guesses.")
        difficulty_chosen = True
    else: # try again if an invalid choice is made
        print("Invalid choice.")
        difficulty_chosen = False
        game_difficulty = 0
    return game_difficulty, difficulty_chosen # return answers

def answer_choice(guess, answer, guesses_left): #controls player guessing
    if guesses_left == 0:
        print("You have run out of guesses.  You lose.")
        game_state = True
    elif guess == answer:
        print(f"You win, the number was {answer}")
        game_state = True
    elif guess > answer:
        guesses_left -= 1
        print(f"Too high. You have {guesses_left} guesses to go.")
        game_state = False
    elif guess < answer:
        guesses_left -= 1
        print(f"Too low. You have {guesses_left} guesses to go.")
        game_state = False
    return game_state, guesses_left

def main_game(): 
    number_to_guess = random.randint(1, 100)
    print(number_to_guess)
    game_over = False
    difficulty_chosen = False
    while not game_over: #begin game loop
        while not difficulty_chosen: # ask player to set a difficulty level subloop
            game_difficulty, difficulty_chosen = difficulty_choice()
        player_guess = int(input("Pick a number: \n")) #player guessing main loop
        game_over, game_difficulty = answer_choice(player_guess, number_to_guess, game_difficulty)

print(logo) #start game
main_game()