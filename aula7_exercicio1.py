from turtle import Turtle, Screen

comp = int(input("Qual é o comprimento das pétalas? "))
petala = int(input("Quantas pétalas você deseja? "))

est = Screen()
est.bgcolor('blue')
est.title('Flor de Lis')

leo = Turtle()

leo.color('green', 'limegreen')
leo.pensize(5)

# Posiciona a caneta lá embaixo
leo.penup()
leo.goto(0, -200)
leo.pendown()
leo.left(45)

# Primeira parte do talo (antes da folha)
leo.circle(150, 40)
leo.right(90)

# Comando pra fazer a folha
leo.begin_fill() 
leo.circle(50, 60)
leo.left(120)
leo.circle(50, 60)
leo.end_fill()

# Segunda parte do talo (depois da folha)
leo.right(150)
leo.circle(250, 40)

# Pétalas
leo.color('moccasin', 'gold')
leo.shape("turtle")
leo.pensize(3)
leo.speed(8)

# Aqui faz uma pétala
leo.begin_fill()
def desenho(leo, raio):
    '''Faz uma pétala'''
    heading = leo.heading()
    leo.circle(raio, 60) #(raio do círculo, parte do círculo desenhada em graus)
    leo.left(120)
    leo.circle(raio, 60)
    leo.setheading(heading)

# Comando para fazer as outra pétalas
for c in range(petala):
    desenho(leo, comp)
    leo.left(360 / petala)
leo.end_fill()

leo.hideturtle()

est.mainloop()
