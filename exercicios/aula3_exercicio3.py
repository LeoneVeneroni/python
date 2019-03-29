import math
def zen():
    cateto_oposto = float(input('Insira a sombra do corpo em metros: '))
    cateto_adjacente = float(input('Insira a altura do corpo em metros: '))
    tangente_theta = cateto_oposto/cateto_adjacente
    theta = math.atan(tangente_theta)
    print('O ângulo zenital do Sol é: ')
    print(theta, 'em radianos')
    print(math.degrees(theta), 'em graus')

zen()