# implementation of card game - Memory
#Memory with images in a sinble line. 
#You can play and see the code at http://www.codeskulptor.org/#user41_CukfCV5dLY_1.py

import simplegui
import random

# images

d = {0:"http://www.clker.com/cliparts/Y/Q/a/m/E/8/flower-th.png",\
     1:"http://www.flowerclipart.com/flower_clipart_images/clipart_illustration_of_a_red_poppy_0071-0812-2317-0040_TN.jpg",\
     2:"http://ep.yimg.com/ay/yhst-83547458988818/solar-flower-pink-tulip-12.jpg",\
     3:"http://i00.i.aliimg.com/photo/v0/255140638/ARTIFICIAL_FLOWER_STEM.summ.jpg",\
     4:"http://img6a.flixcart.com/image/artificial-flower/u/g/r/5-head-peony-flower-5-fourwalls-0-100x100-imadzdhg4dwhc8hy.jpeg",\
     5:"http://www.clker.com/cliparts/d/3/f/6/13685576602026420623Pink%20Tulip.svg.thumb.png",\
     6:"http://www.clipartguide.com/_thumbs/1552-0908-0803-1843.jpg",\
     7:"http://www.clker.com/cliparts/v/N/G/v/A/a/flower-th.png"}
image_0 = simplegui.load_image(d[0])
image_1 = simplegui.load_image(d[1])
image_2 =simplegui.load_image(d[2])
image_3 =simplegui.load_image(d[3])
image_4 =simplegui.load_image(d[4])
image_5 =simplegui.load_image(d[5])
image_6 =simplegui.load_image(d[6])
image_7 =simplegui.load_image(d[7])
idx1 = 2*[image_0, image_1, image_2, image_3, image_4, image_5, image_6, image_7]
#idx2 = [image_0, image_1, image_2, image_3, image_4, image_5, image_6, image_7]
images = idx1

# helper function to initialize globals
def new_game():
    global x,z, face_up, matrix, state, text, polygon, post_cards, exposed, exposed_y, turn
    exposed = [False for i in range (16)] 
    matrix = {(0,0):0,(1,0):1,(2,0):2,(3,0):3,\
              (0,1):4,(1,1):5,(2,1):6,(3,1):7,\
              (0,2):8,(1,2):9,(2,2):10,(3,2):11,\
              (0,3):12,(1,3):13,(2,3):14,(3,3):15}
    state = 0
    face_up = []
    text = []
    turn = 0
    post_cards = []
    z = range (8) + range (8)
    random.shuffle(z)    
    random.shuffle(images)
    print z
    for n in z:
        tex = str(n)
        text.append(tex)

# define event handlers
def mouseclick(pos):
    global state, exposed, face_up, turn, matrix
    l = len (face_up)
    print "l",l
    if state == 0:       
        state = 1
        print "x,y=",[pos[0]//50,pos[1]//100]
        print pos       
        exposed [(matrix[pos[0]//50,pos[1]//100])] = True
        face_up.append(matrix[pos[0]//50,pos[1]//100])      
    elif state == 1:
        if not matrix[pos[0]//50,pos[1]//100] in face_up:
            state = 2
            exposed [(matrix[pos[0]//50,pos[1]//100])] = True
            face_up.append(matrix[pos[0]//50,pos[1]//100])
        print "len = ", l
        print "face_up[l-2]",face_up[l-2]
        print "face_up[l-1]",face_up[l-1]
        print "z[face_up[l-2]]",z [face_up[l-2]]
        print "z[face_up[l-1]]",z [face_up[l-1]]                        
    else:
        if not matrix[pos[0]//50,pos[1]//100] in face_up:
            turn += 1
            state = 1
            face_up.append(matrix[pos[0]//50,pos[1]//100])
            exposed [(matrix[pos[0]//50,pos[1]//100])] = True            
            if images[face_up[l-2]] != images [face_up[l-1]]:          
                exposed[face_up[l-2]] = False
                exposed[face_up[l-1]] = False
#                exposed [(matrix[pos[0]//50,pos[1]//100])] = True
                face_up.pop((l-1))
                face_up.pop((l-2))
#                face_up.append(matrix[pos[0]//50,pos[1]//100])	
#            elif images[face_up[l-2]] == images [face_up[l-1]]:
#
#                print "len = ", l
#                print "face_up[l-2]",face_up[l-2]
#                print "face_up[l-1]",face_up[l-1]
#                print "z[face_up[l-2]]",z [face_up[l-2]]
#                print "z[face_up[l-1]]",z [face_up[l-1]]            
    print "state", state    
    print "face_up",face_up
    print "exposed", exposed 
    print turn
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global exposed, turn, matrix
    i = 0   
    label.set_text("Turns = " + str(turn))
    for n in text:
        if len (face_up) != 16:
            i +=1
            if i >=0 and i <=4:
                center_dest_x = 25 + 800/16 *(i-1) 
                center_dest_y = 50
                canvas.draw_image(images[i-1], (25,50), (50,100), (center_dest_x, center_dest_y), (50,100))
            if i >=5 and i <=8:
                center_dest_x = -200 + 25 + 800/16 *(i-1) 
                center_dest_y = 150
                canvas.draw_image(images[i-1], (25,50), (50,100), (center_dest_x, center_dest_y), (50,100))
            if i >=9 and i <=12:
                center_dest_x = -400 + 25 + 800/16 *(i-1) 
                center_dest_y = 250
                canvas.draw_image(images[i-1], (25,50), (50,100), (center_dest_x, center_dest_y), (50,100))
            if i >=13 and i <=16:
                center_dest_x = -600 + 25 + 800/16 *(i-1) 
                center_dest_y = 350
                canvas.draw_image(images[i-1], (25,50), (50,100), (center_dest_x, center_dest_y), (50,100))
            
#            pos_r = 10 + 800/16 * (i - 1)                
#            canvas.draw_text(n, (pos_r, 70), 60, 'white')            
        else:
            canvas.draw_text("HURRAY!", (50, 200), 20, 'white')
            
    for i in range(16):
        if exposed[i]== False:
            if i >= 0 and i <=3:
                pos_rect = 25 + 800/16 * (i)
                polygon = [(pos_rect - 25,0), (pos_rect + 25,0), (pos_rect + 25,100),(pos_rect - 25,100)]
                canvas.draw_polygon(polygon, 1, "white", "green")
            if (i >= 4) and (i <=7):
                pos_rect = -200 + 25 + 800/16 * (i)
                polygon = [(pos_rect - 25,100), (pos_rect + 25,100), (pos_rect + 25,200),(pos_rect - 25,200)]
                canvas.draw_polygon(polygon, 1, "white", "green")
            if (i >= 8) and (i <=11):
                pos_rect = -400 + 25 + 800/16 * (i)
                polygon = [(pos_rect - 25,200), (pos_rect + 25,200), (pos_rect + 25,300),(pos_rect - 25,300)]
                canvas.draw_polygon(polygon, 1, "white", "green")                
            if (i >= 12) and (i <=15):
                pos_rect = -600 + 25 + 800/16 * (i)
                polygon = [(pos_rect - 25,300), (pos_rect + 25,300), (pos_rect + 25,400),(pos_rect - 25,400)]
                canvas.draw_polygon(polygon, 1, "white", "green")
#            else:
#                canvas.draw_polygon([(0,0),(0,0),(0,0),(0,0)], 1, "white", "green")
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 200, 400)
frame.add_button("Reset", new_game)
label = frame.add_label( "Turns = 0" )

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()