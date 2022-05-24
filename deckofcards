#!/usr/bin/env python3
import random
from pprint import pprint as pprint
def main():
    global deck
    global hand
    deck = {}
    deck = make_deck()
    hand = draw_hand()
    print(f'Your hand contains {hand}')

def make_deck():
    global deck
    suits = {"Spades", "Hearts", "Clubs", "Diamonds"}

    for key in suits:
        if key not in deck:
            deck[key] = list()
            deck[key].extend(make_suit(key))
    return deck
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
                list_of_values.append("{} of {}".format(special[x-len(numbered_cards)+1], key))
    return list_of_values

    dict[key].extend()
def draw_hand(turn = 1):
    global deck
    hand = []
    if turn == 1:
        for x in range(7):
            suit = random.choice(list(deck.values()))
            card = random.choice(list(suit))
            hand.append(card)
            suit = search(deck, card)
            remove_card(suit, card)
            # pprint(suit)
            # pprint(card)
            # pprint(deck)
    return hand
    return deck
def search(dict, lookup):
    for key, value in dict.items():
        for v in value:
            if lookup in v:
                return key
def remove_card(suit, card):
    global deck
    deck[suit] = [s for s in deck[suit] if card not in s]
    return deck


if __name__ == '__main__': main()
