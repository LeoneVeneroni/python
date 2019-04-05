import turtle
le = turtle.Screen()
le.bgcolor("green")
le.title("Loucura, "*3)

jaja = turtle.Turtle()
jaja.color("lavender")
jaja.pensize(5)

def square(t):
	for i in range(4):
		t.forward(120)
		t.left(90)

square(jaja)

jaja.penup()
jaja.forward(80)
jaja.pendown()

def square(bob):
	for i in range(4):
		bob.forward(120)
		bob.left(90)
		
square(jaja)

le.mainloop()