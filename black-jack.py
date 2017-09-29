# Mini-project #6 - Blackjack - Sue
#http://www.codeskulptor.org/#user43_KnyJpSNr5wc3imd.py

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
dealer_message = ""
score = 0
dealer_hand = []
player_hand = []
my_deck = []



# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
 
    
class Hand:
    def __init__(self):
        # create Hand object
        self.card_hand = []
    
    def string_list_join(self):
        string_list = ""
        for i in range(len(self.card_hand)):
            string_list += str(self.card_hand[i]) + " "
        return string_list

    def __str__(self):
            # return a string representation of a hand
            return "Card hand is " + str(self.string_list_join())

    def add_card(self, card):
            # add a card object to a hand
            self.card_hand.append(card)   

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
                
                values = []
                hand_value = 0
                total = 0
                for card in self.card_hand:
                    answer = Card.get_rank(card)
                    values.append(VALUES[answer])
                    total = sum(values)
                for i in values:
                    if i != 1:
                        hand_value = total
                    elif i == 1 and total + 10 <= 21:
                        hand_value = total + 10
                        return hand_value
                    else:
                        hand_value = total
                return hand_value
   
    def draw(self, canvas, pos):
            # draw a hand on the canvas, use the draw method for cards
            for card in self.card_hand:
                card.draw(canvas, pos)
                pos[0] += CARD_SIZE[0] + 5
  
 

# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object					
        self.deck = []
        for i in range(len(SUITS)):
            for j in range(len(RANKS)):
                single_card = Card(SUITS[i],RANKS[j])
                self.deck.append(single_card)
        return self.deck

    def shuffle(self):
        # shuffle the deck 
        shuffle_cards = random.shuffle(self.deck)
        return shuffle_cards
        

    def deal_card(self):
            # deal a card object from the deck
            dealt_card = self.deck.pop(-1)
            return dealt_card
         
            
    def deck_list_join(self):
        deck_list = ""
        for i in range(len(self.deck)):
            deck_list += str(self.deck[i]) + " "
        return deck_list
    
    def __str__(self):
        return "deck is " + str(self.deck_list_join())  



#define event handlers for buttons
def deal():
    global outcome, in_play, player_hand, dealer_hand, my_deck, dealer_message, score
    
      
    if in_play == True:
        dealer_message = "You canceled the game. You lose"
        outcome = "New deal?"
        score -= 1
        in_play = False
        return
        
    # create and shuffle deck
    
    my_deck = Deck()
    my_deck.shuffle()  
    
    player_hand = Hand()
    dealer_hand = Hand()
    
             
    dealer_hand.add_card(my_deck.deal_card())
    player_hand.add_card(my_deck.deal_card())
    dealer_hand.add_card(my_deck.deal_card())
    player_hand.add_card(my_deck.deal_card())    
    in_play = True
    outcome = "Hit or Stand?"
    dealer_message = ""
    
    

def hit():
        global  player_hand, my_deck, outcome, dealer_message, in_play, score
         # if the hand is in play, hit the player
        if player_hand.get_value() < 21: 
            player_hand.add_card(my_deck.deal_card())
            
            
        # if busted, assign a message to outcome, update in_play and score 
        if player_hand.get_value() > 21:
                in_play = False
                dealer_message = "You have busted. You lose."
                outcome = "New deal?"
                score -= 1
       
               
       
def stand():
        # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
        global  dealer_hand, player_hand, my_deck, dealer_message, outcome, in_play, score
        
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(my_deck.deal_card()) 
              
            
            
    # assign a message to outcome, update in_play and score
        if dealer_hand.get_value() <= 21 and dealer_hand.get_value() >= player_hand.get_value():
                dealer_message = "You lose"
                outcome = "New deal?"
                in_play = False
                score -= 1
                
        elif dealer_hand.get_value() > 21:
            in_play = False
            dealer_message = "Dealer busted. You win!"
            outcome = "New deal?"
            score += 1
            
        else:
            dealer_message = "You win!"
            outcome = "New deal?"
            in_play = False
            score += 1
            
                
# draw handler    
def draw(canvas):
    global player_hand, dealer_hand, outcome, in_play
    # test to make sure that card.draw works, replace 
    # with your code below
    dealer_hand.draw(canvas, [50, 130])
    player_hand.draw(canvas, [50, 320])
    
    #draw text
    canvas.draw_text('Blackjack', (50, 40), 28, 'GreenYellow')
    canvas.draw_text('Dealer', (50, 110), 24, 'Cyan')
    canvas.draw_text('Player', (50, 300), 24, 'Cyan')
    canvas.draw_text(outcome, (200, 300), 24, 'Black')
    canvas.draw_text(dealer_message, (200, 110), 24, 'Black')
    canvas.draw_text("Score: " + str(score), (400, 70), 24, 'White')
               
    #draw hole image
    if in_play == True:
        canvas.draw_image(card_back, (72 / 2, 96 / 2), CARD_BACK_SIZE, (85, 179), CARD_BACK_SIZE)
        
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()