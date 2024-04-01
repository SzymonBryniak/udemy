import turtle as t
import random

tim = t.Turtle()
screen = tim.screen
screen.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = r, g, b
    return rgb

for i in range(10000):
    t.setheading(i*10)
    t.circle(50)
    t.color(random_color())

