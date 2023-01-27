import math

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Vector import Vector


class Ball:

    def __init__(self, position, radius, border):
        self.pos = position
        self.radius = radius
        self.border = border
        self.color = 'Red'
        self.velocity = Vector(0, 0)

    def draw(self, canvas):
        print(self.pos.get_p())
        canvas.draw_circle(self.pos.get_p(), self.radius, self.border, self.color, self.color)
        self.update()

    def vanish(self):
        self.color = 'Black'

    def get_pos(self):
        return self.pos.get_p()

    def set_pos(self, pos):
        self.pos = Vector(pos)

    def set_velocity(self, x, y):
        self.velocity = Vector(x, y)

    def update(self):
        self.pos.add(self.velocity)


class Mouse:
    def __init__(self):
        self.pos = None

    def click_handler(self, pos):
        self.pos = pos

    def click_pos(self):
        click = self.pos
        self.pos = None
        return click


class Interaction:
    def __init__(self, ball, mouse):
        self.ball = ball
        self.mouse = mouse

    def draw(self, canvas):
        self.ball.draw(canvas)
        click = self.mouse.click_pos()
        if click is not None:
            self.check_pos(click, self.ball.get_pos(), self.ball)

    def check_pos(self, mousePos, ballPos, ball):
        x = mousePos[0] - ballPos[0]
        y = mousePos[1] - ballPos[1]
        center_distance = math.sqrt(x * x + y * y)
        if center_distance <= ball.radius + ball.border:
            ball.set_velocity(x / 5, y / 5)
        else:
            ball.set_velocity(0, 0)


WIDTH = 700
HEIGHT = 500

pos = Vector(WIDTH / 2, HEIGHT / 2)

b = Ball(pos, 40, 1)
m = Mouse()
i = Interaction(b, m)

frame = simplegui.create_frame('Click', WIDTH, HEIGHT)
frame.set_mouseclick_handler(m.click_handler)
frame.set_draw_handler(i.draw)
frame.start()
