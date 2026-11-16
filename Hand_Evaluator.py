# for monte carlo, probably stick with this library called treys cuz its fast, if u actually have time at the end
# then make it urself
# recurring mention of asyncio and i also saw threading - look into this

from itertools import combinations

# treys for monte carlo, itertools for in game

class Hand_Evaluator:
    def __init__(self, hole_cards, comm_cards):
        self.hole_cards = hole_cards
        self.comm_cards = comm_cards

    def evaluate(self):

        # Okay so the idea is that i work down the rankings of Poker and stop after i hit the first high card.
        # This should lower the amount of checks i end up making at the very end

        # Okay so apparently its not necessary to have a system like this when the total possible combination of cards is just 21
        # So for human v human games, i can just compare every possible hand and rank it

        # Then use python max function to find the one with the highest ranking

        available_cards = self.hole_cards + self.comm_cards
        possible_deck = list(combinations(available_cards, 5))
        print(possible_deck)
        print(len(possible_deck))

    # itertools combinations lsit without replacement seems worth it

eval = Hand_Evaluator(["4A", "5C"], ["KH", "KD", "KS", "1S","2C"])
eval.evaluate()
