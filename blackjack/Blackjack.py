# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

pos_player = [72,400]
pos_dealer = [72,150]

# initialize some useful global variables
in_play = False
outcome = ""
score_player = 0
score_dealer = 0

# define globals for cards

SUITS = ['C', 'S', 'H', 'D']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
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
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.cards = []

    def __str__(self):
        # return a string representation of a hand
        ans = ""
        for i in range(len(self.cards)):
            ans += " " + str(self.cards[i])
        return "Hand contains " + ans

    def add_card(self, card):
        # add a card object to a hand
        self.cards.append(card)

    def get_value(self):
        v = 0
        aces = 0
        for s in self.cards:
            if VALUES[(s.get_rank())] !=1:
                v += VALUES[(s.get_rank())]
#                print "value no aces",v #
#                print "loop" #
            else: 
                if (v + VALUES[(s.get_rank())] + 10) <= 21:
                    print v + VALUES[(s.get_rank())] + 10
                    aces += 1
#                    print "aces", aces #
                    v +=  VALUES[(s.get_rank())] + 10
#                    print "final value if 1 aces", v   #                                     
#                    print "loop" #
                else: 
                    aces += 1
#                    print "aces", aces #
                    v += VALUES[(s.get_rank())] 
#                    print "value if busted", v  #
#                    print "loop" #                                    
        return  v
        print "value", v
        print "" #
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for c in self.cards:
            i = self.cards.index(c)
            c.draw (canvas,(pos[0]*i + 70,pos[1]))
                           
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for s in SUITS: 
            for r in RANKS:
#                self.deck.append([s,r])
               self.deck.append(Card(str(s),str(r)))
    # create a Card object using Card(suit, rank) 
    # and add it to the card list for the deck
    
    def shuffle(self):
        # shuffle the deck 
        return random.shuffle(self.deck)

    def deal_card(self):
        # deal a card object from the deck
        return self.deck.pop(len (self.deck)-1)        
    
    def __str__(self):
            # return a string representing the deck
        ans = ""
        for i in range(len(self.deck)):
            ans += " " + str(self.deck[i])
        return "Deck contains " + ans

#define event handlers for buttons
def deal():
    
    global outcome, in_play, deck, game_deck, player_hand, dealer_hand, score_dealer
    if in_play: 
        score_dealer +=1
    in_play = True    
    outcome = ""
    game_deck = Deck()
    game_deck.shuffle()
    print game_deck #
    player_hand = Hand()
    dealer_hand = Hand()
    player_hand.add_card(game_deck.deal_card()) 
    player_hand.add_card(game_deck.deal_card()) 
    print "player", player_hand  #
    print player_hand.get_value() #
    dealer_hand.add_card(game_deck.deal_card())
    dealer_hand.add_card(game_deck.deal_card()) 
    print "dealer",  dealer_hand  #
    print dealer_hand.get_value() #

    
def hit():
    global in_play, score_dealer, score_player, outcome
    if player_hand.get_value() <= 21 and (in_play == True):
        player_hand.add_card(game_deck.deal_card())
        
        if player_hand.get_value() > 21:
            outcome = "You have busted. Another deal?"
            in_play = False
            score_dealer += 1
    else:
        message = "You've already busted!. Another deal?"    
    
    print "player_hand_value", player_hand.get_value() #
    print "player",  player_hand  #
    print "dealer_hand_value", dealer_hand.get_value() #
    print "dealer",  dealer_hand  # 
    print ""
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global in_play, score_dealer, score_player, player_hand, dealer_hand, outcome
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    if player_hand.get_value() > 21:
        outcome = "Hey!, your are busted! another deal?"
        in_play = False
    if in_play:
            while dealer_hand.get_value() <=17:
                    dealer_hand.add_card(game_deck.deal_card())
            if dealer_hand.get_value() <=21:
                if dealer_hand.get_value() >= player_hand.get_value():

                        outcome = "Dealer wins, New deal?"                   
                        in_play = False
                        score_dealer += 1
                else:
                        outcome = "Player wins, New deal?"

                        in_play = False
                        score_player += 1
            else:
                    score_player += 1
                    outcome = "Dealer is busted!, Player wins" 
                    in_play = False

                       
    print "player value", player_hand.get_value() #
    print dealer_hand.get_value() # 
    print "player", player_hand  #
    print "dealer", dealer_hand  #
    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    global outcome
    
    player_hand.draw(canvas,pos_player)
    dealer_hand.draw(canvas,pos_dealer)
    if in_play: 
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_SIZE, (pos_dealer[0]*1.46,pos_dealer[1]*1.32), CARD_SIZE)
    canvas.draw_text("Dealer", [72,90], 28, "Black")
    canvas.draw_text("Player", [72,340], 28, "Black")
    canvas.draw_text((str (outcome)), [72,380], 28, "Yellow")
    canvas.draw_text("Blackjack", [72,50], 30, "Yellow")
    canvas.draw_text( ("Score Player = " + str(score_player)), [300,340], 28, "Black")
    canvas.draw_text( ("Score Dealer = " + str(score_dealer)), [300,90], 28, "Black")


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


# remember to review the gradic rubric