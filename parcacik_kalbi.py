"""Pink particle heart based on the readable Turtle code in the reference reel."""
import math as m
import random as r
import time
import turtle as t


screen = t.Screen()
screen.setup(700, 700)
screen.bgcolor("black")
screen.colormode(1.0)
screen.tracer(0, 0)

pen = t.Turtle(visible=False)
pen.speed(0)
pen.penup()


def heart(angle, scale):
    x = 16 * m.sin(angle) ** 3 * scale
    y = (
        13 * m.cos(angle)
        - 5 * m.cos(2 * angle)
        - 2 * m.cos(3 * angle)
        - m.cos(4 * angle)
    ) * scale
    return x, y


def draw_streak(x, y, length, green, blue, min_width, max_width):
    angle = m.atan2(y, x)
    pen.pencolor(r.uniform(0.78, 1.0), r.uniform(*green), r.uniform(*blue))
    pen.width(r.uniform(min_width, max_width))
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.goto(x + m.cos(angle) * length, y + m.sin(angle) * length)
    pen.penup()


# A first burst scatters pink strokes through the inside of the heart.
for i in range(1000):
    angle = r.uniform(0, 2 * m.pi)
    scale = r.uniform(0.5, 15.5)
    x, y = heart(angle, scale)
    length = r.uniform(4, 14)
    draw_streak(x, y, length, (0.12, 0.43), (0.42, 0.94), 0.45, 1.2)
    if i % 25 == 0:
        screen.update()
    time.sleep(0.0018)

# A second, denser burst fills the heart and brightens its outer edge.
for i in range(3500):
    angle = r.uniform(0, 2 * m.pi)
    scale = r.uniform(0.5, 15.5)
    x, y = heart(angle, scale)
    length = r.uniform(2, 12)
    draw_streak(x, y, length, (0.10, 0.35), (0.45, 0.95), 0.55, 1.55)
    if i % 25 == 0:
        screen.update()
    time.sleep(0.0018)

screen.update()
t.done()
