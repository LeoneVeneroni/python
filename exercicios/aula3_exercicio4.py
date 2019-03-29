def converter():
    x1 = float(input('Insira a distância percorrida em milhas: '))
    y1 = x1 * 1.60934
    x2 = float(input('Insira o tempo gasto em minutos: '))
    y2 = x2 / 60
    z = float(y1 / y2)
    print('A velocidade média é', z, 'km/h')
    print('O tempo gasto por quilômetro é', 1/z, 'h/km')

converter()
