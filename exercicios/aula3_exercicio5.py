import math as m


def teste():
    alt = float(input('Insira sua altura em metros: '))
    massa = float(input('Insira sua massa em quilos: '))
    imc = massa / alt ** 2
    print('Seu IMC é de', imc)


teste()


def volume():
    r = float(input('Insira o raio da esfera em centímetros: '))
    V = (4 / 3) * m.pi * r ** 3
    print('O volume de uma esfera é de', V, 'cm³')


volume()


def dif():
    L = float(input('Insira o comprimento de onda do laser (em nanômetro): '))
    D = float(input('Insira a distância entre o anteparo e a fenda (em metro): '))
    E = float(input('Insira o espaçamento entre as fendas (em milímetro): '))
    M = (L * 10 ** (-9) * D) / (E * 10 ** (-3))
    print('A distância entre dois máximos consecutivos de interferência é de', M, 'm')


dif()
