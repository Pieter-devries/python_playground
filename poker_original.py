#!/usr/bin/env python3
import random
from pprint import pprint as pprint
import re

# Current Status:
# Deck is created and player can draw and discard cards to create/improve their hand
# Sets are displayed, but not evaluated
# Sequences are not displayed and not evaluated
# Computer player is not programmed
# End goal: Can player single poker and win if you have a better hand then the CP

global deck
global hand
global suits
deck = {}
hand = []
suits = {"Spades", "Hearts", "Clubs", "Diamonds"}

def main():
    # Setup variables
    global deck
    global hand
    global suits
    turn = 1
    continue_game = True
    while continue_game:
        deck = make_deck(deck, suits)
        hand = draw_hand(turn)
        sets = create_sets(hand)
        display_hand(hand, sets)
        response = input()
        if int(response) == 0:  # Quit Game
            print('Thanks for playing!')
            continue_game = False
        discard_choice = hand[int(response) - 1]
        discard_card(discard_choice)
        turn += 1

# Create initial deck
def make_deck(deck, suits):
    # Helper function for making the deck
    def make_suit(key):
        numbered_cards = range(1, 11)
        special = ["Ace", "Jack", "Queen", "King"]
        list_of_values = []
        for x in range(13):
            if x < len(numbered_cards) and x != 0:
                list_of_values.append("{} of {}".format(numbered_cards[x], key))
            else:
                if x == 0:
                    list_of_values.append("{} of {}".format(special[x], key))
                else:
                    list_of_values.append("{} of {}".format(special[x - len(numbered_cards) + 1], key))
        return list_of_values
    for key in suits:
        if key not in deck:
            deck[key] = list()
            deck[key].extend(make_suit(key))
    return deck
# Function to remove cards from the deck and add into the player's hand
def draw_hand(turn = 1):
    global deck
    global hand
    # Helper function for drawing hand
    def search(dict, lookup):
        for key, value in dict.items():
            for v in value:
                if lookup in v:
                    return key
    # Helper function for drawing hand
    def remove_card(deck, suit, card):
        deck[suit] = [s for s in deck[suit] if card not in s]
        return deck
    if turn == 1:
        for x in range(7):
            suit = random.choice(list(deck.values()))
            card = random.choice(list(suit))
            hand.append(card)
            suit = search(deck, card)
            remove_card(deck, suit, card)
    else:
        suit = random.choice(list(deck.values()))
        card = random.choice(list(suit))
        hand.append(card)
        suit = search(deck, card)
        remove_card(deck, suit, card)
    return hand
# Function to show hand to player
def display_hand(hand, sets):
    print(f'Your hand contains')
    pprint(hand)
    print(f'You have these sets: {sets}.')
    print('Choose a card to discard by typing 1,2,3 etc. or quit by typing 0.')
# Function to remove cards from player's hand
def discard_card(card):
    global hand
    hand = [s for s in hand if card not in s]
    return hand
# Function for creating sets
def create_sets(hand):
    # Helper function for creating sets and sequences
    def first_value(hand):
        values = []
        for card in hand:
            value = re.search('([\S]+)', card).group()
            values.append(value)
        return values
    # Helper function for creating sets
    def remove_duplicates(sets):
        return list(dict.fromkeys(sets))
    values = first_value(hand)
    duplicates = []
    for value in values:
        dupes = values.count(value)
        if dupes > 1:
            duplicates.append(f'{dupes} of {value}s')
    if duplicates:
        sets = remove_duplicates(duplicates)
        return sets
    sets = "No sets"
    return sets

if __name__ == '__main__': main()
