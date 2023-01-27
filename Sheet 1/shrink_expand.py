try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

WIDTH = 700
HEIGHT = 500
loop = 0
RADIUS = 50
shrinking = True
def draw(canvas):

    global loop
    global shrinking
    global RADIUS
    loop+=1
    if loop % 2 == 0:
        loop = 0
        if RADIUS == 10:
            shrinking = False
        elif RADIUS == 50:
            shrinking = True

        if shrinking:
            RADIUS-=1
        else:
            RADIUS+=1
    canvas.draw_circle([WIDTH/2,HEIGHT/2], RADIUS, 1, 'Red','Red')
frame = simplegui.create_frame('Shrink Expand', WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.start()