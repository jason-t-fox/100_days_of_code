import hangman_words
import hangman_art
import random

#initialize variables
answer = random.choice(hangman_words.word_list)
answer_len = len(answer)
answer_display = []
user_lives = 6
user_guesses = []
game_over = False

#set initial display
for _ in range(answer_len):
    answer_display.append("_")

print(hangman_art.logo)
#print(answer)
print(f"The word has {answer_len} characters.")
print(''.join(answer_display))

#begin
while not game_over:
    user_guess = input("Guess a letter: ").lower()

    for position in range(answer_len):
        letter = answer[position]
        if letter == user_guess:
            answer_display[position] = letter
    
    if user_guess not in answer:
        print(hangman_art.stages[user_lives])
        user_lives -= 1
        user_guesses.append(user_guess)
        user_guesses_str = ','.join(user_guesses)
        print(f"{user_lives} choices left")
        print(f"[{user_guesses_str}] are the incorrect choices so far")

    print(''.join(answer_display))

    if "_" not in answer_display:
        game_over = True
        print("you won!")
    
    if user_lives == 0:
        game_over = True
        print(hangman_art.stages[user_lives])
        print(f"you lost! The answer was {answer}")

