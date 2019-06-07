from typing import List

import matplotlib.pyplot as plt

d0 = 0
dfin = 5
v = 12
t = [i for i in range(0, 31)]  # intervalos de 1 minuto, 30 minutos
d = [d0+v/60 * ti for ti in t]

print(d)

