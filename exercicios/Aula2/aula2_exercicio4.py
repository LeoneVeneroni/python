print('Laser vermelho - comprimento de onda = 632.8 nm')
print('Distância entre o anteparo e a fenda = 1.98 m')
print('Espaçamento entre as fendas = 0.250 mm')
print('A distância entre dois máximos consecutivos de interferência é')

L=632.8*10**(-9)
D=1.98
d=0.250*10**(-3)
M=(L*D)/d

print(M, 'm')