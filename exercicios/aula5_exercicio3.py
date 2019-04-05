def mult():
    a1 = int(input('Digite o primeiro valor da lista: '))
    a2 = int(input('Digite o segundo valor da lista: '))
    a3 = int(input('Digite o terceiro valor da lista: '))
    a4 = int(input('Digite o quarto valor da lista: '))
    a5 = int(input('Digite o quinto valor da lista: '))
    A = [a1, a2, a3, a4, a5]
    B = A[0]*A[1]*A[2]*A[3]*A[4]    
    print('Produto dos números da lista =', B)
    
mult()    