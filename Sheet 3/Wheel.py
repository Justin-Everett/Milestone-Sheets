from Vector import Vector

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

WIDTH = 500
HEIGHT = 500


class Wheel:
    def __init__(self, pos, radius=10):
        self.pos = pos
        self.vel = Vector()
        self.radius = max(radius, 10)
        self.colour = 'White'
        self.pos2 = Vector(-self.radius, HEIGHT-40)
        self.rightEdge = self.pos.get_p()[0] + self.radius
        self.leftEdge = self.pos.get_p()[0] - self.radius

    def draw(self, canvas):
        canvas.draw_circle(self.pos2.get_p(), self.radius, 1, self.colour, self.colour)
        canvas.draw_circle(self.pos.get_p(), self.radius, 1, self.colour, self.colour)

    def update(self):

        self.rightEdge = self.pos.get_p()[0] + self.radius
        self.leftEdge = self.pos.get_p()[0] - self.radius

        #ball goes off screen to the right
        if self.rightEdge >= WIDTH:
            self.pos = Vector (self.leftEdge-WIDTH,HEIGHT-40)
            self.pos2 = Vector(self.rightEdge-40, HEIGHT-40)
        #ball goes off screen to the left
        if self.leftEdge <= 0:
            self.pos = Vector(self.rightEdge+WIDTH, HEIGHT-40)
            self.pos2 = Vector(self.leftEdge+40, HEIGHT - 40)


        self.pos.add(self.vel)
        self.vel.multiply(0.85)


class Keyboard:
    def __init__(self):
        self.right = False
        self.left = False
        self.both = False

    def keyDown(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = True
        if key == simplegui.KEY_MAP['left']:
            self.left = True
        if key == simplegui.KEY_MAP['right'] and self.left:
            self.left = False
            self.right = True
            self.both = True
        if key == simplegui.KEY_MAP['left'] and self.right:
            self.right = False
            self.left = True
            self.both = True


    def keyUp(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = False
        if key == simplegui.KEY_MAP['left']:
            self.left = False
        if key == simplegui.KEY_MAP['right'] and self.both:
            self.right = False
            self.left = True
            self.both = False
        if key == simplegui.KEY_MAP['left'] and self.both:
            self.left = False
            self.right = True
            self.both = False


class Interaction:
    def __init__(self, wheel, keyboard):
        self.wheel = wheel
        self.keyboard = keyboard

    def update(self):
        if self.keyboard.right:
            self.wheel.vel.add(Vector(1, 0))
        if self.keyboard.left:
            self.wheel.vel.add(Vector(-1,0))


kbd = Keyboard()
wheel = Wheel(Vector(WIDTH / 2, HEIGHT - 40), 40)
inter = Interaction(wheel, kbd)


def draw(canvas):
    inter.update()
    wheel.update()
    wheel.draw(canvas)


frame = simplegui.create_frame('Interactions', WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.start()
