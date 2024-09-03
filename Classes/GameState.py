class GameState:
    """Game state will hold a list of players and a list with all the available cards in the common game deck and the cards already placed in the build piles"""



    def __init__(self, players, game_deck):
        self.players = players
        self.game_deck = game_deck
        self.build_piles = [[]*4]

    def get_game_state(self):

        return self.players, self.game_deck, self.build_piles

    def set_game_state(self, players, game_deck, build_piles):
        self.players = players
        self.game_deck = game_deck
        self.build_piles = build_piles