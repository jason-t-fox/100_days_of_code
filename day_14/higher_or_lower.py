import art
import game_data
import random

game_state = None
keep_going = True
def pick_two():
    choice_one, choice_two = random.sample(game_data.data, k=2)
    return choice_one, choice_two


def game_main(p1={}):
    round_won = None
    if p1 == {}: # if the game was won last round, import the old p1
        p1, p2 = pick_two()
    else:
        _, p2 = pick_two()
    print(art.logo)
    print("Compare A: " + p1['name'] + ", " + p1['description'] + ", from " + p1['country'] + ".")
    print(art.vs)
    print("Against B: " + p2['name'] + ", " + p2['description'] + ", from " + p2['country'] + ".")
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    if answer == 'a':
        if p1['follower_count'] > p2['follower_count']:
            print("Correct! " + p1['name'] + " has " + str(p1['follower_count']) + " followers, while " + p2[
                'name'] + " has " + str(p2['follower_count']) + " followers.")
            round_won = True
            return p1, round_won
        else:
            print("Wrong! " + p1['name'] + " has " + str(p1['follower_count']) + " followers, while " + p2[
                'name'] + " has " + str(p2['follower_count']) + " followers.")
            round_won = False
            return p1, round_won
    if answer == 'b':
        if p2['follower_count'] > p1['follower_count']:
            print("Correct! " + p1['name'] + " has " + str(p1['follower_count']) + " followers, while " + p2[
                'name'] + " has " + str(p2['follower_count']) + " followers.")
            round_won = True
            return p1, round_won
        else:
            print("Wrong! " + p1['name'] + " has " + str(p1['follower_count']) + " followers, while " + p2[
                'name'] + " has " + str(p2['follower_count']) + " followers.")
            round_won = False
            return p1, round_won


# still need to figure out this loop
while keep_going is True:
    pick1 = {}
    if game_state is None:
        pick1, game_state = game_main()
    if game_state is True:
        pick1, game_state = game_main(p1=pick1)
    if game_state is False:
        keep_going = False


