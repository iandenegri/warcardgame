#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    Create deck
    Shuffle deck
    Split deck in half
    return deck 1 and deck 2
    """
    def __init__ (self):
        self.allcards = [(s,r) for s in SUITE for r in RANKS]

    def shuffle (self):
        print("Deck is being shuffled...")
        shuffle(self.allcards)

    def split_deck(self):
        deck1 = self.allcards[:26]
        deck2 = self.allcards[26:]
        # return a tuple of the split cards.
        return(deck1,deck2)


class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self,cards):
        self.cards = cards

    def __str__(self):
        return ("Contains" + len(self.cards) + "cards.")

    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()


class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self,name,hand):
        self.name = name
        self.hand = hand


    def play_card(self):
        drawn_card = self.hand.remove_card()
        print(str(self.name) + " has placed" + str(drawn_card))
        print('\n')
        return drawn_card


    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards


    def still_has_cards(self):
        """
        returns true if player still has cards
        """
        return len(self.hand.cards) != 0



######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

# Use the 3 classes along with some logic to play a game of war!


# Create new deck and split in half.
d = Deck()
d.shuffle()
half1,half2 = d.split_deck()

comp = Player("Computer", Hand(half1))

p_name = input("What is your name?")

user = Player(p_name, Hand(half2))

total_rounds = 0
war_count = 0

while user.still_has_cards() and comp.still_has_cards():
    total_rounds += 1
    print ("Starting next round")
    print('Here are the current standings:')
    print("Total rounds played: " + str(total_rounds))
    print("Total wars occured: " + str(war_count))
    print(user.name + " has this many cards: " + str(len(user.hand.cards)))
    print(comp.name + " has this many cards: " + str(len(comp.hand.cards)))
    print('Play your card!')
    print('\n')


    table_cards = []

    cpu_card = comp.play_card()
    player_card = user.play_card()

    table_cards.append(cpu_card)
    table_cards.append(player_card)

    if cpu_card[1] == player_card[1]:
        war_count += 1

        print('WAR MATEYS')

        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        if RANKS.index(cpu_card[1]) < RANKS.index(player_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

    else:
        if RANKS.index(cpu_card[1]) < RANKS.index(player_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

print('Game over! Number of rounds: ' + str(total_rounds))
print('Total number of wars: ' + str(war_count))
if len(user.hand.cards) > 50:
    print('You win :-D')
else:
    print('You lose.')
