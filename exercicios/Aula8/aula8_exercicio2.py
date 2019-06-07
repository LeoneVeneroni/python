import matplotlib.pyplot as plt

x = []
y = []
z = []
for i in range(0, 11):
    x.append(i)
    y.append(i+2 - 2*i + i**2)
    z.append(i+3 - 3*i + i**2)

#x = [0, 1, 2, 3]
# y = [10, 50, 60, 80]
# z = [20, 55, 68, 101]

plt.plot(x, y, 'r+')
plt.scatter(x, z, marker='*', color="red")
plt.title("Teste radical")

plt.xlabel('Tempo (s)')
plt.ylabel('Temperatura (K)')

plt.show()

