class Ponto:
    """ Cria um novo Ponto, com coordenadas x, y """

    def __init__(self, x=0, y=0):
        """ Inicializa em x, y o novo ponto criado pela classe """
        self.x = x
        self.y = y

    def reflexao(self):
        return self.x, -self.y

p = Ponto(3, 5)
print(p.x, p.y)
print(Ponto(3, 5).reflexao())

	
