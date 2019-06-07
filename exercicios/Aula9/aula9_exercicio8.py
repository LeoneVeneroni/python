import math as m
from Ponto import *
import turtle

class Circulo:
    
    """Representa um circulo"""
    
    def __init__(self, raio=0, centro = Ponto(0,0)):
        """ Inicializa o círculo a partir do ponto centro e do parâmetro raio"""
        self.raio = raio
        self.centro = centro
        

    def desenhar_circulo(self, t):
        """Desenha um círculo definido dos parâmetros fornecidos"""
        t.penup()
        t.goto(self.centro.x, self.centro.y)               # Posiciona o cursor no centro do círculo
        t.forward(self.raio)
        t.pendown()
        t.left(90)
        for i in range(90):                                # Desenha o círculo
            t.forward(2*m.pi*self.raio/90)
            t.left(4)

janela = turtle.Screen()
tartaruga = turtle.Turtle()

Circulo(75, Ponto(150, 100)).desenhar_circulo(tartaruga)

janela.mainloop()
