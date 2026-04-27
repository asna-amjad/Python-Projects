import random
from art import logo, vs
from game_data import data


def extract_data(account):
    """Extract data from game_data.py into printable format."""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"

def check_result(choice, followers_a, followers_b):
    # Check if user's guess is correct and print feedback.
    if followers_a > followers_b:
        return user_choice == "a"
    else:
        return user_choice == "b"

print(logo)
score = 0
keep_playing = True
profile_b = random.choice(data)

### Loop to make the game repeatable
while keep_playing:

    # Generate random account from game_data.py
    # Make account B tha account A
    profile_a = profile_b
    profile_b = random.choice(data)

    if profile_a == profile_b:
        profile_b = random.choice(data)

    print(f"Compare A: {extract_data(profile_a)}.")
    print(vs)
    print(f"Against B: {extract_data(profile_b)}.")

    # Ask for user choice.
    user_choice = input("Who has more followers? Type 'A' or 'B' ").lower()

    # make the screen clear after user input
    print("\n" * 20)
    print(logo)

    # Get follower counts
    follower_count_a = profile_a["follower_count"]
    follower_count_b = profile_b["follower_count"]
    is_correct = check_result(user_choice, follower_count_a, follower_count_b)

    # Print feedback based on user's choice
    if is_correct:
        score += 1
        print(f"You are right! Current score: {score}")
    else:
        print(f"Sorry, You are wrong! Final score: {score}")
        keep_playing = Fal
