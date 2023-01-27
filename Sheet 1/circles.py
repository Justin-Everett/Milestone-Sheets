import random

try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


WIDTH = 700
HEIGHT = 500

loop = 0

def randCol ():
    r = random.randrange (0, 256)
    g = random.randrange (0, 256)
    b = random.randrange (0, 256)
    return 'rgb('+str(r)+ ','+str(g)+ ','+str(b)+ ')'

COL1 = randCol()
COL2 = randCol()
COL3 = randCol()
COL4 = randCol()
def draw(canvas):
    global loop
    loop+=1
    global COL1
    global COL2
    global COL3
    global COL4
    if loop%60 == 0:
        loop = 0
        COL1 = randCol()
        COL2 = randCol()
        COL3 = randCol()
        COL4 = randCol()

    RADIUS = 100
    canvas.draw_circle([WIDTH/ 2 - (RADIUS / 2) , HEIGHT / 2], RADIUS, 4, COL1,COL2)
    canvas.draw_circle([WIDTH/2+(RADIUS/2),HEIGHT/2],RADIUS,4, COL3,COL4)

frame = simplegui.create_frame("Circles",WIDTH,HEIGHT)
frame.set_draw_handler(draw)
frame.start()