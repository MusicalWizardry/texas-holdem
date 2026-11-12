from Poker import Poker
from Board import Board

class Texas_Holdem(Poker):
    def __init__(self, s_blind = 10, b_blind = 20):
        super().__init__()
        self.board = Board()
        self.s_blind = s_blind
        self.b_blind = b_blind
    
    def deal_starting_cards(self):
        for i in range(2):
            for seat in self.active_players:
                seat.hand.append(self.deck.deal())
    
    def round_over(self):
        if len(self.active_players) <= 1:
            return True
        for seat in self.active_players:
            if seat.stack > 0 and (not self.has_acted or self.bet < self.bet_to_match):
                return False
    
    def deal_comm_cards(self, count): # deals community cards  
        self.deck.deal()
        for i in range(count):
            self.board.deck.append(self.deck.deal())
    
    def run_bet_round(self, start_ix):
        for seat in self.active_players:
            seat.has_acted = False
        curr_ix = start_ix % len(self.active_players)

        while not self.round_over():
            seat = self.active_players[curr_ix]

            if seat.all_in: # for all in people
                seat.has_acted = True
                curr_ix = (curr_ix + 1) % len(self.active_players)
                continue # to skip this all in persons turn
            
            decision = seat.action()

            if decision == 1:
                raise_to = int(input(f"Currently {self.bet_to_match}\nRaise bet to: "))
                seat.bet = raise_to #nvm this system sucks -> must change
                self.bet_to_match = max(self.bet_to_match, seat.bet)
                for others in self.active_players:
                    others.has_acted = False
                seat.has_acted = True
            
            elif decision == 2:
                seat.bet = self.bet_to_match
                seat.has_acted = True
            
            elif decision == 3:
                seat.has_acted = True
            
            elif decision == 4:
                self.active_players.remove(seat)
                if self.active_players:
                    curr_ix %= len(self.active_players)
                continue
            
            elif decision == 5:
                seat.bet = seat.stack
                seat.all_in = True
                self.bet_to_match = max(self.bet_to_match, seat.bet)
                for others in self.active_players:
                    others.has_acted = False if not others.all_in or seat.bet == self.bet_to_match else others.has_acted
            
            curr_ix = (curr_ix + 1)% len(self.active_players)

