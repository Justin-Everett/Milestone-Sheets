import math

from Vector import Vector

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import random

WIDTH = 700
HEIGHT = 500
SIZE = int(math.sqrt((WIDTH^2)+(HEIGHT^2))/3)

class ball:
    def __init__(self,pos,velocity,radius,color):
        self.pos = pos
        self.velocity = velocity
        self.radius = radius
        self.color = color
        self.border = 1

    def update(self):
        self.pos.add(self.velocity)
        self.decreaseRad()

    def decreaseRad(self):
        if self.radius > 1:
            self.radius = self.radius-1

    def check(self):
        if (0 > self.pos.get_p()[0] > WIDTH) or (0 > self.pos.get_p()[1] > HEIGHT) or self.radius <= 1:
            return True
        return False

class paint:
    def __init__(self):
        self.balls = []
        self.remove = []

    def addBall(self):
        self.balls.append(ball(pos,velocity,radius,color))

    def draw(self,canvas):
        for b in self.balls:
            if b.check():
                self.balls.remove(b)

            canvas.draw_circle(b.pos.get_p(), b.radius, b.border, b.color, b.color)
            b.update()

def randCol():
    r = random.randrange (0, 256)
    g = random.randrange (0, 256)
    b = random.randrange (0, 256)
    return 'rgb('+str(r)+ ','+str(g)+ ','+str(b)+ ')'

def resetRands():
    global color
    global radius
    global randVelX
    global randVelY
    global velocity
    global pos
    color = randCol()
    radius = random.randrange(SIZE, SIZE * 5)
    randVelX = random.randrange(-SIZE, SIZE)
    randVelY = random.randrange(-SIZE, SIZE)
    velocity = Vector(randVelX, randVelY)
    pos = Vector(random.randrange(0,WIDTH), random.randrange(0,HEIGHT))

color = randCol()
radius = random.randrange(SIZE,SIZE*5)
randVelX = random.randrange(-SIZE,SIZE)
randVelY = random.randrange(-SIZE,SIZE)
velocity = Vector(randVelX,randVelY)
pos = Vector(WIDTH/2,HEIGHT/2)

def timer():
    global p
    resetRands()
    p.addBall()

p = paint()
timer = simplegui.create_timer(100,timer)
timer.start()
frame = simplegui.create_frame("Circles",WIDTH,HEIGHT)
frame.set_draw_handler(p.draw)
frame.start()