a1 = int(input('Digite o primeiro valor da lista: '))
a2 = int(input('Digite o segundo valor da lista: '))
a3 = int(input('Digite o terceiro valor da lista: '))
a4 = int(input('Digite o quarto valor da lista: '))
a5 = int(input('Digite o quinto valor da lista: '))

A = [a1, a2, a3, a4, a5]
M = max(A)

x = 0
while x <= M:
     if x % 2 == 0 and x in A:
         print(x)
     x = x + 1