import turtle as t
import random
tim = t.Turtle()
screen = tim.screen
colors = ["blue violet", "indian red", "midnight blue", "orange red", "green", "blue", "medium slate blue", "coral",
              "medium violet red"]


def random_move(ranangle, rancolor, tim):
    tim.width(20)
    tim.color(rancolor)
    tim.forward(50)
    tim.right(ranangle)


anglelist = [0 ,90, 180, 270]
for i in range(1000):
    angle = random.choice(anglelist)
    rancolor = random.choice(colors)
    random_move(angle, rancolor, tim)
    # if angle == angle2:
    # if angle == angle2:
    #     while angle == angle2:
    #         angle = random.choice(anglelist)
    #         rancolor = random.choice(colors)
    #         random_move(angle, rancolor, tim)
screen.onscreenclick



