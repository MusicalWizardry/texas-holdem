# this class has to be kept separate from everything to do with the game
class Player:
    def __init__(self, name, balance, pid):
        self.name = name
        self.balance = balance
        self.pid = pid # player id
