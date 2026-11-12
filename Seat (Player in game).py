from Player import Player

class Seat:
    def __init__(self, player, buy_in):
        self.player = player
        self.stack = buy_in
        self.hand = []
        self.bet = 0
        self.total_bet = 0
        self.player.balance -= buy_in
        self.has_acted = False
        self.all_in = False

    def action(self):
        decision = int(input("What would you like to do (1: raise, 2: call, 3: check, 4: fold, 5: all in): "))
        return decision

    def leave_table(self):
        self.player.balance += self.stack
        self.stack = 0
