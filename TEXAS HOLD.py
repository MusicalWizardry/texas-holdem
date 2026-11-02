import random
import secrets

# add whatever python socket programming is

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

class Table:
    def __init__(self, pot=0, community_cards = None):
        self.pot = pot
        self.community_cards = community_cards if community_cards is not None else []

def init_deck():
    suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    hierarchy = {}
    for i in range(len(ranks)):
        if ranks[i].isnumeric():
            hierarchy[ranks[i]] = int(ranks[i])
        else:
            if ranks[i] == "A":
                hierarchy[ranks[i]] = (1, 14)
            elif ranks[i] == "J":
                hierarchy[ranks[i]] = 11
            elif ranks[i] == "Q":
                hierarchy[ranks[i]] = 12
            elif ranks[i] == "K":
                hierarchy[ranks[i]] = 13
    print(hierarchy)
    Deck = []
    for i in range(len(suits)):
        for j in range(len(ranks)):
            Deck.append(Card(suits[i], ranks[j]))
    print(Deck)
    #for i in range(len(Deck)):
     #   print(Deck[i].suit, Deck[i].rank)

    return Deck


# the actual game

# blinds
S_BLIND = 1
B_BLIND = 2
BUY_IN = 100 * B_BLIND  # this will probably be useless

table = Table()

class Player:
    def __init__(self, id, deck=None, stack=BUY_IN, current_bet=None, folded = False, dealer = False):
        self.id = id
        self.deck = deck if not deck is None else []
        self.stack = stack
        self.current_bet = current_bet
        self.folded = folded
        self.dealer = dealer

def start():
    global player_list, Deck, removed_cards
    Deck = init_deck()
    removed_cards = []
    playerNum = int(input("how many players"))
    player_list = []
    for i in range(playerNum):
        player_list.append(Player(i + 1))

#for plays ist like index%len(playerlist)
def blinds():
    table = 5
    global table
    dealerIx = secrets.choice(range(0, len(player_list)))
    player_list[dealerIx].dealer = True
    sBlindGiver = player_list[(dealerIx+1)%len(player_list)]
    bBlindGiver = player_list[(dealerIx+2)%len(player_list)]

    table.pot += S_BLIND
    sBlindGiver.stack -= S_BLIND
    table.pot += B_BLIND
    bBlindGiver.stack -= B_BLIND

    for player in player_list:
        print(f"\n{player.id}: {player.stack}")
    print(table.pot)
    return dealerIx
    #blinds complete - make sure u set blinds to true in main program

# happens after blinds
def pre_flop():
    for i in range(len(player_list)):
        deal(2, i)
    for player in player_list:
        for i in range(len(player.deck)):
            print(f"{player.id}: {player.deck[i].rank}, {player.deck[i].suit}")


def deal(noOfCards, playerIx):
    print(f"this is for player {playerIx}")
    q_deck = []
    for i in range(noOfCards):
        print("i have been called")
        cardIx = secrets.choice(range(0, len(Deck)))
        q_deck.append(Deck[cardIx])
        removed_cards.append(Deck[cardIx])
        Deck.pop(cardIx)
    for card in q_deck:
        print(f"{card.rank} {card.suit}")
    player_list[playerIx].deck.extend(q_deck)

def call():
    pass

def raze(highest_bet, currentPlayerIx):
    raise_to = int(input("What would you like to raise to: "))
    player_list[currentPlayerIx].current_bet = current_bet+raise_to
    player_list[currentPlayerIx].stack -= raise_to

def fold():
    pass

def check():
    pass

def turn_loop(dealerIx, currentPlayerIx):
    highest_bet = max(player_list, key = lambda player: player.current_bet)
    currentPlayerIx = (currentPlayerIx + 1)%len(player_list)
    decision = int(input("What would you like to do (1: raise, 2: call, 3:check, 4: fold): "))
    if decision == 1:
        raze(highest_bet, currentPlayerIx)
    elif decision == 2:
        call()
    elif decision == 3:
        check()
    else:
        fold()

def main():
    # stages
    BLINDS = False
    PRE_FLOP = False
    FLOP = False
    TURN = False
    RIVER = False
    SHOWDOWN = False

    start()
    # ------~{[=BLINDS=]}~------ #
    dealerIx = blinds()
    BLINDS = True
    # ------~{[=PRE_FLOP=]}~------ #
    pre_flop()
    PRE_FLOP = True
    # ------~{[=TURN_LOOP=]}~------ #
    #probably need a for loop so that each player gets a turn
    turn_loop(dealerIx, player_list[(dealerIx+2)%len(player_list)])#parameter two is big blind giver

main()