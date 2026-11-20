# for monte carlo, probably stick with this library called treys cuz its fast, if u actually have time at the end
# then make it urself
# recurring mention of asyncio and i also saw threading - look into this
from abc import ABC, abstractmethod


# treys for monte carlo, itertools for in game

class Base_Hand_Evaluator(ABC):

    rank_to_rt = {
        2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, "J":11, "Q":12, "K":13, "A":14
    }

    rank_to_treys = {
        2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"10", "J":"J", "Q":"Q", "K":"K", "A":"A"
    }

    suit_to_treys = {
        "Spades": "s", "Hearts": "h", "Diamonds": "d", "Clubs": "c"
    }

    @abstractmethod
    def evaluate_hand(self, hole_cards, comm_cards):
        pass
    
    # i choose not to add a find winner subroutine within this class because i intend to make a separate function for that somewhere - maybe
