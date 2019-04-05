import turtle
op = turtle.Screen()
op.bgcolor("lightgreen")
op.title("Polígono pitoresco")

jay = turtle.Turtle()
jay.color("brown")
jay.pensize(4.5)

def polygon(t, length, n):
	alfa = 360/n
	for i in range(n):
		t.forward(length)
		t.left(alfa)

polygon(jay, 120, 6)

op.mainloop()
