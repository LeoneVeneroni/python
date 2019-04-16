from turtle import Turtle, Screen

def histograma(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()           # Added this line
    t.left(90)
    t.forward(height)
    t.write("   " + str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()             # Added this line

#xs = [48, 117, 200, 240, 160, 260, 220]

A = list()
for c in range(7):
    try:
        A.append(int(input('Digite um valor: ')))
    except:
        print('Erro encotrado. Só números inteiros podem ser inseridos.')

tela = Screen()         # Set up the window and its attributes
tela.bgcolor("lightgreen")

touche = Turtle()       # Create tess and set some attributes
cor = list()
cor.append(str(input('Digite a cor da borda: ')))
cor.append(str(input('Digite a cor do prenchimento: ')))

try:
    touche.color(cor[0], cor[1])
except:
    print('Erro encontrado. Você não inseriu uma cor válida.')

touche.pensize(3)

touche.penup()
touche.backward(120)
touche.pendown()

for a in A:
    histograma(touche, a)

tela.mainloop()
