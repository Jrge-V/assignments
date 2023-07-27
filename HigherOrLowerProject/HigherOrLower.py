import random
import sys
import Art
import Game_data


def play_game(t_d, total_score):
    compare_a = random.randint(0, t_d)
    compare_b = random.randint(0, t_d)
    if compare_a == compare_b:
        re_roll(compare_a, compare_b, t_d)
    print(f"Compare A: {Game_data.data[compare_a]['name']}, a {Game_data.data[compare_a]['description']}, from {Game_data.data[compare_a]['country']}")
    print(Art.vs)
    print(f"Compare B: {Game_data.data[compare_b]['name']}, a {Game_data.data[compare_b]['description']}, from {Game_data.data[compare_b]['country']}")

    user_pick = pick_higher_lower("")

    if user_pick == 'A':
        if Game_data.data[compare_a]['follower_count'] >= Game_data.data[compare_b]['follower_count']:
            total_score += 1
            print(f"You're right! Current score: {total_score}.")
            return True, total_score
        else:
            print(f"Sorry that's wrong. Final score: {total_score}")
            sys.exit()

    elif user_pick == 'B':
        if Game_data.data[compare_b]['follower_count'] >= Game_data.data[compare_a]['follower_count']:
            total_score += 1
            print(f"You're right! Current score: {total_score}.")
            return True, total_score
        else:
            print(f"Sorry that's wrong. Final score: {total_score}")
            sys.exit()


def re_roll(c_a, c_b, t_d):
    while c_a == c_b:
        c_b = random.randint(0, t_d)
    return c_b


def pick_higher_lower(u_p):
    user_choice = input("Who has more followers? Type 'A' or 'B': ").capitalize()
    if user_choice != "A" and user_choice != "B":
        pick_higher_lower(u_p)
    else:
        u_p = user_choice
        return u_p


print(Art.logo)
# returns 50, there are currently 49 entries in the dictionary
total_data = len(Game_data.data) - 1
score = 0

while True:
    result, score = play_game(total_data, score)
    if not result:
        break
