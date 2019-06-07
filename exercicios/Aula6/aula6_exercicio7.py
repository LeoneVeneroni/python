import turtle
le = turtle.Screen()
le.bgcolor("lightblue")
le.title("E aí, belezinha? "*2)

alice = turtle.Turtle()
alice.color("gray")
alice.pensize(5)

def square(t, length):
	for i in range(4):
		t.forward(length)
		t.left(90)

square(alice, 150)

le.mainloop() 
