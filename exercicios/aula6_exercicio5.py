import turtle
jn = turtle.Screen()
jn.bgcolor("firebrick")
jn.title("O bonde da tartaruga")

zeca = turtle.Turtle()
zeca.shape("turtle")
zeca.speed(4)
zeca.color("DarkSalmon")
zeca.pensize(4)

zeca.penup()
zeca.backward(300)
for i in range(4):
	zeca.penup()
	zeca.forward(120)	
	zeca.pendown()
	for j in range(5):
		zeca.forward(80)
		zeca.right(144)

jn.mainloop() 