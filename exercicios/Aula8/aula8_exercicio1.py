from turtle import Turtle, Screen

def histograma(t, peso):
    """ Faz a tartaruga t desenhar uma bar de um certo "peso" """
    t.begin_fill()           
    t.left(90)
    t.forward(peso)
    t.write("   " + str(peso))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(peso)
    t.left(90)
    t.end_fill()            

A = list() # Cria uma lista vazia
for c in range(7):
    try:
        A.append(int(input('Digite um valor: ')))
    except:
        print('Erro encotrado. Só números inteiros podem ser inseridos.')

cor = list()        # Cria uma lista vazia
cor.append(str(input('Digite a cor da borda: '))) # Cria um elemento para a 1ª posição da lista
cor.append(str(input('Digite a cor do prenchimento: '))) # Cria um elemento para a 2ª posição da lista

tela = Screen()     # Mostra a janela e seus atributos
tela.bgcolor("lightgreen")

touche = Turtle()   # Cria a tartaruga 
touche.pensize(3)
touche.penup()
touche.backward(120)
touche.pendown()

try:
    touche.color(cor[0], cor[1])
except:
    print('Erro encontrado. Você não inseriu uma cor válida.')

for a in A:
    histograma(touche, a)

tela.mainloop()
