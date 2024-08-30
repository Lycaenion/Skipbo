class Player:
    player_discard_piles = [[] * 4]

    def __init__(self, player_number, player_hand, player_deck):
        self.player_number = player_number
        self.player_hand = player_hand
        self.player_deck = player_deck



    def get_player_hand(self):
        return self.player_hand

    def get_player_discard_piles(self):
        return self.player_discard_piles
