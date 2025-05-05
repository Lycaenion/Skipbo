class Player:
    player_discard_piles = [[] * 4]

    def __init__(self, player_id, player_hand, player_stock_pile):
        self.player_number = player_id
        self.player_hand = player_hand
        self.player_stock_pile = player_stock_pile




    def get_player_hand(self):
        return self.player_hand

    def get_player_discard_piles(self):
        return self.player_discard_piles
