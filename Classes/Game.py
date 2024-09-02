"""Game will hold actions, handle logic and communicate with the game state."""
"""Game will create players with decks, game deck and pass it along to the game state."""
"""Actions available are: Build, discard and draw. Build is available from both player hand and player discard piles. When player runs out of cards on hand, 5 new ones will be given and the player continues."""
"""The game will first be adapted for 2-3 players. Later players 4-6 will be added."""

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

game_deck = []
players = []

number_of_players = 2

def create_game():
    return

def populate_game_deck():
    return

def populate_player_deck():
    return

def populate_player_hand():
    return

def build():
    return

def discard_to_pile():
    return

def draw():
    return

def change_player_turn():
    return

