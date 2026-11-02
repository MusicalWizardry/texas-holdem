# Poker -> texas holdem class

import secrets
import random

class Poker:
    def __init__(self):
        self.total_players = []
        self.active_players = []
        self.pot = Pot()
        self.deck = Deck()
        # need to add bet to match
        self.dealer_button_index = 0

    def add_player(self, player):
        self.total_players.append(player)
        self.active_players.append(player)

    def remove_player(self, player):
        self.total_players.remove(player)
        self.active_players.remove(player)

    def move_dealer_button(self):
        self.dealer_button_index = (self.dealer_button_index + 1)%len(self.active_players)

    def collect_bets(self, player_ix):
        self.pot.amount += self.active_players[player_ix].bet
        self.active_players[player_ix].stack -= self.active_players[player_ix].bet

    def award_bets(self, player_ix):
        self.active_players[player_ix].stack += self.pot
        self.pot = 0

    def reset(self):
        self.pot = 0
        self.deck.shuffle()

    def run_bet_round(self, player_ix):
        raise NotImplementedError("run bet round")

    def deal_starting_cards(self):
        raise NotImplementedError("deal starting cards")


class Deck:
    def __init__(self):
        self.cards = []

        suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        secure_random = secrets.SystemRandom() # create a rng with ur systems random generator
        secure_random.shuffle(self.cards) # function of random that shuffles the list by editing the list itself

    def deal(self):
        return self.cards.pop()

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

class Player:
    def __init__(self, name, stack, total_bet, bet, id):
        self.name = name
        self.stack = stack
        self.bet = bet
        self.total_bet = total_bet
        self.id = id

    def action(self):
        decision = int(input("What would you like to do (1: raise, 2: call, 3: check, 4: fold): "))
        return decision


class Pot:
    def __init__(self, amount):
        self.amount = amount

class Board:
    def __init__(self, deck = None):
        self.deck = deck if not deck is None else []


Holdem = Poker()
deck = Deck()
card = deck.deal()
print(card.suit, card.rank)