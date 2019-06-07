n = int(input("Insira uma número maior do que 101: "))

for i in range(102, n):
    if (i % 21 == 0):
        print('O menor número divisível por 21 é', i)
        break
    elif (n < 105):
        print('Nenhum número é divisível por 21 neste intervalo')
 

