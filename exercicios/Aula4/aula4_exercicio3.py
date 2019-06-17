def miltokm():
    x1 = float(input('Insira a distância percorrida em milhas: '))
    y1 = x1 * 1.60934
    return y1
    
def mintoh():
    x2 = float(input('Insira o tempo gasto em minutos: '))
    y2 = x2 / 60
    return y2

def kmtomil():
    x3 = float(input('Insira a distância percorrida em quilômetros: '))
    y3 = x3 / 1.60934
    return y3

def htomin():
    x4 = float(input('Insira o tempo gasto em horas: '))
    y4 = x4 * 60
    return y4

m1 = miltokm()
m2 = mintoh()
    
z1 = float(m1 / m2)
print('A velocidade média é', z1, 'km/h')
print('O tempo gasto por quilômetro é', 1/z1, 'h/km')    

m3 = kmtomil()
m4 = htomin()

z2 = float(m3 / m4)
print('A velocidade média é', z2, 'milhas/min')
print('O tempo gasto por quilômetro é', 1/z2, 'min/milhas')