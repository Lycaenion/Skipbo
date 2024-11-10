import unittest
from itertools import count
from unittest import removeResult

from Classes.Game import *

class TestGameFunctions(unittest.TestCase):

    #function to test population of the game deck
    def test_populate_game_deck(self):

        expected_game_deck_size = 162

        result = populate_game_deck()
        game_deck_size = len(result)

        self.assertEqual(game_deck_size, expected_game_deck_size)

    def test_populate_player_deck(self):

        expected_player_deck_size = 30

        game_deck = populate_game_deck()

        result = populate_player_deck(game_deck)
        player_deck_size = len(result)

        self.assertEqual(player_deck_size, expected_player_deck_size)

    def test_decrease_of_game_deck_after_player_deck_population(self):

        expected_num_cards_in_game_deck = 132

        game_deck = populate_game_deck()

        player_deck = populate_player_deck(game_deck)
        game_deck_size = len(game_deck)

        self.assertEqual(game_deck_size, expected_num_cards_in_game_deck)

    def test_populate_player_hand(self):

        player_hand_expected_size = 5

        game_deck = populate_game_deck()

        player_hand = populate_player_hand(game_deck)
        player_hand_size = len(player_hand)


        self.assertEqual(player_hand_size, player_hand_expected_size)

    def test_decrease_of_game_deck_after_population_of_player_hand(self):

        expected_num_cards_in_game_deck = 157

        game_deck = populate_game_deck()

        player_hand = populate_player_hand(game_deck)
        game_deck_size = len(game_deck)

        self.assertEqual(game_deck_size, expected_num_cards_in_game_deck)

    def test_decrease_of_game_deck_after_population_of_2_players(self):

        expected_num_cards_in_game_deck = 92

        game_deck = populate_game_deck()

        player_x_deck = populate_player_deck(game_deck)
        player_x_hand = populate_player_hand(game_deck)
        player_y_deck = populate_player_deck(game_deck)
        player_y_hand = populate_player_hand(game_deck)

        self.assertEqual(len(game_deck), expected_num_cards_in_game_deck)

    def test_check_if_build_is_permitted_true(self):

        card = Card(2)
        card_one = Card(1)
        pile = [card_one]

        print(pile)

        result = check_if_build_permitted(card, pile)

        self.assertEqual(result, True)

    def test_check_if_build_is_permitted_false(self):
        card = Card(3)
        card_one = Card(1)
        pile = [card_one]

        result = check_if_build_permitted(card, pile)

        self.assertEqual(result, False)