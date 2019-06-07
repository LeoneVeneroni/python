# import matplotlib.pyplot as plt
import math

S0 = math.exp(0)-math.exp(-10)

precisao = 2
n = 10
while precisao > 1:
    S1 = 0
    x1=[(10*i)/n for i in range(0, n)]
    for xi in x1:
        S1 = S1 + math.exp(-xi) * (10/n)
    precisao = ((S1-S0) / S0) * 100
    n += 1

print(f'Resultado numérico (soma de {n-1} caixinhas) = {S1}')
print("Resultado analítico = ",S0)

print(f'A precisão é de {precisao}%')



