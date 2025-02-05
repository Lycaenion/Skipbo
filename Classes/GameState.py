class GameState:
    """Game state will hold a list of players and a list with all the available cards in the common game deck and the cards already placed in the build piles"""


    def __init__(self, players, game_deck):
        self.players = players
        self.game_deck = game_deck
        self.build_piles = [[],[],[],[]]

    def get_game_state(self):

        return self.players, self.game_deck, self.build_piles

    def set_game_state(self, players, game_deck, build_piles):
        self.players = players
        self.game_deck = game_deck
        self.build_piles = build_piles

    def get_player(self, player_id):

        num_of_players = self.players.count()

        for i in range(num_of_players):
            if self.players[i].player_id == player_id:
                return self.players[i]

    def get_build_pile(self, num):
        return self.build_piles[num]

    def get_build_piles(self):
        return self.build_piles

    def set_build_piles(self, build_piles):
        self.build_piles = build_piles
        return