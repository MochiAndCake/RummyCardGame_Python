# Name: Ann Soong
# Assignment number: 3

import random

def make_deck(num):
    '''(int)->list of int
        Returns a list of integers representing the strange deck with num ranks.

    >>> deck=make_deck(13)
    >>> deck
    [101, 201, 301, 401, 102, 202, 302, 402, 103, 203, 303, 403, 104, 204, 304, 404, 105, 205, 305, 405, 106, 206, 306, 406, 107, 207, 307, 407, 108, 208, 308, 408, 109, 209, 309, 409, 110, 210, 310, 410, 111, 211, 311, 411, 112, 212, 312, 412, 113, 213, 313, 413]

    >>> deck=make_deck(4)
    >>> deck
    [101, 201, 301, 401, 102, 202, 302, 402, 103, 203, 303, 403, 104, 204, 304, 404]
    
    '''
    deck = []
    for i in range(num): # This loop creates the ranks
        for j in range(4): # This loop creates the suits
            deck.append((j+1)*100 + (i+1))
    return deck



def shuffle_deck(deck):
    '''(list of int)->None
       Shuffles the given list of strings representing the playing deck

    Here you should use random.shuffle function from random module.
    
    Since shufflling is random, exceptionally in this function
    your output does not need to match that show in examples below:

    >>> deck=[101, 201, 301, 401, 102, 202, 302, 402, 103, 203, 303, 403, 104, 204, 304, 404]
    >>> shuffle_deck(deck)
    >>> deck
    [102, 101, 302, 104, 304, 103, 301, 403, 401, 404, 203, 204, 303, 202, 402, 201]
    >>> shuffle_deck(deck)
    >>> deck
    [402, 302, 303, 102, 104, 103, 203, 301, 401, 403, 204, 101, 304, 201, 404, 202]
    '''
    random.shuffle(deck) # Hmmm (- n - ) She did say to use it...

def deal_cards_start(deck):
    '''(list of int)-> list of int

    Returns a list representing the player's starting hand.
    It is  obtained by dealing the first 7 cards from the top of the deck.
    Precondition: len(dec)>=7
    '''
    hand = []
    for i in range(7): # The loop remove a card from the deck and adds a card to the player 7 times
        hand.append(deck.pop())
    return hand



def deal_new_cards(deck, player, num):
    '''(list of int, list of int, int)-> None
    Given the remaining deck, current player's hand and an integer num,
    the function deals num cards to the player from the top of the deck.
    If len(deck)<num then len(deck) cards is dealt, in particular
    all the remaining cards from the deck are dealt.

    Precondition: 1<=num<=6 deck and player are disjoint subsets of the strange deck. 
    
    >>> deck=[201, 303, 210, 407, 213, 313]
    >>> player=[302, 304, 404]
    >>> deal_new_cards(deck, player, 4)
    >>> player
    [302, 304, 404, 313, 213, 407, 210]
    >>> deck
    [201, 303]
    >>>

    >>> deck=[201, 303]
    >>> player=[302, 304, 404]
    >>> deal_new_cards(deck, player, 4)
    >>> player
    [302, 304, 404, 303, 201]
    >>> deck
    []
    '''
    j = num
    if len(deck) < num: # If the length of the deck is less than the dice number, the length of the deck is used instead
        j = len(deck)
        
    for i in range(j):
        player.append(deck.pop())

        


def print_deck_twice(hand):
    '''(list)->None
    Prints elements of a given list deck in two useful ways.
    First way: sorted by suit and then rank.
    Second way: sorted by rank.
    Precondition: hand is a subset of the strange deck.
    
    Your function should not change the order of elements in list hand.
    You should first make a copy of the list and then call sorting functions/methods.

    Example run:
    >>> a=[311, 409, 305, 104, 301, 204, 101, 306, 313, 202, 303, 410, 401, 105, 407, 408]
    >>> print_deck_twice(a)

    101 104 105 202 204 301 303 305 306 311 313 401 407 408 409 410 

    101 301 401 202 303 104 204 105 305 306 407 408 409 410 311 313 
    >>> a
    [311, 409, 305, 104, 301, 204, 101, 306, 313, 202, 303, 410, 401, 105, 407, 408]

    '''
    rank = hand[:]
    rank.sort()
    suit = []
    strrank = ''
    strsuit = ''

    if len(hand) >= 1: # If the list is empty, there is no point in sorting
    
        for i in range(len(rank)-1):
            strrank += str(rank[i]) + ' '
        strrank += str(rank[len(rank)-1])
        
        for i in range(len(hand)):
            suit.append(str(hand[i])[1:] + str(hand[i])[0])
        suit.sort()
        
        
        for i in range(len(suit)-1):
            strsuit += suit[i][2] + suit[i][0:2] + ' '
        strsuit += suit[len(suit)-1][2] + suit[len(suit)-1][0:2]
         
    print(strrank, end = "\n\n")
    print(strsuit)
        


