import turtle

cor = str(input("Digite a cor de fundo: "))
jn = turtle.Screen()
jn.bgcolor(cor)
jn.title("Cor de fundo")

donatelo = turtle.Turtle()
donatelo.color("purple")
donatelo.pensize(4)

for i in [0,1,2,3]:
	donatelo.forward(50)
	donatelo.right(90)

jn.mainloop()  