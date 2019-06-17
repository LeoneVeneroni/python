import matplotlib.pyplot as plt

arquivo = open('dados_alunos.txt')

linhas = arquivo.readlines()

idade = []
altura = []
massa = []

for i in linhas:
    coluna = i.strip().split()
    idade.append(int(coluna[0]))
    altura.append(float(coluna[1]))
    massa.append(float(coluna[2]))
    print(coluna)

plt.hist(x=idade, bins=30, range=(15, 45))
plt.xlabel('idade (anos)')
plt.ylabel('frequência')
plt.title('Histrograma da idade dos estudantes')
plt.show()

plt.hist(x=altura, bins=10, range=(1.5, 2))
plt.xlabel('altura (m)')
plt.ylabel('frequência')
plt.title('Histrograma da altura dos estudantes')
plt.show()

plt.hist(x=massa, bins=80, range=(40, 120))
plt.xlabel('massa (kg)')
plt.ylabel('frequência')
plt.title('Histrograma da massa dos estudantes')
plt.show()