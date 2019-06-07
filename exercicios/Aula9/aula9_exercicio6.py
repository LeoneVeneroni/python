import math as m

class Ponto:
    """ Cria um novo Ponto, com coordenadas x, y """

    def __init__(self, x=0, y=0):
        """ Inicializa em x, y o novo ponto criado pela classe """
        self.x = x
        self.y = y

    def ObterPonto(self):
        return self.x, self.y


class Circulo:
    """Representa um círculo. Atributos: centro e raio."""
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio


    def ponto_no_circulo(self, p=Ponto()):
        """Verifica se um ponto está dentro de um círculo (ou na superfície).

        ponto: objeto Ponto
        círculo: objeto Círculo
        """
        d = ((self.centro.x - p.x) ** 2 + (self.centro.y - p.y) ** 2) ** 0.5
        if d <= self.raio:
            return "True"
        else:
            return "False"


p = Ponto(150, 100)
circulo = Circulo(p, 75)
q = Ponto(35, 12)
print('Coordenadas do centro do círculo:', q.ObterPonto())
print('Está dentro do círculo ou na borda?', circulo.ponto_no_circulo(q))

