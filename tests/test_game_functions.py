import unittest
from itertools import count
from unittest import removeResult
from Classes.Player import *
from Classes.Game import *
from Classes.Card import *

class TestGameFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Runnning before everything')
    def setUp(self):
        print('running setup')
        player_a_hand = [Card('01'), Card('02'), Card('03'), Card('04'), Card('05')]
        player_a_deck = [Card('06'), Card('07'), Card('08'), Card('09'), Card('10')]
        player_b_hand = [Card('06'), Card('07'), Card('08'), Card('09'), Card('10')]
        player_b_deck = [Card('01'), Card('02'), Card('03'), Card('04'), Card('05')]
        self.player_a = Player(0, player_a_hand, player_a_deck)
        self.player_b = Player(1, player_b_hand, player_b_deck)

        self.game_deck = [Card('01'), Card('02'), Card('03'), Card('04'), Card('05'), Card('06'), Card('07'), Card('08'), Card('09'), Card('10') ]

        self.players = [self.player_a, self.player_b]

        self.game_state = GameState(self.players, self.game_deck)

        shuffle_pile = []


    def tearDown(self):
        print("teardown")
    #function to test the population of the game deck
    def test_populate_game_deck(self):

        expected_game_deck_size = 162

        result = populate_game_deck()
        game_deck_size = len(result)

        self.assertEqual(game_deck_size, expected_game_deck_size)

    def test_populate_player_deck(self):

        expected_player_deck_size = 30

        game_deck = populate_game_deck()

        result = populate_player_stock_pile(game_deck)
        player_deck_size = len(result)

        self.assertEqual(player_deck_size, expected_player_deck_size)

    def test_decrease_of_game_deck_after_player_deck_population(self):

        expected_num_cards_in_game_deck = 132

        game_deck = populate_game_deck()

        player_deck = populate_player_stock_pile(game_deck)
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

        player_x_deck = populate_player_stock_pile(game_deck)
        player_x_hand = populate_player_hand(game_deck)
        player_y_deck = populate_player_stock_pile(game_deck)
        player_y_hand = populate_player_hand(game_deck)

        self.assertEqual(len(game_deck), expected_num_cards_in_game_deck)

    def test_check_if_build_is_permitted_true(self):

        card_index = 0
        pile_index = 1


        result = check_if_build_permitted(self.player_a, self.player_a.player_hand[card_index], pile_index, self.game_state)

        self.assertEqual(result, True)

    def test_check_if_build_is_permitted_false(self):
        card_index = 3
        pile_index = 1

        result = check_if_build_permitted(self.player_a, self.player_a.player_hand[card_index], pile_index, self.game_state)

        self.assertEqual(result, False)

    def test_check_if_build_is_permitted_skipbo_card(self):

        self.player_a.player_hand = [Card('SKIPBO'), Card('02'), Card('03'), Card('04'), Card('05')]

        card_index = 0
        pile_index = 0

        result = check_if_build_permitted(self.player_a, self.player_a.player_hand[card_index], pile_index, self.game_state)

        self.assertEqual(result, True)

    def test_discard_to_pile(self):

        discard_to_pile(self.player_a, 1, 1)

        expected_num_of_cards_player_hand = 4
        size_player_hand = len(self.player_a.player_hand)

        expected_num_of_cards_discard_pile = 1
        size_discard_pile = len(self.player_a.player_discard_piles[0])

        self.assertEqual(size_player_hand, expected_num_of_cards_player_hand)
        self.assertEqual(size_discard_pile, expected_num_of_cards_discard_pile)

    def test_build_from_player_hand_empty_build_pile(self):

        self.game_state.build_piles = [[],[Card('01')],[Card('01')],[Card('01')]]

        build_from_hand(self.player_a, 1 , 1, self.game_state)

        expected_num_cards_hand = 4

        size_player_hand = len(self.player_a.player_hand)

        self.assertEqual(size_player_hand, expected_num_cards_hand)

    def test_build_from_player_hand_non_empty_build_pile(self):

        self.game_state.build_piles = [[], [Card('01')], [Card('01')], [Card('01')]]

        build_from_hand(self.player_a, 2, 2, self.game_state)

        expected_num_cards_hand = 4
        size_player_hand = len(self.player_a.player_hand)

        self.assertEqual(expected_num_cards_hand, size_player_hand)

    def test_empty_build_pile(self):
        self.game_state.build_piles = [[Card('01'), Card('02'), Card('03'), Card('04'), Card('05')], [Card('01'), Card('02'), Card('03'), Card('04')], [Card('01')], [Card('01')]]

        empty_build_pile(0, self.game_state)

        expected_pile_size = 0
        actual_pile_size = (len(self.game_state.build_piles[0]))

        self.assertEqual(expected_pile_size, actual_pile_size)



    @classmethod
    def tearDownClass(cls):
        print('tearing down everything')

if __name__ == '__main__':
    unittest.main()