def is_valid(cards, player):
    '''(list of int, list of int)->bool
    Function returns True if every card in cards is the player's hand.
    Otherwise it prints an error message and then returns False,
    as illustrated in the followinng example runs.

    Precondition: cards and player are subsets of the strange deck.
    
    >>> is_valid([210,310],[201, 201, 210, 302, 311])
    310 not in your hand. Invalid input
    False

    >>> is_valid([210,310],[201, 201, 210, 302, 310, 401])
    True
    '''
    for i in cards:
        if player.count(i) == 0: # If the card does not occur in the player's hand once, then it is invalid
            print(str(i) + " not in your hand. Invalid input")
            return False
    return True



def is_discardable_kind(cards):
    '''(list of int)->True
    Function returns True if cards form 2-, 3- or 4- of a kind of the strange deck.
    Otherwise it returns False. If there  is not enough cards for a meld it also prints  a message about it,
    as illustrated in the followinng example runs.
    
    Precondition: cards is a subset of the strange deck.

    In this function you CANNOT use strings except in calls to print function. 
    In particular, you cannot conver elements of cards to strings.
    
    >>> is_discardable_kind([207, 107, 407])
    True
    >>> is_discardable_kind([207, 107, 405, 305])
    False
    >>> is_discardable_kind([207])
    Invalid input. Discardable set needs to have at least 2 cards.
    False
    '''
    if len(cards) < 2:
        print("Invalid input. Discardable set needs to have at least 2 cards.")
        return False
    else:
        for i in range(1, len(cards)):
            if cards[i]%100 != cards[i-1]%100:
                return False
        return True
    


def is_discardable_seq(cards):
    '''(list of int)->True
    Function returns True if cards form progression of the strange deck.
    Otherwise it prints an error message and then returns False,
    as illustrated in the followinng example runs.
    Precondition: cards is a subset of the strange deck.

    In this function you CANNOT use strings except in calls to print function. 
    In particular, you cannot conver elements of cards to strings.

    >>> is_discardable_seq([313, 311, 312])
    True
    >>> is_discardable_seq([311, 312, 313, 414])
    Invalid sequence. Cards are not of same suit.
    False
    >>> is_discardable_seq([311,312,313,316])
    Invalid sequence. While the cards are of the same suit the ranks are not consecutive integers.
    False
    >>> is_discardable_seq([201, 202])
    Invalid sequence. Discardable sequence needs to have at least 3 cards.
    False
    >>> is_discardable_seq([])
    Invalid sequence. Discardable sequence needs to have at least 3 cards.
    False
    '''
    if len(cards) < 3:
        print("Invalid sequence. Discardable sequence needs to have at least 3 cards.")
        return False
    else:
        cards.sort()
        for i in range(1, len(cards)):
            if cards[i-1]+1 != cards[i]:
                if cards[i-1]//100 != cards[i]//100:
                    print("Invalid sequence. Cards are not of same suit.")
                else:
                    print("Invalid sequence. While the cards are of the same suit the ranks are not consecutive integers.")
                return False
        return True

    

