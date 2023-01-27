import math

from Vector import Vector

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# Some constants
WIDTH = 600
HEIGHT = 400

IMG = simplegui.load_image('http://www.cs.rhul.ac.uk/courses/CS1830/sprites/coach_wheel-512.png')
IMG_CENTRE = (256, 256)
IMG_DIMS = (512, 512)

STEP = 0


class Wheel:
    def __init__(self, pos, radius=10):
        self.pos = pos
        self.vel = Vector()
        self.radius = max(radius, 10)
        self.colour = 'White'
        self.pos2 = Vector(-self.radius, self.pos.get_p()[1])
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
            self.pos = Vector (self.leftEdge-WIDTH,self.pos.get_p()[1])
            self.pos2 = Vector(self.rightEdge-self.radius, self.pos.get_p()[1])
        #ball goes off screen to the left
        if self.leftEdge <= 0:
            self.pos = Vector(self.rightEdge+WIDTH, self.pos.get_p()[1])
            self.pos2 = Vector(self.leftEdge+self.radius, self.pos.get_p()[1])


        self.pos.add(self.vel)
        self.vel.multiply(0.85)

    def on_ground(self):
        if (self.pos.get_p()[1] >= HEIGHT-self.radius):
            return True
        return False


class Keyboard:
    def __init__(self):
        self.right = False
        self.left = False
        self.both = False
        self.space = False

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
        if key == simplegui.KEY_MAP['space']:
            self.space = True


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
        if key == simplegui.KEY_MAP['space']:
            self.space = False


class Interaction:
    def __init__(self, wheel, keyboard):
        self.wheel = wheel
        self.keyboard = keyboard

    def update(self):
        global STEP
        global circumfrence
        circumfrence = 2*math.pi*wheel.radius
        #Design choice: I chose to ignore the disallowage of right and left movement while in the air
        #because this was more fun
        if self.keyboard.right:
            self.wheel.vel.add(Vector(1, 0))
        if self.keyboard.left:
            self.wheel.vel.add(Vector(-1, 0))
        if self.wheel.on_ground():
            self.wheel.pos = Vector(self.wheel.pos.get_p()[0], HEIGHT-self.wheel.radius)
            self.wheel.vel = Vector(self.wheel.vel.get_p()[0],0)
            if self.keyboard.space:
                self.wheel.vel.add(Vector(0,-self.wheel.radius*(2/3)))

        else:
            self.wheel.vel.add(Vector(0, 2))
        if -math.pi <= wheel.vel.get_p()[0] <= math.pi:
            STEP = 0
        else:
            time = circumfrence / self.wheel.vel.get_p()[0]

            STEP = time/(720)



# Global variables
img_dest_dim = (128,128)
img_pos = [WIDTH/2, 2*HEIGHT/3.]
img_rot = 0

# Drawing handler
def draw(canvas):
    global img_rot
    img_rot += STEP
    wheel.colour = '#2C6A6A'
    inter.update()
    wheel.update()
    wheel.draw(canvas)
    canvas.draw_image(IMG, IMG_CENTRE, IMG_DIMS, wheel.pos.get_p(), img_dest_dim, img_rot)
    canvas.draw_image(IMG, IMG_CENTRE, IMG_DIMS, wheel.pos2.get_p(), img_dest_dim, img_rot)

kbd = Keyboard()
wheel = Wheel(Vector(WIDTH / 2, HEIGHT - 64), 64)
inter = Interaction(wheel, kbd)

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Bouncing Wheel Game", WIDTH, HEIGHT)
frame.set_canvas_background('#2C6A6A')
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.set_draw_handler(draw)


# Start the frame animation
frame.start()
