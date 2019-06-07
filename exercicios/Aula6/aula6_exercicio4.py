import turtle
jn = turtle.Screen()
jn.bgcolor("yellow")
jn.title("O bonde da tartaruga")

zeca = turtle.Turtle()
zeca.shape("turtle")
zeca.speed(1)
zeca.color("blue violet")
zeca.pensize(4)

for i in range(5):
	zeca.forward(180)
	zeca.right(144)
	
jn.mainloop() 