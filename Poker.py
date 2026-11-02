from Deck import *
from Pot import *

class Poker:
    def __init__(self):
        self.total_players = []
        self.active_players = []
        self.pot = Pot(0)
        self.deck = Deck()
        self.bet_to_match = 0 #cbtm = current bet to match
        self.dealer_button_index = 0

    def add_player(self, player):
        self.total_players.append(player)
        self.active_players.append(player)

    def remove_player(self, player):
        self.total_players.remove(player)
        self.active_players.remove(player)

    def move_dealer_button(self):
        self.dealer_button_index = (self.dealer_button_index + 1) % len(self.total_players)

    def collect_bets(self, player_ix):
        player = self.active_players[player_ix]
        self.pot.amount += player.bet
        player.stack -= player.bet
        #at some point i have to make bet 0 - ideally next round.

    def award_bets(self, player_ix):
        self.active_players[player_ix].stack += self.pot.amount
        self.pot.amount = 0

    def reset(self):
        self.pot.amount = 0
        self.deck = Deck()
        self.deck.shuffle()
        self.active_players = self.total_players
        self.bet_to_match = 0

    def run_bet_round(self, player_ix):
        raise NotImplementedError("run bet round")

    def deal_starting_cards(self):
        raise NotImplementedError("deal starting cards")
