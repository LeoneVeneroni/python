class Ponto:
    """ Cria um novo Ponto, com coordenadas x, y """

    def __init__(self, x=0, y=0):
        """ Inicializa em x, y o novo ponto criado pela classe """
        self.x = x
        self.y = y

    def parametros_reta(self, t):
        """ Calcula o coeficiente angular e linear """
        a = (self.y - t.y) / (self.x - t.x)
        return a, self.y - a*self.x

p = Ponto(4, 11)
print(Ponto(4, 11).parametros_reta(Ponto(6, 15)))
