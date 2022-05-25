#!/usr/bin/env python3
import random
from pprint import pprint as pprint
import re

# Current Status:
# Deck is created and player can draw and discard cards to create/improve their hand
# Sets are displayed, but not evaluated
# Sequences are not displayed and not evaluated
# Computer player draws a single hand, which can be viewed but doesn't change over time
# End goal: Player can play poker against the CP and win if they have a stronger hand

global deck
global suits
deck = {}
suits = {"Spades", "Hearts", "Clubs", "Diamonds"}
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


class Hand:
    def __init__(self):
        self.hand = []
    global deck
    # Function to remove cards from the deck and add into the player's hand
    def draw_hand(self, turn=1):
        global deck
        hand = self.hand
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
    def display_hand(self, hand, sets):
        print(f'Your hand contains')
        pprint(self.hand)
        print(f'You have these sets: {sets}.')
        print('Choose a card to discard by typing 1,2,3 etc. or quit by typing 0.')
    def dis_comp_hand(self, hand):
        print(f'The computer has')
        pprint(self.hand)
    # Function to remove cards from player's hand
    def discard_card(self, card):
        self.hand = [s for s in self.hand if card not in s]
        return self.hand
    # Function for creating sets
    def create_sets(self, hand):
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

def main():
    # Setup variables
    global deck
    global suits
    turn = 1
    player = Hand()
    computer = Hand()
    continue_game = True
    deck = make_deck(deck, suits)
    hand = player.draw_hand(turn)
    computer_hand = computer.draw_hand(turn)
    sets = player.create_sets(hand)
    player.display_hand(hand, sets)
    print('Type 10 at any time to see the computer\'s hand.')
    while continue_game:
        turn += 1
        response = input()
        if int(response) == 0:  # Quit Game
            print('Thanks for playing!')
            break
        if int(response) == 10:
            computer.dis_comp_hand(computer_hand)
            print('Choose a card to discard by typing 1,2,3 etc. or quit by typing 0.')
            continue
        discard_choice = hand[int(response) - 1]
        player.discard_card(discard_choice)
        hand = player.draw_hand(turn)
        sets = player.create_sets(hand)
        player.display_hand(hand, sets)



if __name__ == '__main__': main()
