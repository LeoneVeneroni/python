class Ponto:
    """ Cria um novo Ponto, com coordenadas x, y """

    def __init__(self, x=0, y=0):
        """ Inicializa em x, y o novo ponto criado pela classe """
        self.x = x
        self.y = y

    def distancia_da_origem(self):
        """ Calcula a distância da origem """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def distancia(self, t):
        """ Calcula a distância entre as partículas """
        return (((self.x - t.x) ** 2) + ((self.y - t.y) ** 2)) ** 0.5

print("Partícula 1")
x = int(input('Insira a distância para a origem em x: '))
y = int(input('Insira a distância para a origem em y: '))
p = Ponto(x, y)
print(p.x)       
print(p.y)
print("distância da origem para p: ", p.distancia_da_origem()) # distância da origem
print("="*50)
print("Partícula 2")
x = int(input('Insira a distância para a origem em x: '))
y = int(input('Insira a distância para a origem em y: '))
q = Ponto(x, y)
print(q.x)
print(q.y)
print("distância da origem para q: ", q.distancia_da_origem())

print("A distância entre as partículas é: ", p.distancia(q))

