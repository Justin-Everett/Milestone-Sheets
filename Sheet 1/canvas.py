try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

def randCol ():
    r = random.randrange (0, 256)
    g = random.randrange (0, 256)
    b = random.randrange (0, 256)
    return 'rgb('+str(r)+ ','+str(g)+ ','+str(b)+ ')'

# Drawing handler :
# this function is called 60 times per second
loop = 0
def draw(canvas):
    global loop
    loop += 1
    if (loop % 60 == 0):
        frame.set_canvas_background(randCol())
        loop = 0

# Create a frame and assign the callback to the event handler
frame = simplegui.create_frame(" Colours ", 400 , 200)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
