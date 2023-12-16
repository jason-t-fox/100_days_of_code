import art  # imports
import game_data
import random


def pick_two():
    """Choose two to compare. Choice 1 may be short-circuited in the main function, if the game loops to a second
    round or beyond."""
    choice_one, choice_two = random.sample(game_data.data, k=2)
    return choice_one, choice_two


def game_main():
    """main game function"""
    old_p1 = {}
    keep_going = True
    score = 0
    while keep_going is True:
        if old_p1 == {}:  # this if block will short circuit p1 if the game loops.  This is intentional
            p1, p2 = pick_two()
        else:
            p1 = old_p1
            _, p2 = pick_two()
        print(art.logo)
        print(f"Your current score is {score}.")
        print("Compare A: " + p1['name'] + ", " + p1['description'] + ", from " + p1['country'] + ".")
        print(art.vs)
        print("Against B: " + p2['name'] + ", " + p2['description'] + ", from " + p2['country'] + ".")
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()  # covering possible answer conditions
        if answer == 'a':
            if p1['follower_count'] > p2['follower_count']:
                print("Correct! " + p1['name'] + " has " + str(p1['follower_count']) + " followers, while " + p2[
                    'name'] + " has " + str(p2['follower_count']) + " followers.")
                old_p1 = p1
                score += 1
            else:
                print("Wrong! " + p1['name'] + " has " + str(p1['follower_count']) + " followers, while " + p2[
                    'name'] + " has " + str(p2['follower_count']) + " followers.")
                keep_going = False
        if answer == 'b':
            if p2['follower_count'] > p1['follower_count']:
                print("Correct! " + p1['name'] + " has " + str(p1['follower_count']) + " followers, while " + p2[
                    'name'] + " has " + str(p2['follower_count']) + " followers.")
                old_p1 = p1
                score += 1
            else:
                print("Wrong! " + p1['name'] + " has " + str(p1['follower_count']) + " followers, while " + p2[
                    'name'] + " has " + str(p2['follower_count']) + " followers.")
                keep_going = False
        if keep_going is True:  # ask the player if they would like to keep going
            should_continue = input("Would you like to keep going? 'Y' for yes: ").lower()
            if should_continue == 'y':
                pass
            else:
                print("Game ending.")
                keep_going = False


game_main()
