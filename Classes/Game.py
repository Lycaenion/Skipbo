"""Game will hold actions, handle logic and communicate with the game state."""
"""Game will create players with decks, game deck and pass it along to the game state."""
"""Actions available are: Build, discard and draw. Build is available from both player hand and player discard piles. When player runs out of cards on hand, 5 new ones will be given and the player continues."""
"""The game will first be adapted for 2-3 players. Later players 4-6 will be added."""
from Classes.Player import *
from Classes.Card import *
import random
from Classes.GameState import *

CARD_VALUES = [
    '01',
    '02',
    '03',
    '04',
    '05',
    '06',
    '07',
    '08',
    '09',
    '10',
    '11',
    '12'
]

PLAYER_STOCK_PILE_SIZE = 30
PLAYER_HAND_SIZE = 5


players = []
game_state = None
game_deck = []
shuffle_pile = []
number_of_players = 2
player_turn = 0

def create_game():


    game_deck = populate_game_deck()

    for i in range(number_of_players):
        player_stock_pile = populate_player_stock_pile(game_deck)
        player_hand = populate_player_hand(game_deck)
        player = Player(i,player_hand, player_stock_pile)
        players.append(player)

    #game_state = GameState(players, game_deck)


    return

def populate_game_deck():
    temp_deck = []
    for i in range(12):
        for j in range(12):
            card = Card(CARD_VALUES[j])
            temp_deck.append(card)

    for i in range(18):
        temp_deck.append(Card('SKIPBO'))

    random.shuffle(temp_deck)


    return temp_deck

def populate_player_stock_pile(game_deck):

    player_deck = []
    for i in range(PLAYER_STOCK_PILE_SIZE):
        player_deck.append(game_deck[i])

    for i in range(PLAYER_STOCK_PILE_SIZE):
        game_deck.pop(i)

    return player_deck

def populate_player_hand(game_deck):
    player_hand = []

    for i in range(PLAYER_HAND_SIZE):
        player_hand.append(game_deck[i])

    for i in range(PLAYER_HAND_SIZE):
        game_deck.pop(i)

    return player_hand


def build_from_hand(player, card_index, pile_index , game_state):

    chosen_pile_index = pile_index
    chosen_card = player.player_hand[card_index-1]

    print('here')

    result = check_if_build_permitted(chosen_card, chosen_pile_index, game_state)

    chosen_pile = game_state.build_piles[chosen_pile_index-1]


    if result:

        player.player_hand.remove(chosen_card)
        chosen_pile.append(chosen_card)

        if len(chosen_pile) == 12:
            empty_build_pile(pile_index, game_state)

        return
    if result is False:
        print('error')
        return

def build_from_player_stock_pile(player, build_pile_index, game_state):

    chosen_card = player.player_stock_pile[-1]
    result = check_if_build_permitted(chosen_card, build_pile_index, game_state)


    if result is True:
        player.player_stock_pile.pop()
        game_state.build_piles[build_pile_index].append(chosen_card)

        if len(game_state.build_piles[build_pile_index]) == 12:
            empty_build_pile(build_pile_index, game_state)

    else:
        print('Error')
    return

def build_from_discard_pile(player, discard_pile_num, build_pile_num, game_state):

    discard_pile = player.player_discard_piles[discard_pile_num-1]
    chosen_card = discard_pile[-1]
    result = check_if_build_permitted(chosen_card, build_pile_num, game_state)
    build_piles = game_state.get_build_piles()

    if result is True:
        discard_pile.pop()
        build_piles[build_pile_num].append(chosen_card)
        game_state.set_build_piles(build_piles)

        if len(game_state.build_piles[build_pile_num]) == 12:
            empty_build_pile(build_pile_num, game_state)
    else:
        print('error')
    return

def discard_to_pile(player, input_a, input_b ):
    #input_card = int(input())
    #input_pile = int(input())

    chosen_card = player.player_hand[input_a-1]
    chosen_pile = player.player_discard_piles[input_b-1]

    player.player_hand.pop(input_a-1)

    chosen_pile.append(chosen_card)
    
    return

def draw(player):
    STANDARD_HAND_SIZE = 5
    player_hand = player.get_player_hand()
    num_of_cards_in_hand = len(player_hand)

    if len(game_deck) < 5:
        shuffle_deck()

    for i in range(STANDARD_HAND_SIZE-num_of_cards_in_hand):
        card = game_deck[-1]
        game_deck[-1].pop()
        player_hand.append(card)
    return

def empty_build_pile(build_pile_number, game_state):

    pile = game_state.get_build_pile(build_pile_number)

    for card in pile:
        shuffle_pile.append(card)

    pile.clear()
    game_state.set_build_pile(build_pile_number, pile)

def shuffle_deck():

    random.shuffle(shuffle_pile)
    game_deck.extend(shuffle_pile)
    shuffle_pile.clear()

    return

def change_player_turn(player_turn):

    if player_turn > number_of_players + 1:
        player_turn = 0
    else:
        player_turn + 1
    return

# def player_turn(player_id):
#     player = game_state.get_player(player_id)
#
#     action = input("What do you want to do?")
#     if action == 1:
#         build_from_hand(player_id)
#     if action == 2:
#         build_from_discard_pile(player_id)
#     if action == 3:
#         discard_to_pile(player_id)
#
#     draw(player)
#
#     return

def check_if_build_permitted(chosen_card, chosen_pile_index, game_state):
    print('start check')
    chosen_pile = game_state.build_piles[chosen_pile_index - 1]
    chosen_card

    print(chosen_card.card_value)

    if chosen_card.card_value == 'SKIPBO':

        return True

    value = (int(chosen_card.card_value)) #2

    if len(chosen_pile) == 0:

        if value == 1:
            return True
        else:
            return False
    else:
        chosen_pile_value = int(chosen_pile[-1].card_value)

        if value == chosen_pile_value + 1:
            return True
        else:
            return False

