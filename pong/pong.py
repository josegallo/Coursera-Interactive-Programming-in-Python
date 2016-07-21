# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [1, 1]
paddle1_pos = HEIGHT / 2
paddle2_pos = HEIGHT / 2
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0
winner1 = ""
winner2 = ""
direction = RIGHT

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]    
    if RIGHT:
        ball_vel[0] = random.randrange(2, 4)
        ball_vel[1] = - random.randrange(1, 3)
    else:
        ball_vel[0] = - random.randrange(2, 4)
        ball_vel[1] = - random.randrange(1, 3)
        
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, LEFT, RIGHT, direction  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(direction)
    score1 = 0
    score2 = 0

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, LEFT, RIGHT, paddle1_vel, paddle2_vel, winner1, winner2 
 
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # Update ball position
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # collide and reflect off of left hand side of canvas
    if ball_pos[0] >= (WIDTH-(PAD_WIDTH)-BALL_RADIUS):
        if abs (ball_pos[1] - paddle2_pos) < PAD_HEIGHT / 2: 
            ball_vel[0] = - 1.1 * ball_vel[0]                                          
        else: 
            ball_vel[0] = - ball_vel[0]
            LEFT
            spawn_ball(LEFT)
            if score2 <=3:
                score2 +=1
            else:
                score2 = score2 + 1
                winner1 = "Winner!"
                ball_vel = [0, 0]
    if ball_pos[0] <= (BALL_RADIUS+(PAD_WIDTH)):
        if abs (ball_pos[1] - paddle1_pos) < PAD_HEIGHT / 2: 
            ball_vel[0] = - 1.1 * ball_vel[0]
        else: 
            RIGHT
            spawn_ball(RIGHT)
            ball_vel[0] = - ball_vel[0]
            if score1 <=3:
                score1 +=1
            else:
                score1 = score1 +1
                winner2 = "Winner!"
                ball_vel = [0, 0]
    if ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]
    if ball_pos[1] <= (BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]            

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    
    # draw paddles
    canvas.draw_polygon([(0, paddle1_pos - 40),(8, paddle1_pos - 40), (8, paddle1_pos + 40), (0, paddle1_pos + 40)], 1, "white", "white")
    canvas.draw_polygon([(WIDTH - 8, paddle2_pos - 40),(WIDTH , paddle2_pos - 40), (WIDTH , paddle2_pos + 40),(WIDTH - 8, paddle2_pos + 40)], 1, "white", "white")    
    
    # determine whether paddle and ball collide    
    if paddle1_pos >= (HEIGHT-40):
        paddle1_vel = 0
        paddle1_pos = (HEIGHT-40)
    if paddle1_pos <= (40):
        paddle1_vel = 0
        paddle1_pos = 40
    if paddle2_pos >= (HEIGHT-40):
        paddle2_vel = 0
        paddle2_pos = (HEIGHT-40)
    if paddle2_pos <= (40):
        paddle2_vel = 0
        paddle2_pos = 40

    # draw scores
    canvas.draw_text(str(score1), (400, 20), 24, 'White')
    canvas.draw_text(winner2, (370, 40), 24, 'White')
    canvas.draw_text(str(score2), (200, 20), 24, 'white')
    canvas.draw_text(winner1, (170, 40), 24, 'White')
    
def keydown(key):
    global paddle1_vel, paddle2_vel, vel
    vel = 10
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = + vel 
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel = - vel
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = - vel  
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = + vel  
      
def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel = 0
    paddle2_vel = 0
    
def button_handler():
    global spawn_ball, direction, winner1, winner2, LEFT, RIGHT
    winner1 = ""
    winner2 = ""
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button1 = frame.add_button('Restart', button_handler, 50)

# start frame
new_game()
frame.start()
