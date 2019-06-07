def velo1():
    xi = float(input('Insira a posição inicial: '))
    xf = float(input('Insira a posição final: '))
    t = float(input('Insira o tempo transcorrido: '))
    v = (xf - xi) / t
    print('Velocidade média = ', v)


velo1()


def velo2():
    vi = float(input('Insira a velocidade inicial: '))
    t2 = float(input('Insira o tempo transcorrido: '))
    a = float(input('Insira a aceleração constante: '))
    v2 = vi + a * t2
    print('Velocidade final = ', v2)


velo2()
