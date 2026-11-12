# for monte carlo, probably stick with this library called treys cuz its fast, if u actually have time at the end
# then make it urself 
# recurring mention of asyncio and i also saw threading - look into this

class Hand_Evaluator:
    def __init__(self, hole_cards, comm_cards):
    
    # Okay so the idea is that i work down the rankings of Poker and stop after i hit the first high card.
    # This should lower the amount of checks i end up making at the very end

    # Okay so apparently its not necessary to have a system like this when the total possible combination of cards is just 21
    # So for human v human games, i can just compare every possible hand and rank it

    # Then use python max function to find the one with the highest ranking

    available_cards = hole_cards + comm_cards

    #itertools combinations lsit without replacement seems worth it
