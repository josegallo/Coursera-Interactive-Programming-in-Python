import simplegui

# global variables:

count = 0
hits = 0
attemps = 0
timer_runs = False

# helper variables: 

def secs (u): 
    secs = (u//10)% 60
    if secs <10:
        return "0" + str (secs)
    else: 
        return str (secs)
    
def min (u): 
    min = (u/10)//60
    return str (min)

def format(u):
    global tenths
    tenths = u% 10
    return min (u) + ":" + secs(u) + "." + str (tenths)

# Event Handlers: 

def timer_handler(): 
    global count
    count +=1

def click_start():
    global timer_runs
    timer_runs = True
    timer.start()
    
def click_stop():
    timer.stop()
    global tenths, attemps, hits, timer_runs
    if timer_runs and tenths == 0:
        hits +=1
        attemps +=1
        timer_runs = False
    elif timer_runs: 
        attemps +=1
        timer_runs = False
    
def click_reset():
    global count, timer_runs, attemps, hits
    count = 0
    hits = 0
    attemps = 0
    timer_runs = False
    timer.stop()
    
def draw(canvas):
    canvas.draw_text(format(count), [100,112], 48, "White")
    canvas.draw_text((str (hits)+ "/"+str (attemps)), [250,20], 24, "Green")
    
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)

# Register handlers
frame.add_button("Start", click_start,100)
frame.add_button("Stop", click_stop,100)
frame.add_button("Reset", click_reset,100)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, timer_handler)


# Start the frame animation
frame.start()
timer.stop()
