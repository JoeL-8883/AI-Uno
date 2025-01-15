from Card import Card
from Deck import Deck
from Player import Player
from Bot import Bot
from util import *
import random
import sys


PLAYER_PLAYING = True
PLAYING = True
PLAYER_NAME = "Joe"
NUM_PLAYERS = 2
ANALYSIS = False


# Create players
players = []
if PLAYER_PLAYING:
    player = Player("Joe")
    players.append(player)
    for i in range(NUM_PLAYERS-1):
        bot = Bot("Bot " + str(i + 1))
        players.append(bot)
else:
    for i in range(NUM_PLAYERS):
        bot = Bot("Bot " + str(i + 1))
        players.append(bot)

random.shuffle(players) # Randomize player order

# Create a deck
deck = Deck()

# Assign cards to players (each player gets 7 cards)
for p in players:
    deck.initial_draw(p)

# Put the first card on the discard pile
print("First card is: " + str(deck.current) + " it is " + players[0].name + "'s turn.")
print()

# Game loop
while PLAYING:
    # Check if anyone has won
    for player in players:
        if len(player.get_hand()) == 0:
            print(player.name + " has won!")
            PLAYING = False
            sys.exit()
                
    if ANALYSIS:
        print("Player hands:")
        for p in players:
            print(p.name + ": " + str(p.get_hand()))

    # Player's turn
    for p in players:
        if PLAYER_PLAYING and p == player:
            moved = False

            print("Your turn!")
            print("Your hand: " + str(p.get_hand()))
            print("Current card: " + str(deck.current))
            while not moved:
                if p.has_valid_card(deck.current):
                    print("Play card (p(--)) or Draw card (d)?")
                    action = input().lower()

                    if action[0] not in ['p', 'd']:
                        print("Invalid action.")
                        continue
                    elif action[0] == 'p':
                        # Get the played card
                        played_card = action[1:].upper()
                        print(played_card)
                        '''Check if the played card is valid'''
                        # Check the player has the card
                        if played_card not in p.get_hand():
                            print("You do not have that card.")
                            continue
                        
                        # Check the card is valid
                        elif not can_play_card(played_card, deck.current):
                            print("Invalid card.")
                            continue
                        
                        # Play the card
                        else:
                            played_card = p.play(played_card)
                            deck.remove_card(played_card)
                            deck.current = played_card
                            moved = True
                            print(p.name+'-p' + deck.current)
                elif action[0] == 'd':
                    ### Write code to draw a card
                else:
                    drawed_card = deck.draw_card()
                    p.draw(drawed_card)
                    print("You do not have a valid card -- you get a " + drawed_card)
                    moved = True
    PLAYING = False

