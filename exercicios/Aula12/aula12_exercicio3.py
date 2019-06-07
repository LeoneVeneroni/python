import math
import matplotlib.pyplot as plt

S0 = math.exp(0)-math.exp(-10)

n = 10  # Número de trapézios
for i in range(1, n):
	soma = 2*math.exp(-i)

S1 = 1 + soma + math.exp(-(n+1))

print('Resultado numérico (10 trapézios) =', S1)
print("Resultado analítico = ", S0)

precisao = (abs(S1 - S0) / S0) * 100
print("A precisão é de {0}%".format(precisao))