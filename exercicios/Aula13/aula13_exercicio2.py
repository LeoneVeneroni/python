import matplotlib.pyplot as plt
import numpy as np

# Primeiro trecho
d0 = 0  # posição inicial 
d1a = 5  # distância percorrida no primeiro trecho
v1 = 12  # velocidade constante deste trecho
t1a = (5/12) * 60  # tempo gasto no deslocamento do primeiro trecho
t1 = [i for i in np.arange(0, t1a+0.01, 0.01)]  # lista contendo intervalos de 0.01 minuto até
d1 = [d0 + v1/60 * ti for ti in t1]

# Segundo trecho
d2a = 0.2  # distância percorrida no segundo trecho
v2 = 15  # velocidade final após a aceleração em 200 metros
a = (v2**2 - v1**2) / (2 * d2a)  # aceleração
t2a = round(((v2 - v1) / a) * 60, 2)  # tempo gasto no deslocamento do segundo trecho
t2 = [i for i in np.arange(t1a, t1a+t2a+0.01, 0.01)]
d2 = [d1[-1] + v2/60 * (ti - t1a) + (a* (ti - t1a)**2) / 7200 for ti in t2]

# Terceiro trecho
d3a = 1.8  # distância percorrida no terceiro trecho
t3a = round((d3a/v2) * 60, 2)  # tempo gasto no deslocamento do terceiro trecho
t3 = [i for i in np.arange(t2a+t1a, t2a+t1a+t3a+0.01, 0.01)]   
d3 = [d2[-1] + v2/60 * (ti - (t1a + t2a)) for ti in t3]

plt.plot(t1, d1)
plt.plot(t2, d2)
plt.plot(t3, d3)
plt.xlabel('tempo (min)')
plt.ylabel('distância (km)')
plt.show()

