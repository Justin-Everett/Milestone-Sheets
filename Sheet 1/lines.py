try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

WIDTH = 700
HEIGHT = 500
x = 0
y=0
def draw(canvas):
    LINE_WIDTH = 40
    global x
    global y
    x+=1
    if x==WIDTH+LINE_WIDTH/2:
        x=2
        y=0
    elif x+20>=WIDTH:
        y+=1
        canvas.draw_line([0,0],[0,HEIGHT], y, 'Red')

    canvas.draw_line([x,0],[x,HEIGHT],LINE_WIDTH,'Red')
    canvas.draw_line([0,0],[WIDTH,HEIGHT],2, 'Red')
    canvas.draw_line([0, HEIGHT], [WIDTH, 0], 2, 'Red')

frame = simplegui.create_frame("Lines",WIDTH,HEIGHT)
frame.set_draw_handler(draw)

frame.start()