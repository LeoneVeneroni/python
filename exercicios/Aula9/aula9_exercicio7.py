import turtle

class Ponto:
    """ Cria um novo Ponto, com coordenadas x, y """

    def __init__(self, x=0, y=0):
        """ Inicializa em x, y o novo ponto criado pela classe """
        self.x = x
        self.y = y


class Retangulo:
    """Representa um retângulo"""

    def __init__(self, largura=0, altura=0, canto=Ponto(0, 0)):
        """ Inicializa o retângulo a partir do ponto canto e dos parâmetros largura e altura"""
        self.largura = largura
        self.altura = altura
        self.canto = canto

    def desenhar_ret(self, t):
        """Desenha um retângulo, com vértice inferior esquerdo na posição canto e com largura e altura fornecidos"""
        t.penup()
        t.goto(self.canto.x, self.canto.y)  # Posiciona o cursor no vértice inferior esquerdo
        t.pendown()
        t.forward(self.largura)  # Desenha o retângulo
        t.left(90)
        t.forward(self.altura)
        t.left(90)
        t.forward(self.largura)
        t.left(90)
        t.forward(self.altura)


janela = turtle.Screen()
zequinha = turtle.Turtle()
zequinha.speed(3)

Retangulo(150, 100, Ponto(-50, 50)).desenhar_ret(zequinha)

janela.mainloop()