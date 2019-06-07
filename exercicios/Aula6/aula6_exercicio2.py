import turtle

jn = turtle.Screen()
jn.bgcolor("burlywood")
jn.title("Cor da tartaruga")

leone = turtle.Turtle()
tarta = str(input("Insira a cor da tartaruga: "))
caneta = int(input("Insira o tamanho da tartaruga: "))
leone.color(tarta)
leone.pensize(caneta)

for i in [0,1,2,3]:
	leone.forward(50)
	leone.right(90)

jn.mainloop()  