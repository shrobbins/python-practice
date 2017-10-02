# implementation of card game - Memory

#http://www.codeskulptor.org/#user43_8CFiXuZd0P_7.py

import simplegui
import random

# global variables
cards1 = [0,1,2,3,4,5,6,7]
cards2 = [0,1,2,3,4,5,6,7]
cards = []
cards.extend(cards1)
cards.extend(cards2)
card1 = -1
card2 = -1
card3 = -1
turns = 0



# helper function to initialize globals
def new_game():
    global state, exposed, turns
    state = 0
    exposed = [False]*16
    turns = 0
    random.shuffle(cards) 
    
        
# define event handlers
def mouseclick(pos):
    global exposed, state, card1, card2, card3, turns, flag
    # add game state logic here
    flag = False
    card_loc = pos[0] // 50
    for j in range(len(exposed)):
        if exposed[j] == True and j == card_loc:
            flag = True
    
    if flag == False:     
        if state == 0:
            for i in range(len(exposed)):
                if i == card_loc and exposed[i] == False:
                    exposed[i] = True
                    card1 = i
                    state = 1
        elif state == 1:
            for i in range(len(exposed)):
                if card3 >= 0:
                    card1 = card3
                    card3 = -1
                if i == card_loc and exposed[i] == False:
                        exposed[i] = True
                        card2 = i
                        turns +=1
                        state = 2;
        elif state == 2:
            for i in range(len(exposed)):
                if i == card_loc and exposed[i] == False:
                    exposed[i] = True
                    card3 = i 
                if cards[card1] != cards[card2]:
                    for i in range(len(exposed)):
                        if i == card1 or i == card2: 
                            exposed[i] = False          
                state = 1    
    
# cards are logically 50x100 pixels in size
def draw(canvas): 
    global cards, exposed, turns
    for card_index in range(len(cards)):
            card_pos = 50 * card_index
            canvas.draw_polygon([(card_pos, 0), (card_pos, 0 + 100),\
                                 (card_pos + 48, 0 + 100), (card_pos + 48, 0)], \
                                1, "SlateBlue","SlateBlue")
            
    for card_index in range(len(exposed)):
        if exposed[card_index] == True:
                card_pos = 50 * card_index
                canvas.draw_polygon([(card_pos, 0), (card_pos, 0 + 100),\
                                 (card_pos + 48, 0 + 100), (card_pos + 48, 0)], \
                                1, "Violet","Violet")
                canvas.draw_text(str(cards[card_index]), [card_pos + 15 , 54], \
                             24, "White") 
    label.set_text("turns = " + str(turns))
    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game, 150)
label = frame.add_label("turns = " + str(turns))


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()