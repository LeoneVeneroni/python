import turtle
import math

ge = turtle.Screen()
ge.bgcolor("red")
ge.title("Círculo da felicidade")

gira = turtle.Turtle()
gira.color("lightgreen")
gira.pensize(4.8)


def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def circle(t, r):
    arc(t, r, 360)

circle(gira, 50)

ge.mainloop()
