import secrets

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

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