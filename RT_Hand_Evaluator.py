from itertools import combinations
from Base_Hand_Evaluator import Base_Hand_Evaluator

class RealTime_Hand_Evaluator(Base_Hand_Evaluator):
    get_score([1,2,3,4])
    def get_score(self, cards):
        ranks = sorted([self.rank_to_rt[c.rank] for c in cards], reverse = True)
        suits = [c.suit for c in cards]
        is_flush = len(set(suits)) == 1
        print(suits)
    def evaluate_hand(self, hole_cards, comm_cards):
        available_cards = hole_cards + comm_cards
        possible_deck = list(combinations(available_cards, 5))




geg = RealTime_Hand_Evaluator()





# from Base_Hand_Evaluator import Base_Hand_Evaluator

# class Base_Hand_Evaluator:
#     def __init__(self, hole_cards, comm_cards):
#         self.hole_cards = hole_cards
#         self.comm_cards = comm_cards

#     def evaluate(self):

#         # Okay so the idea is that i work down the rankings of Poker and stop after i hit the first high card.
#         # This should lower the amount of checks i end up making at the very end

#         # Okay so apparently its not necessary to have a system like this when the total possible combination of cards is just 21
#         # So for human v human games, i can just compare every possible hand and rank it

#         # Then use python max function to find the one with the highest ranking

#         available_cards = self.hole_cards + self.comm_cards
#         possible_deck = list(combinations(available_cards, 5))
#         print(possible_deck)
#         print(len(possible_deck))

#     # itertools combinations lsit without replacement seems worth it

# eval = Hand_Evaluator(["4A", "5C"], ["KH", "KD", "KS", "1S","2C"])
# eval.evaluate()