def rolled_one_round(player):
    '''(list of int)->None
    This function plays the part when the player rolls 1
    Precondition: player is a subset of the strange deck

    >>> #example 1:
    >>> rolled_one_round(player)
    Discard any card of your choosing.
    Which card would you like to discard? 103
    103
    No such card in your hand. Try again.
    Which card would you like to discard? 102

    Here is your new hand printed in two ways:

    201 212 311 

    201 311 212

    rolled_one_round([311, 201, 212, 102])
    '''
    ans = False
    print("Discard any card of your choosing.")
    while ans == False:
        card = input("Which card would you like to discard? ").strip()
        if card.isdigit():
            removed = False
            i = 0
            while removed == False and i < len(player):
                if player[i] == int(card):
                    player.remove(player[i])
                    removed = True
                i += 1

            if removed:
                print("\nHere is your new hand printed in two ways:\n")
                print_deck_twice(player)
                ans = True
            else:
                print(card)
                print("No such card in your hand. Try again.")
        else:
            print(card)
            print("No such card in your hand. Try again.")

            

def rolled_nonone_round(player):
    '''(list of int)->None
    This function plays the part when the player rolls 2, 3, 4, 5, or 6.
    Precondition: player is a subset of the strange deck

    >>> #example 1:
    >>> player=[401, 102, 403, 104, 203]
    >>> rolled_nonone_round(player)
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? yes
    Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: 102 103 104
    103 not in your hand. Invalid input
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? yes
    Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: 403 203

    Here is your new hand printed in two ways:

    102 104 401 

    401 102 104 
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? no

    >>> #example 2:
    >>> player=[211, 412, 411, 103, 413]
    >>> rolled_nonone_round(player)
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? yes
    Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: 411 412 413

    Here is your new hand printed in two ways:

    103 211 

    103 211 
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? no

    >>> #example 3:
    >>> player=[211, 412, 411, 103, 413]
    >>> rolled_nonone_round(player)
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? yes
    Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: 411 412
    Invalid sequence. Discardable sequence needs to have at least 3 cards.

    >>> #example 4:
    >>> player=[401, 102, 403, 104, 203]
    >>> rolled_nonone_round(player)
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? alsj
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? hlakj
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? 22 33
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? no
    '''
    repeat = True
    while repeat:
        if len(player) > 0:
            ans = input("Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? ").strip().lower()
            if ans == 'no':
                repeat = False
            elif ans == 'yes':
                cards = input("Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: ").strip().split(' ')

                for i in range(len(cards)):
                    if cards[i].isdigit():
                        cards[i] = int(cards[i])
                
                if is_valid(cards, player):
                    if is_discardable_kind(cards) or is_discardable_seq(cards):
                        for i in range(len(cards)):
                            player.remove(cards[i])
                        print("\nHere is your new hand printed in two ways:\n")
                        print_deck_twice(player)
        else:
            repeat = False



# main
print("Welcome to Single Player Rummy with Dice and strange deck.\n")
size_change = input("The standard deck  has 52 cards: 13 ranks times 4 suits.\nWould you like to change the number of cards by changing the number of ranks? ").strip().lower()

if size_change == 'yes':
    repeat = True
    while repeat:
        num_ranks = input("Enter a number between 3 and 99, for the number of ranks: ").strip()
        if num_ranks.isdigit():
            if 3 <= int(num_ranks) <= 99:
                repeat = False
else:
    num_ranks = '13'

deck = make_deck(int(num_ranks))
shuffle_deck(deck)

print("You are playing with a deck of " + str(len(deck)) + " cards\nHere is your starting hand printed in two ways:\n")
player = deal_cards_start(deck)
print_deck_twice(player)

rounds = 0

while len(player) > 0: # Game ends when player is out of cards
    
    rounds += 1
    print("Welcome to round " + str(rounds) + ".")
    
    if len(deck) > 0:
        roll = random.randint(1,6)
    
        print("Please roll the dice.\nYou rolled the dice and it shows: " + str(roll))
        if roll == 1:
            rolled_one_round(player)
        else:
            print("Since your rolled, " + str(roll) + " the following " + str(roll) + " or " + str(len(deck)) + " (if the deck has less than " + str(roll) + " cards) will be added to your hand from the top of the deck.")
            deal_new_cards(deck, player, roll)
        
            print("\nHere is your new hand printed in two ways:\n")
            print_deck_twice(player)

            rolled_nonone_round(player)
    else:
        print("The game is in empty deck phase.")
        rolled_one_round(player)

    print("Round " + str(rounds) + " completed.")

print("Congratulations, you completed the game in " + str(rounds) + " rounds.")
