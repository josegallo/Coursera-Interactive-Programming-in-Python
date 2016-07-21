# implementation of card game - Memory
# you can see the code and pleay at http://www.codeskulptor.org/#user41_qj4hntvvho_0.py

import simplegui
import random

# helper function to initialize globals
def new_game():
    global x,z, face_up,state, text, polygon, post_cards, exposed, turn
    exposed = [False for i in range (16)]
    state = 0
    face_up = []
    text = []
    turn = 0
    post_cards = []
    z = range (8) + range (8)
    random.shuffle(z)
    print z
    for n in z:
        tex = str(n)
        text.append(tex)

# define event handlers
def mouseclick(pos):
    global state, exposed, face_up, turn
    l = len (face_up)
    print "l",l
    if state == 0:       
        state = 1
        exposed [pos[0]//50] = True
        face_up.append(pos[0]//50)
    elif state == 1:
        if ((pos[0]//50) in face_up) == False:
            state = 2
            exposed [pos[0]//50] = True
            face_up.append(pos[0]//50)
        print "len = ", l
        print "face_up[l-2]",face_up[l-2]
        print "face_up[l-1]",face_up[l-1]
        print "z[face_up[l-2]]",z [face_up[l-2]]
        print "z[face_up[l-1]]",z [face_up[l-1]]                        
    else:
        if ((pos[0]//50) in face_up) == False:
            turn += 1
            state = 1
            if z[face_up[l-2]] != z [face_up[l-1]]:          
                exposed[face_up[l-2]] = False
                exposed[face_up[l-1]] = False
                exposed [pos[0]//50] = True
                face_up.append(pos[0]//50)
                face_up.pop((l-1))
                face_up.pop((l-2))
            elif z[face_up[l-2]] == z [face_up[l-1]]:
                face_up.append(pos[0]//50)
                exposed [pos[0]//50] = True
                print "len = ", l
                print "face_up[l-2]",face_up[l-2]
                print "face_up[l-1]",face_up[l-1]
                print "z[face_up[l-2]]",z [face_up[l-2]]
                print "z[face_up[l-1]]",z [face_up[l-1]]
            
    print "state", state    
    print "face_up",face_up
    print "exposed", exposed 
    print turn
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global exposed, turn
    i = 0   
    label.set_text("Turns = " + str(turn))
    for n in text:
        if len (face_up) != 16:
            i +=1
            pos_r = 10 + 800/16 * (i - 1)
            canvas.draw_text(n, (pos_r, 70), 60, 'white')            
        else:
            canvas.draw_text("HURRAY!", (275, 70), 60, 'white')
            
    for i in range(16):
        if exposed[i]== False:
            pos_rect = 25 + 800/16 * (i)
            polygon = [(pos_rect - 25,0), (pos_rect + 25,0), (pos_rect + 25,100),(pos_rect - 25,100)]
            canvas.draw_polygon(polygon, 1, "white", "green")
        else:
            canvas.draw_polygon([(0,0),(0,0),(0,0),(0,0)], 1, "white", "green")
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label( "Turns = 0" )

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)


# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
