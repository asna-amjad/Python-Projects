### The Blackjack Project

import random
from random import shuffle
from replit import clear
from art import logo

def deal_card(): # function to return a random card from the deck of cards
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    shuffled = random.choice(cards)
    return shuffled

def calc_score(cards):   # function to take a list of cards and calculate score from the cards
    if sum(cards) == 21 and len(cards) == 2:
        return 0         # 0 - a blackjack in our game

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(p_score, c_score):
    if p_score == c_score:
        return "It's a Draw"
    elif c_score == 0:
        return "Lose, Opponent has a Blackjack"
    elif p_score == 0:
        return "Won with a Blackjack"
    elif p_score > 21:
        return "You Lose, You Went Over"
    elif c_score > 21:
        return "You Win, Opponent Went Over"
    elif p_score > c_score:
        return "You Win"
    else:
        return "You Lose"

def blackjack_game():
    print(logo)
    user_cards = []
    computer_cards = []
    comp_score = -1
    player_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        player_score = calc_score(user_cards)
        comp_score = calc_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if player_score == 0 or comp_score == 0 or player_score > 21:
            is_game_over = True
        else:
            user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_choice == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while comp_score != 0 and comp_score < 17:
        computer_cards.append(deal_card())
        comp_score = calc_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {comp_score}")
    print(compare(player_score, comp_score))

while input("Do you want to play again? (y/n): ") == "y":
    clear()
    blackjack_game()
