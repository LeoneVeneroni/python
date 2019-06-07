import turtle
import math

n = int(input('Insira o número de lados do polígono: '))

tela = turtle.Screen()
tela.bgcolor('darkred')
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
tartaruga.speed(3)
tartaruga.color('cyan', 'green')

def poligono(t, L, n):
    """Faz polígonos regulares com n lados"""

    r = L / (2 * math.sin(math.pi / n))
    t.begin_fill()
    for i in range(n):
        t.forward(r)
        t.left(90 + 180 / n)
        t.forward(L)
        t.left(90 + 180 /n)
        t.forward(r)
        t.left(180)
    t.hideturtle()
    t.end_fill()

poligono(tartaruga, 100, n)


tela.mainloop()