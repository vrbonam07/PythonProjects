import random

# Here we are initiating our lists of suits and rand and a dict for give list of ranks
# We use this data elements to create a deck of playing cards which we are going to use for building the game.

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
playing = True

# we created a card class to define a format of how card shoud mbe like example "Ace of Spades, King of Diamonds"
class Card():
    
    def __init__(self,rank,suit):
        self.suit=suit
        self.rank=rank
    
    def __str__(self):
        return self.rank+" of "+self.suit

# Here using below Deck class we are going to creat a deck of cards
class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                # below we are creating a list of cards by append method used suit and rank lists
                self.deck.append(Card(rank,suit))
    
    def __str__(self):
        deck_comp ='' #defning am empty string 
        # take each card from the append list that we create above and create a str deck 
        for card in self.deck:
            deck_comp= deck_comp + '\n' + card.__str__()
        return "this deck has: "+deck_comp
            
        
    # This Method is used to shuffle the deck of cards
    def shuffle(self):
        #here we used suffle method from random package to shuffle the list that created above
        random.shuffle(self.deck)
        
    # This Method is ued to randomly select a card from the deck of cards 
    def deal(self):
        # Here single card is picked from the list and returned using pop method
        single_card= self.deck.pop()
        return single_card


# below hand class is used to issue a playinf hands to the player and dealer
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    # This method is used to add a card to the existing list of card of a hand
    def add_card(self,card):
        self.cards.append(card) # A card that is pulled from deck of cards is append to card here 
        # the rank value from the card is added to the value to get with sum
        self.value += values[card.rank]
    # This method is used to hadel Ace and adjust value of Ace (1 ot 11) based on the total value
    def adjust_for_ace(self):
        
        if self.value>21 and self.aces>0:
            self.value -= 10
            self.aces -= 1
# below class is to add or subtract winnings from total chips
class Chips:
    total=100
    def __init__(self):
        self.bet = 0
    # below method adds winnings to the total    
    def win_bet(self):
        Chips.total += self.bet
    # below method substracts winnings from the total
    def lose_bet(self):
        Chips.total -= self.bet
# Below Function is used to take bet amount as input to the code
def take_bet(Chips):
        
    while True:
        try:
            Chips.bet = int(input("Place your bet? "))
        except:
            print("Please enter bets in integer")
        else:
            if Chips.bet > Chips.total:
                print('Sorry not enough chips! you have {}'.format(Chips.total))
            else:
                break

# Below Function will pull a card from the deck and distributes it to Player or Dealer
def hit(deck,hand):
    
    single_card=deck.deal() # this line will go grab a card from the Deck
    hand.add_card(single_card) #this line adds thos card to players hand
    hand.adjust_for_ace() #this handel the Ace's in the total sum

#  Bellow Function i called when play want to hit for additional card or want to stay without any card  
def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        action=input("Hit or Stand, 'h' for hit and 's' for stand ")
        
        if action[0].lower() == 'h':
            hit(deck,hand)
        elif action.lower() == 's':
            print('player likes to stay now its delear turn')
            playing = False
        else:
            print("Invalid selection plese selet 'h' or 's'")
            continue
        break
     
# this Function is to show Delears one card face up and once card face down and players both cards face up.
def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
 
# This function will show all the cards face up delear and player   
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value) 
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

# this function substrats bet amount from the total when player busts
def player_busts(player,dealer,chips):
    print('Player Busted!')
    chips.lose_bet()
# this function adds bet amount to total when player wins
def player_wins(player,dealer,chips):
    print('Player Win!')
    chips.win_bet()
# this function adds bet amount to total when dealer busts
def dealer_busts(player,dealer,chips):
    print('Player Win Dealer Bustes!')
    chips.win_bet()
# this function substrats bet mount from the total when dealer wins.    
def dealer_wins(player,dealer,chips):
    print('Dealer Wins!')
    chips.lose_bet()
# this finction will be called when push occurs (i.e. dealer hand total and player hand total are same)
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")

# below peace of code will execute used all the Class, methods and functions that created above
# To Inisiate 2 cards each 2 for dealer and 2 for player are distributed.


while True:
    # Print an opening statement
    print("\n Welcome to the Blackjack Table, Let's Play!")
    
    # Create & shuffle the deck, deal two cards to each player
    
    deck = Deck()
    deck.shuffle()
        
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    # Set up the Player's chips
    
    player_chips = Chips()
    
    # Prompt the Player for their bet

    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    
    show_some(player_hand,dealer_hand)
    
    while playing: # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand)
                
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)
    
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
        
        # Show all cards
        show_all(player_hand, dealer_hand)
        
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
            
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
            
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
            
        else:
            push(player_hand,dealer_hand)
    
    # Inform Player of their chips total 
    print("\n the ayer Table, chips remaining are {}".format(player_chips.total))
    
    # Ask to play again
    play=input('like to play a new hand y/n? ')
    if play[0].lower()=='y':
        playing=True
        continue
    else:
        print('\n Thanks for playing!')
        break