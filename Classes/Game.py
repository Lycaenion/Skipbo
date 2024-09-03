"""Game will hold actions, handle logic and communicate with the game state."""
from Classes.Player import Player

"""Game will create players with decks, game deck and pass it along to the game state."""
"""Actions available are: Build, discard and draw. Build is available from both player hand and player discard piles. When player runs out of cards on hand, 5 new ones will be given and the player continues."""
"""The game will first be adapted for 2-3 players. Later players 4-6 will be added."""
import Card
import random
CARD_VALUES = {
    'ONE' : 1,
    'TWO' : 2,
    'THREE' : 3,
    'FOUR' : 4,
    'FIVE' : 5,
    'SIX' : 6,
    'SEVEN' : 7,
    'EIGHT' : 8,
    'NINE' : 9,
    'TEN' : 10,
    'ELEVEN' : 11,
    'TWELVE' : 12
}

PLAYER_DECK_SIZE = 30
PLAYER_HAND_SIZE = 5

game_deck = []
players = []

number_of_players = 2

def create_game():
    for i in range(number_of_players):
        player_deck = populate_player_deck()
        player_hand = populate_player_hand()
        player = Player(i,player_hand, player_deck)
        players.append(player)

    return

def populate_game_deck():

    for i in range(12):
        for j in range(12):
            card = Card.Card(CARD_VALUES[j])
            game_deck.append(card)

    for i in range(18):
        game_deck.append(Card.Card('SKIPBO'))

    random.shuffle(game_deck)

    return

def populate_player_deck():

    player_deck = []
    for i in range(PLAYER_DECK_SIZE):
        player_deck.append(game_deck[i])

    for i in range(PLAYER_DECK_SIZE):
        game_deck.pop(i)

    return player_deck

def populate_player_hand():
    player_hand = []

    for i in range(PLAYER_HAND_SIZE):
        player_hand.append(game_deck[i])

    for i in range(PLAYER_HAND_SIZE):
        game_deck.pop(i)

    return player_hand

def build():
    return

def discard_to_pile():
    return

def draw():
    return

def change_player_turn():
    return

