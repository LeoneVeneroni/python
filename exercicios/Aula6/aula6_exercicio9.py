import turtle
from math import pi

ta = turtle.Screen()
ta.bgcolor("lightgreen")
ta.title("Círculo boladão")

ciranda = turtle.Turtle()
ciranda.color("hotpink")
ciranda.pensize(4.8)


def polygon(t, length, n):
    alfa = 360 / n
    for i in range(n):
        t.forward(length)
        t.left(alfa)


def circle(t, r):
    circunf = 2 * pi * r
    n = 50
    length = circunf / n
    polygon(t, length, n)


circle(ciranda, 100)

ta.mainloop()
