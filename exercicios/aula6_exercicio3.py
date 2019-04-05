import turtle
jn = turtle.Screen()
jn.bgcolor("yellow")
jn.title("O bonde da tartaruga")

zeca = turtle.Turtle()
zeca.shape("turtle")
zeca.speed(1)
zeca.color("purple")
zeca.pensize(4)

for i in range(8):
	zeca.forward(80)
	zeca.left(45)
	
jn.mainloop() 