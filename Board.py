class Board:
    def __init__(self, deck = None):
        self.deck = deck if not deck is None else []